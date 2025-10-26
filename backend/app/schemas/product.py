from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name : str = Field(..., min_length=5, max_length=100, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0, description="Product price")
    
    category_id: int = Field(..., description= 'Category id')
    image_url: Optional[str] = Field(None, description="URL of the product image")


class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description="Unique identifier for the product")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]

    created_at: datetime = Field(..., description="Timestamp when the product was created")
    category: CategoryResponse = Field(..., description="Category of the product")

    class Config:
        form_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="Total number of products available")