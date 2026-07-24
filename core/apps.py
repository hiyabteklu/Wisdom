from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        try:
            from django.contrib.sites.models import Site
            Site.objects.update_or_create(
                id=1,
                defaults={
                    'domain': 'wisdom-1-qp71.onrender.com',
                    'name': 'Wisdom'
                }
            )
        except Exception:
            pass
