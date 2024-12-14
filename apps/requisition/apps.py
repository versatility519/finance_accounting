from django.apps import AppConfig


class RequisitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.requisition'

    def ready(self):
        import apps.requisition.signals 