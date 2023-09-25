from src.item import Item


class MixingLang:
    _language = "EN"

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'RU'
        return self

    @property
    def language(self):
        return self._language


class Keyboard(Item, MixingLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.name = name

    @classmethod
    def check_name(cls, name):
        return cls.name
