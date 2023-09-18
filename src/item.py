import csv
import os

src_directory = os.path.abspath(os.path.join(os.path.dirname(__file__)))
path = os.path.join(src_directory, 'items.csv')


class Item:
    all = []
    pay_rate = 1.0

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.all.append(self)
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return str(self.__name)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def check_name(cls, name):
        if len(name) >= 11:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open(path, encoding='windows-1251', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all = [cls((row['name']), float(row['price']), int(row['quantity'])) for row in reader]
        return cls.all

    @staticmethod
    def string_to_number(value: str) -> int:
        return int(float(value))
