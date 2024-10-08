"""Apps configuration for the Task model."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration for the API application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
