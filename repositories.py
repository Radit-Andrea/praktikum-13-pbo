from models import Product


class ProductRepository:
    """
    Repository sebagai lapisan data produk.
    """

    def __init__(self):
        self.products = {
            1: Product(1, "Buku", 5000),
            2: Product(2, "Pulpen", 3000),
            3: Product(3, "Penghapus", 2000)
        }

    def get_by_id(self, product_id: int) -> Product:
        return self.products.get(product_id)
