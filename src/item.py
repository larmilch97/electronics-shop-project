class Item:
    """
    Класс для представления товара в магазине.
    """
    all = []
    pay_rate = 1.0


    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.all.append(self)
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self) -> float:
        return self.price * self.quantity


    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price