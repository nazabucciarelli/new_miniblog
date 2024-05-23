from django.shortcuts import (
    render,
    redirect
)

from product.models import Supplier
from product.repositories.supplier import SupplierRepository

supplier_repository = SupplierRepository()


def supplier_list(request):
    suppliers = supplier_repository.get_all()
    return render(
        request,
        'suppliers/list.html',
        dict(
            suppliers=suppliers
        ))


def supplier_detail(request, id):
    supplier = supplier_repository.get_by_id(id)
    return render(
        request,
        'suppliers/detail.html',
        dict(
            supplier=supplier
        ))


def supplier_delete(request, id):
    supplier = supplier_repository.get_by_id(id)
    supplier.delete()
    return redirect('supplier_list')


def supplier_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        supplier_repository.create(name, address, phone)
        return redirect('supplier_list')

    return render(
        request,
        'suppliers/create.html'
    )


def supplier_update(request,id):
    supplier = supplier_repository.get_by_id(id)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        supplier_repository.update(supplier,name,address,phone)
        return redirect('supplier_list')
    
    return render(
        request,
        'suppliers/update.html',
        dict(
            supplier=supplier
        )
    )
