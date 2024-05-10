from django.shortcuts import render, redirect

from product.repositories.category import CategoryRepository

category_repository = CategoryRepository()

def category_list(request):
    categorias = category_repository.get_all()

    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )


def category_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category_repository.create(name=name)
        return redirect("category_list")

    return render(request,
                  'categories/create.html')


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


def category_delete(request,id):
    category = category_repository.get_by_id(id)
    category_repository.delete(category)
    return redirect('category_list')
