from django.urls import path

from product.views.product_view import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
)
from product.views.category_view import category_list

urlpatterns = [
    path(route='', view=product_list, name='product_list'),
    path(route='create/',view=product_create, name='product_create'),
    path(route='<int:id>/',view=product_detail,name="product_detail"),
    path(route='<int:id>/update/',view=product_update,name="product_update"),
    path(route='<int:id>/delete/',view=product_delete,name="product_delete"),
    path(route='category/',view=category_list,name='category_list')
]
