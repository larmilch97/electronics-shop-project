import pytest
from src.keyboard import Keyboard


def test_keyboard_creation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
