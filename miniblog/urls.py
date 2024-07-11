from django.contrib import admin
from django.urls import path, include

from product.views.category_view import category_list, category_create, category_delete, category_update
from product.views.supplier_view import supplier_detail, supplier_list, supplier_create, supplier_delete, supplier_update
from product.views.product_review_view import ProductReviewListView, ProductReviewCreateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")),
    path('categories', view=category_list, name="category_list"),
    path('categories/create', view=category_create, name="category_create"),
    path('categories/delete/<int:id>',
         view=category_delete, name="category_delete"),
    path('categories/update/<int:id>',
         view=category_update, name="category_update"),
    path('suppliers', view=supplier_list, name="supplier_list"),
    path('suppliers/<int:id>', view=supplier_detail, name="supplier_detail"),
    path('suppliers/create', view=supplier_create, name="supplier_create"),
    path('suppliers/delete/<int:id>',
         view=supplier_delete, name="supplier_delete"),
    path('suppliers/update/<int:id>',
         view=supplier_update, name="supplier_update"),
    path(route='product_reviews/', view=ProductReviewListView.as_view(),
         name="product_reviews_list"),
    path(route='product_reviews/create/',
         view=ProductReviewCreateView.as_view(), name="product_reviews_create")
] + static(settings.MEDIA_URL, document_roots=settings.MEDIA_ROOT)
