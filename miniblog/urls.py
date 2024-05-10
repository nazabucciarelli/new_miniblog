from django.contrib import admin
from django.urls import path, include

from product.views.product_view import index_view
from product.views.category_view import category_list, category_create, category_delete, category_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")),
    path('',index_view,name="index"),
    path('categories/', view=category_list,name="category_list"),
    path('categories/create',view=category_create,name="category_create"),
    path('categories/delete/<int:id>',view=category_delete,name="category_delete"),
    path('categories/update/<int:id>',view=category_update,name="category_update")
]