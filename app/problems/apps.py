from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProblemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'problems'
    verbose_name = _('Problems')
    icon = 'fa fa-users-viewfinder'  # Add your icon class here