from django.apps import AppConfig


class LopezConfig(AppConfig):
    name = 'lopez'
    verbose_name = 'Viral Videos'

    def ready(self):
        from .signals import inform_administrators
        from .checks import settings_check
