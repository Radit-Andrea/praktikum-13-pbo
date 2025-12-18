class Product:
    """
    Model data produk.
    """

    def __init__(self, product_id: int, name: str, price: int):
        self.product_id = product_id
        self.name = name
        self.price = price
