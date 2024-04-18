# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney


class GiftCardPurchase(DataObject):
    """
    | Object containing information on purchased gift card(s)
    """

    __amount_of_money: Optional[AmountOfMoney] = None
    __number_of_gift_cards: Optional[int] = None

    @property
    def amount_of_money(self) -> Optional[AmountOfMoney]:
        """
        | Object containing information on an amount of money

        Type: :class:`worldline.connect.sdk.v1.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: Optional[AmountOfMoney]) -> None:
        self.__amount_of_money = value

    @property
    def number_of_gift_cards(self) -> Optional[int]:
        """
        | Number of gift cards that are purchased through this transaction

        Type: int
        """
        return self.__number_of_gift_cards

    @number_of_gift_cards.setter
    def number_of_gift_cards(self, value: Optional[int]) -> None:
        self.__number_of_gift_cards = value

    def to_dictionary(self) -> dict:
        dictionary = super(GiftCardPurchase, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.number_of_gift_cards is not None:
            dictionary['numberOfGiftCards'] = self.number_of_gift_cards
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GiftCardPurchase':
        super(GiftCardPurchase, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'numberOfGiftCards' in dictionary:
            self.number_of_gift_cards = dictionary['numberOfGiftCards']
        return self
