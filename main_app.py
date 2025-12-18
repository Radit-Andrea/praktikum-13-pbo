from repositories import ProductRepository
from services import CartService, CashPayment, DebitCardPayment


class PosApp:
    """
    Orchestrator aplikasi POS.
    """

    def __init__(self, product_repo, cart_service, payment_processor):
        self.product_repo = product_repo
        self.cart_service = cart_service
        self.payment_processor = payment_processor

    def run(self):
        print("=== APLIKASI POS SEDERHANA ===")
        print("1. Buku (5000)")
        print("2. Pulpen (3000)")
        print("3. Penghapus (2000)")
        print("0. Bayar")

        while True:
            choice = int(input("Pilih produk: "))

            if choice == 0:
                total = self.cart_service.calculate_total()
                self.payment_processor.pay(total)
                break

            product = self.product_repo.get_by_id(choice)
            if product:
                self.cart_service.add_item(product)
                print(f"{product.name} ditambahkan ke keranjang")
            else:
                print("Produk tidak ditemukan")


# ===============================
# MAIN ENTRY POINT
# ===============================

if __name__ == "__main__":
    product_repo = ProductRepository()
    cart_service = CartService()

    # === CHALLENGE OCP/DIP ===
    # GANTI BARIS INI SAJA
    payment_method = DebitCardPayment()
    # payment_method = CashPayment()

    app = PosApp(product_repo, cart_service, payment_method)
    app.run()
