import pytest
from src.item import Item
from src.phone import Phone

phone_1 = Phone("iPhone 14", 120_000, 5, 2)


def test_item_init():
    assert phone_1.name == 'iPhone 14'
    assert phone_1.price == 120000
    assert phone_1.quantity == 5
    assert phone_1.number_of_sim == 2


def test_phone_and_phone_addition():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 80_000, 2, 3)
    assert phone1 + phone2 == 7


def test_item_and_phone_addition():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
