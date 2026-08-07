from behave import given, when, then


@given("que abro Google")
def step_open_google(context):
    context.pages.google.open()


@when('busco "{texto}"')
def step_search(context, texto):
    context.pages.google.search(texto)
    context.page.keyboard.press("Enter")

    context.page.wait_for_load_state("networkidle")


@then('la página contiene "{texto}"')
def step_validate(context, texto):

    print(context.page.title())

    assert texto in context.page.title()