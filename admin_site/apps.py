from django.apps import AppConfig


class AdminSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_site'

    def ready(self):
        import admin_site.signals