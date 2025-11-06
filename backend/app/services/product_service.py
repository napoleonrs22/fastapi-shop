from sqlalchemy.orm import Session
from typing import List
from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository
from ..schemas.product import ProductCreate, ProductResponse, ProductBase, ProductListResponse
from fastapi import HTTPException, status

class ProductService:
    def __init__(self, db:Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)

        
    def get_all_products(self) -> ProductResponse:
        products = self.product_repository.get_all()
        product_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=product_response, total=len(product_response))
    
    def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return ProductResponse.model_validate(product)
    
    def get_products_by_category(self, category_id:int) -> ProductListResponse:

        category = self.category_repository.get_by_id(category_id)

        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        
        products = self.product_repository.get_by_category(category_id)
        products_respone = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_respone, total=len(products_respone))
    
    def create_product(self, product_create: ProductCreate) -> ProductResponse:

        category = self.category_repository.get_by_id(product_create.category_id)

        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        
        new_product = self.product_repository.create(product_create)
        return ProductResponse.model_validate(new_product)