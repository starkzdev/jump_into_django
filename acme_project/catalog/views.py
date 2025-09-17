"""Представления (views) для приложения Catalog."""

from django.shortcuts import render


def product_list(request):
    """Отображает список товаров."""
    template_name = "catalog/product_list.html"
    title = "Список товаров ACME"
    products = [
        "Iron carrot",
        "Giant mousetrap",
        "Dehydrated boulders",
        "Invisible paint",
    ]
    context = {
        "title": title,
        "products": products,
    }
    return render(request, template_name, context)


def product_detail(request, pk):
    """Отображает карточку товара по его ID."""
    template_name = "catalog/product_detail.html"
    title = "Карточка товара"
    product = f"Товар №{pk}"
    context = {
        "title": title,
        "product": product,
    }
    return render(request, template_name, context)
