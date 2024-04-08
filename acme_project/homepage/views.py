"""Представления (views) приложения Homepage."""

from django.shortcuts import render


def index(request):
    """Главная страница сайта с промо-товаром."""
    template_name = "homepage/index.html"
    title = "Главная страница ACME"
    promo_product = {
        "id": 1,
        "name": "Iron carrot",
    }
    context = {
        "title": title,
        "promo_product": promo_product,
    }
    return render(request, template_name, context)
