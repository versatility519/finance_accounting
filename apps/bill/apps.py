from django.apps import AppConfig


class BillConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bill'

    def ready(self):
        import apps.bill.signals 