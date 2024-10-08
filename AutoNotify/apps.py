from django.apps import AppConfig


class AutonotifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AutoNotify'


    def ready(self):
        import AutoNotify.signals