"""Конфигурация приложения Catalog для проекта acme_project."""

from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """Настройки приложения Catalog."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "catalog"
    verbose_name = "Каталог"
