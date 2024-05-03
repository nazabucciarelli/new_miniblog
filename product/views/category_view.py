from django.shortcuts import render, redirect

from product.repositories.category import CategoryRepository

def category_list(request):
    category_repository = CategoryRepository()
    categorias = category_repository.get_all()

    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )