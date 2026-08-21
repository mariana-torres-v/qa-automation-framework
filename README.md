# QA Automation Framework

Framework de automatización de pruebas reutilizable, basado en **BDD (Behave)**, **Page Object Model** y con soporte dual para **Web** (Playwright) y **Mobile** (Appium).

Está pensado para dar de alta distintos proyectos de automatización (por ejemplo `bykon` y `Multiva`) sobre un mismo núcleo (`core/`) sin duplicar lógica de arranque de navegador/driver, esperas, logging ni reporting.

## Contenido

- [Arquitectura](#arquitectura)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Tecnologías](#tecnologías)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración (.env)](#configuración-env)
- [Ejecución de pruebas](#ejecución-de-pruebas)
- [Tags disponibles](#tags-disponibles)
- [Reportes y evidencias](#reportes-y-evidencias)
- [Proyectos automatizados](#proyectos-automatizados)
- [Pendientes / notas conocidas](#pendientes--notas-conocidas)

## Arquitectura

El framework separa el **núcleo reutilizable** (`core/`) de los **proyectos** (`proyectos/`), cada uno con sus propias features, steps, locators, páginas y datos de prueba.

- `core/environment_base.py` — `EnvironmentManager`, punto único que decide si una ejecución es **web** o **mobile** según el userdata `platform` de Behave, arranca el driver correspondiente y arma el `PageManager` del proyecto.
- `core/browser.py` / `core/web/playwright_driver.py` — arranque y cierre de Playwright (chromium/firefox/webkit), local o (a futuro) BrowserStack.
- `core/mobile/appium_driver.py` — arranque y cierre de la sesión Appium (UiAutomator2 / Android).
- `core/web/base_page.py` — Page Object base para Web: abrir URL, click, fill, esperas, capturas, etc.
- `core/mobile/base_page.py` — Page Object base para Mobile: esperas explícitas, click, escritura, scroll (incluyendo scroll por `UiScrollable`), regreso al landing, logging de cada acción.
- `core/waits.py` — esperas explícitas reutilizables para Web (visible, hidden, attached, detached).
- `core/logger/logging.py` — logger único (`FrameworkLogger`) compartido por todo el framework.
- Cada proyecto define su propio `PageManager` (por ejemplo `proyectos/bykon/page_manager.py` y `proyectos/Multiva/mobile/page_manager.py`), que expone las páginas ya instanciadas (`context.pages.login`, `context.pages.home`, etc.) a los steps de Behave.

## Estructura del proyecto

```
qa-automation-framework/
├── behave.ini                  # Config raíz de Behave (paths por defecto: bykon)
├── requirements.txt
├── core/                       # Núcleo reutilizable del framework
│   ├── browser.py              # BrowserManager (Playwright)
│   ├── config.py               # Config central (lee variables de entorno)
│   ├── environment_base.py     # EnvironmentManager (hooks before_all/after_all, web/mobile)
│   ├── waits.py
│   ├── logger/
│   ├── reporting/               # (reservado para reporting adicional)
│   ├── utils/
│   ├── web/                    # Playwright driver + BasePage web
│   └── mobile/                 # Appium driver + BasePage mobile
├── proyectos/
│   ├── bykon/                  # Proyecto de referencia / smoke de arquitectura (Web)
│   │   ├── behave.ini
│   │   ├── page_manager.py
│   │   ├── locators/
│   │   ├── pages/
│   │   └── features/
│   │       ├── environment.py
│   │       ├── google.feature
│   │       └── steps/
│   └── Multiva/
│       └── mobile/             # App bancaria Multiva (Mobile / Appium)
│           ├── data.py         # Datos/masa de prueba
│           ├── page_manager.py # MobilePageManager
│           ├── locators/
│           ├── pages/
│           └── features/
│               ├── environment.py
│               ├── steps/
│               ├── 1 login.feature
│               ├── 2 alta destinatario.feature
│               ├── 3 editar destinatario.feature
│               ├── 4 eliminar destinatario.feature
│               ├── 5 transferencias.feature
│               ├── 6 consulta.feature
│               ├── 7 estado de cuenta.feature
│               └── full_flow.feature
├── docs/                       # Documentación del framework (presentación .pptx)
├── reports/
│   ├── allure-results/         # Salida de Allure
│   └── screenshots/            # Capturas automáticas en fallos (mobile)
└── notes                       # Notas de diseño rápidas
```

## Tecnologías

- **Python** 3.10+
- **Behave** — BDD (Gherkin: features + steps)
- **Playwright** — automatización Web
- **Appium** (`Appium-Python-Client`) + **Selenium** — automatización Mobile (Android / UiAutomator2)
- **Allure** (`allure-behave`, `allure-python-commons`) — reporting y evidencias
- **python-dotenv** style config vía variables de entorno (`core/config.py`)

## Requisitos previos

- Python 3.10 o superior
- Google Chrome/Chromium instalado (Playwright descarga sus propios binarios)
- Para pruebas mobile:
  - [Appium Server](https://appium.io/) corriendo (`APPIUM_SERVER`, por defecto `http://127.0.0.1:4723`)
  - Un emulador/dispositivo Android disponible y con la app QA instalada (`APP_PACKAGE` / `APP_ACTIVITY` en `.env`)
  - `UiAutomator2` configurado en Appium

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/mariana-torres-v/qa-automation-framework.git
cd qa-automation-framework

# 2. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar los navegadores de Playwright
playwright install
```

## Configuración (.env)

El framework lee su configuración desde variables de entorno mediante `core/config.py`. Crea un archivo `.env` en la raíz (o exporta las variables en tu shell) con algo similar a esto:

```dotenv
# Entorno de ejecución
EXECUTION_ENV=local          # local | browserstack (browserstack aún no implementado)
PLATFORM=web                 # web | mobile

# Web / Playwright
BASE_URL=https://www.google.com
BROWSER=chromium             # chromium | firefox | webkit
HEADLESS=False
TIMEOUT=30000

# Mobile / Appium
APPIUM_SERVER=http://127.0.0.1:4723
PLATFORM_NAME=Android
AUTOMATION_NAME=UiAutomator2
DEVICE_NAME=Android
APP_PACKAGE=net.veritran.mvmx.p3.qa
APP_ACTIVITY=.VTCommonActivity
NO_RESET=True
FORCE_APP_LAUNCH=True

# BrowserStack (pendiente de integrar)
BROWSERSTACK_USERNAME=
BROWSERSTACK_ACCESS_KEY=
BROWSERSTACK_PROJECT=QA Framework
BROWSERSTACK_BUILD=local
BROWSERSTACK_SESSION_NAME=Smoke Test
```

> ⚠️ El archivo `.env` actual del repo no está en `.gitignore` y `proyectos/Multiva/mobile/data.py` guarda una contraseña de prueba en texto plano. Si el repo llega a hacerse público o se comparte, conviene mover esas credenciales a variables de entorno / un `.env` ignorado por git.

## Ejecución de pruebas

Behave decide entre Web y Mobile según el userdata `platform` (definido en `EnvironmentManager.before_all`), así que **siempre hay que indicarlo con `-D platform=web` o `-D platform=mobile`**.

### Proyecto `bykon` (Web — smoke de arquitectura)

El `behave.ini` de la raíz ya apunta a estas features por defecto:

```bash
behave -D platform=web
```

Explícito:

```bash
behave proyectos/bykon/features -D platform=web
```

### Proyecto `Multiva` (Mobile — app bancaria)

Requiere Appium levantado y el emulador/dispositivo conectado:

```bash
behave proyectos/Multiva/mobile/features -D platform=mobile
```

Ejecutar solo un feature o un tag específico:

```bash
behave proyectos/Multiva/mobile/features -D platform=mobile --tags=@login
```

## Tags disponibles

En las features de `Multiva` se usan tags para poder filtrar ejecuciones:

| Tag | Descripción |
|---|---|
| `@login` | Inicio de sesión |
| `@destinatarios @alta @spei @spei_e2e` | Alta de destinatario SPEI |
| `@transferencias @cuentas_propias` | Transferencia entre cuentas propias |
| `@transferencias @terceros_multiva` | Transferencia a tercero Multiva |
| `@transferencias @spei` | Transferencia SPEI |
| `@consulta @movimientos` | Consulta del último movimiento por tipo de cuenta |
| `@e2e` | Recorrido completo: alta → edición → transferencia → consulta → estado de cuenta → eliminación |

## Reportes y evidencias

- `reports/allure-results/` — resultados crudos generados por `allure-behave` (usar `allure serve reports/allure-results` para visualizarlos, requiere tener instalado Allure CLI).
- `reports/screenshots/` — capturas automáticas de pantalla que se generan en `after_step` cuando un step falla (solo mobile, ver `proyectos/Multiva/mobile/features/environment.py`).

## Proyectos automatizados

### `bykon` (Web)

Feature única (`google.feature`) que valida que la arquitectura del framework (Playwright + Page Object + Behave) funciona correctamente contra Google. Sirve como base/plantilla para agregar nuevas páginas (`LoginPage`, `HomePage`, etc., ya dejadas comentadas en `page_manager.py` como ejemplo).

### `Multiva` (Mobile)

Automatización end-to-end de la app bancaria Multiva sobre Android vía Appium, cubriendo:

- Login
- Alta, edición y eliminación de destinatarios (SPEI y Multiva)
- Transferencias (cuentas propias, terceros Multiva, SPEI)
- Consulta de movimientos
- Consulta de estado de cuenta
- Un flujo E2E (`full_flow.feature`) que encadena todo lo anterior

## Pendientes / notas conocidas

- La integración con **BrowserStack** está declarada en `core/browser.py` y `core/config.py` pero **no implementada** (`_start_browserstack` lanza `NotImplementedError`).
- Algunos steps de `2 alta destinatario.feature` están comentados a la espera de validar assertions adicionales (confirmación de operación, modal de seguridad, etc.).
- `core/reporting/` y `core/utils/` existen como carpetas reservadas para el framework pero aún no tienen contenido.
- `test_appium.py`, `test_base_page.py` y `test_config.py` en la raíz son scripts sueltos de prueba manual/exploratoria del framework, no tests automatizados formales (y algunos tienen imports desactualizados, p. ej. `from mobile...` en vez de `from core.mobile...`).
- Revisar mover credenciales de prueba (`proyectos/Multiva/mobile/data.py`) fuera del código versionado.
