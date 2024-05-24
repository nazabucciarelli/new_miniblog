from django.shortcuts import (
    render,
    redirect
)
from django.views import View
from product.models import ProductReview
from product.repositories.product_review import ProductReviewRepository


product_review_repository = ProductReviewRepository()

class ProductReviewListView(View):
    def get(self,request):
        product_reviews = product_review_repository.get_all()
        return render(
            request,
            'product_reviews/list.html',
            dict(
                product_reviews=product_reviews
            )
        )
    
    def update(self,request):
        ...

class ProductReviewCreateView(View):
    def get(self,request):
        return render(
            request,
            'product_reviews/create.html',
        )