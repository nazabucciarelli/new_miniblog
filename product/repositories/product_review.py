from typing import List, Optional

from product.models import ProductReview,Product
from datetime import date

class ProductReviewRepository:
    def get_all(self) -> List[ProductReview]:
        return ProductReview.objects.all()
    
    def create(self,product:Product,author:str,text:str,date:date,rating:int) -> ProductReview:
        return ProductReview.objects.create(product=product,author=author,text=text,date=date,rating=rating)
    
    def get_by_id(self,id:int) -> Optional[ProductReview]:
        try:
            product_review = ProductReview.objects.get(id=id)
        except:
            product_review = None
        return product_review
    
    def update(self,product_review:ProductReview,product:Product,author:str,text:str, date:date,rating:int) -> ProductReview:
        product_review = self.get_by_id(product_review.id)
        product_review.product = product
        product_review.author = author
        product_review.text = text
        product_review.date = date
        product_review.rating = rating
        product_review.save() 
        return product_review

    def delete(self,supplier: ProductReview):
        return supplier.delete()