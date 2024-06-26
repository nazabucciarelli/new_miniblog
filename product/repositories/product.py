#import logging
from typing import List, Optional

from product.models import Category, Product


#logger = logging.getLogger(__name__)


class ProductRepository:

    def get_all(self) -> List[Product]:
        return Product.objects.all()

    def filter_by_id(self, id: int) -> Optional[Product]:
        return Product.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Product]:
        try:
            product = Product.objects.get(id=id)
        except:
            product = None
        return product

    def get_product_on_price_range(
        self,
        min_price: float,
        max_price: float,
    ) -> List[Product]:
        #products = Product.objects.filter(
        #    price__gt=min_price,
        #    price__lt=max_price,
        #)
        products = Product.objects.filter(
            price__range=(min_price, max_price)
        )

        return products

    def create(
        self,
        nombre: str,
        precio: float,
        descripcion: Optional[str] = None,
        cantidades: Optional[int] = 0,
        categoria: Optional[Category] = None,
    ):
        return Product.objects.create(
            name=nombre,
            price=precio,
            description=descripcion,
            stock=cantidades,
            category=categoria,
        )

    def filter_by_category(
        self,
        categoria: Category,
    ) -> List[Product]:
        return Product.objects.filter(category=categoria)

    def filter_by_category_name(
        self,
        nombre_categoria: str,
    ) -> List[Product]:
        return Product.objects.filter(
            category__name=nombre_categoria
        )

    def delete(self, producto: Product):
        return producto.delete()
    

    def get_product_gte_stock():
        ...

    def get_product_lte_stock():
        ...

    def update(self,
               product: Product,
               nombre: str,
               precio: float,
               descripcion: str,
               stock: int,
               categoria: Category) -> Product:
        if int(stock) < 0:
            raise ValueError("No se puede tener stock en negativo")
        product.name = nombre
        product.price = precio
        product.stock = stock
        product.description = descripcion
        product.category = categoria
        product.save()
        return product
