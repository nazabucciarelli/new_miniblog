from django.shortcuts import (
    render,
    redirect
    )

from product.models import Category
from product.repositories.product import ProductRepository
from product.repositories.category import CategoryRepository
from django.contrib.auth.decorators import login_required
from product.forms import ProductForm

repo = ProductRepository()

category_repository = CategoryRepository()

@login_required(login_url="/login/")
def product_list(request):
    productos = repo.get_all()
    return render(
        request,
        'products/list.html',
        dict(
            products=productos
        )
    )

@login_required(login_url="/login/")
def product_detail(request, id):
    producto = repo.get_by_id(id=id)
    return render(
        request,
        'products/detail.html',
        {"product":producto}
    )

@login_required(login_url="/login/")
def product_update(request, id):
    product = repo.get_by_id(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)

        edited_product = repo.update(
            product=product,
            nombre=name,
            descripcion = description,
            precio=float(price),
            stock=stock,
            categoria=category
        )
        return redirect("product_detail",edited_product.id)

    categorias = category_repository.get_all()
    return render(
        request,
        "products/update.html",
        dict(
            categories = categorias,
            product = product
        )
    )

@login_required(login_url="/login/")
def product_delete(request, id):
    product = repo.get_by_id(id=id)
    repo.delete(producto=product)
    return redirect("product_list")

@login_required(login_url="/login/")
def product_create(request):
    form = ProductForm()
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)
        product = repo.create(
            nombre=name,
            descripcion=description,
            precio=float(price),
            cantidades=stock,
            categoria=category
        )
        return redirect("product_detail",product.id)
    
    categories = category_repository.get_all()
    return render(request, 'products/create.html', dict(
        categories=categories,
        form=form
    ))