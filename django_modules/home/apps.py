from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'django_modules.home'
    verbose_name = 'home'
    
    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass