from django.shortcuts import (
    render,
    redirect
    )

from product.models import Category
from product.repositories.product import ProductRepository

repo = ProductRepository()

def index_view(request):
    return render(
        request,
        'index/index.html'
    )

def product_list(request):
    productos = repo.get_all()
    return render(
        request,
        'products/list.html',
        dict(
            products=productos
        )
    )

def product_detail(request, id):
    producto = repo.get_by_id(id=id)
    return render(
        request,
        'products/detail.html',
        {"product":producto}
    )

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

    categorias = Category.objects.all()
    return render(
        request,
        "products/update.html",
        dict(
            categories = categorias,
            product = product
        )
    )

def product_delete(request, id):
    product = repo.get_by_id(id=id)
    repo.delete(producto=product)
    return redirect("product_list")

def product_create(request):
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
    
    # TODO reemplazar esta linea con el repositorio de categorias
    categories = Category.objects.all()
    return render(request, 'products/create.html', dict(
        categories=categories
    ))