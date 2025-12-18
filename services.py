from abc import ABC, abstractmethod


# ===============================
# PAYMENT ABSTRACTION
# ===============================

class IPaymentProcessor(ABC):
    """
    Interface pembayaran.
    """

    @abstractmethod
    def pay(self, amount: int):
        pass


class CashPayment(IPaymentProcessor):
    """
    Implementasi pembayaran tunai.
    """

    def pay(self, amount: int):
        print(f"Pembayaran tunai sebesar Rp{amount} berhasil")


class DebitCardPayment(IPaymentProcessor):
    """
    Challenge OCP/DIP: pembayaran kartu debit.
    """

    def pay(self, amount: int):
        print(f"Pembayaran debit sebesar Rp{amount} berhasil")


# ===============================
# CART SERVICE
# ===============================

class CartService:
    """
    Service untuk mengelola keranjang belanja.
    """

    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self) -> int:
        return sum(item.price for item in self.items)
