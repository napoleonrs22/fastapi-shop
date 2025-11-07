from .product_routes import router as product_router
from .categories_routes import router as category_router
from .cart_routes import router as cart_router
__all__ = ["product_router", "category_router", "cart_router"]