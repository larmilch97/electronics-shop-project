from src.item import Item
import pytest


@pytest.fixture


def class_fixture_1():
    item_test_1 = Item("Смартфон", 10000, 20)
    return item_test_1


@pytest.fixture


def class_fixture_2():
    item_test_2 = Item("Ноутбук", 20000, 5)
    return item_test_2


def test_calculate_total_price(class_fixture_1):
    assert class_fixture_1.calculate_total_price() == 200000


def test_calculate_total_price_2(class_fixture_2):
    assert class_fixture_2.calculate_total_price() == 100000


def test_apply_1(class_fixture_1):
    assert class_fixture_1.apply_discount() == 10000


def test_apply_2(class_fixture_2):
    assert class_fixture_2.apply_discount() == 20000.0
