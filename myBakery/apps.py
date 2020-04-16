from django.apps import AppConfig


class MybakeryConfig(AppConfig):
    name = 'myBakery'


    def ready(self):
        import myBakery.signals