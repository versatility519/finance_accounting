from django.apps import AppConfig

class ShippingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.shipping'
    verbose_name = 'Shipping Management'

    def ready(self):
        try:
            import apps.shipping.signals  # noqa
        except ImportError:
            pass
