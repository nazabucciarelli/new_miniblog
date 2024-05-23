from typing import List, Optional

from product.models import ProductReview

class ProductReviewRepository:
    def get_all(self) -> List[ProductReview]:
        return ProductReview.objects.all()
    
    def create(self,name:str,address:str,phone:str) -> ProductReview:
        return ProductReview.objects.create(name=name,address=address,phone=phone)
    
    def get_by_id(self,id:int) -> Optional[ProductReview]:
        try:
            supplier = ProductReview.objects.get(id=id)
        except:
            supplier = None
        return supplier
    
    def update(self,supplier:ProductReview,name:str,address:str,phone:str) -> ProductReview:
        supplier = self.get_by_id(supplier.id)
        supplier.name = name
        supplier.address = address
        supplier.phone = phone
        supplier.save() 
        return supplier

    def delete(self,supplier: ProductReview):
        return supplier.delete()