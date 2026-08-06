from core.environment_base import EnvironmentManager

def before_all(context):
    EnvironmentManager.before_all(context)

def after_all(context):
    EnvironmentManager.after_all(context)
