from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="ID of the product")
    quantity: int = Field(..., gt=0, description="Quantity of the product in the cart")

class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(None, description="ID of the product")
    quantity: int = Field(None, gt=0, description="Updated quantity of the product in the cart")

class CartItem(BaseModel):
    product_id:int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity of the product in the cart")
    subtotal: float = Field(..., description="Subtotal price for this cart item (price * quantity)")
    image_url: Optional[str] = Field(None, description="URL of the product image")


class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in the cart")
    total: float = Field(..., description="Total price of all items in the cart")
    items_count: int = Field(..., description="Total number of items in the cart")