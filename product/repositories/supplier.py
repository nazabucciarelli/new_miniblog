from typing import List, Optional

from product.models import Supplier

class SupplierRepository:
    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()
    
    def create(self,name:str,address:str,phone:str) -> Supplier:
        return Supplier.objects.create(name=name,address=address,phone=phone)
    
    def get_by_id(self,id:int) -> Optional[Supplier]:
        try:
            supplier = Supplier.objects.get(id=id)
        except:
            supplier = None
        return supplier
    
    def update(self,supplier:Supplier,name:str,address:str,phone:str) -> Supplier:
        supplier = self.get_by_id(supplier.id)
        supplier.name = name
        supplier.address = address
        supplier.phone = phone
        supplier.save() 
        return supplier

    def delete(self,supplier: Supplier):
        return supplier.delete()