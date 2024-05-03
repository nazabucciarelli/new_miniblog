from typing import List

from product.models import Category

class CategoryRepository:
    def get_all(self) -> List[Category]:
        return Category.objects.all()


# completar repositorio