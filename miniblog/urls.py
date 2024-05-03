from django.contrib import admin
from django.urls import path, include

from product.views.product_view import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")),
    path('',index_view,name="index")
]