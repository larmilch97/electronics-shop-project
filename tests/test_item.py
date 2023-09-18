from src.item import Item
import pytest
import csv

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


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


def test_name():
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_check_name():
    try:
        item1.name = 'СуперСмартфон'
        Item.check_name(item1.name)
    except Exception as ex:
        assert ex.args[0] == "Длина наименования товара превышает 10 символов."


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == "Смартфон"
