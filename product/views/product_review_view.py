from django.shortcuts import (
    render,
    redirect
)
from django.views import View
from product.models import ProductReview
from product.repositories.product_review import ProductReviewRepository
from product.repositories.product import ProductRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

product_review_repository = ProductReviewRepository()
product_repository = ProductRepository()

@method_decorator(login_required(login_url='/login/'), name='dispatch')
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

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProductReviewCreateView(View):
    def get(self,request):
        products = product_repository.get_all()
        return render(
            request,
            'product_reviews/create.html',
            dict(
                products = products
            )
        )
    
    def post(self, request):
        id_product = request.POST.get('id_product')
        author =request.user
        review =  request.POST.get('review')
        date = request.POST.get('data')
        rating = request.POST.get('rating')
        product = product_repository.get_by_id(id_product)
        print(request)
        product_review_repository.create(
            product=product,
            author=author,
            text=review,
            date=date,
            rating=rating)

        return redirect("product_reviews_list")

