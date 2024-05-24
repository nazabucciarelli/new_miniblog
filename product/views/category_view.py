from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from product.repositories.category import CategoryRepository

category_repository = CategoryRepository()

@login_required(login_url="/login/")
def category_list(request):
    categorias = category_repository.get_all()

    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )

@login_required(login_url="/login/")
def category_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category_repository.create(name=name)
        return redirect("category_list")

    return render(request,
                  'categories/create.html')

@login_required(login_url="/login/")
def category_update(request, id):
    category = category_repository.get_by_id(id)
    if request.method == "POST":
        name = request.POST.get("name")
        category_repository.update(category, name)
        return redirect("category_list")

    return render(request,
                  'categories/update.html',
                  dict(
                      category=category
                  ))

@login_required(login_url="/login/")
def category_delete(request,id):
    category = category_repository.get_by_id(id)
    category_repository.delete(category)
    return redirect('category_list')
