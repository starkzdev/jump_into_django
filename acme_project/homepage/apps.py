"""Конфигурация приложения Homepage для проекта acme_project."""

from django.apps import AppConfig


class HomepageConfig(AppConfig):
    """Настройки приложения Homepage."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "homepage"
    verbose_name = "Главная страница"
