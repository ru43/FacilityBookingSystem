from django.apps import AppConfig


class ObsappConfig(AppConfig):
    name = 'obsapp'
    def ready(self):
        import obsapp.signals
