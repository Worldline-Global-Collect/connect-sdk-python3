# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class LodgingCharge(DataObject):
    """
    | Object that holds lodging related charges
    """

    __charge_amount: Optional[int] = None
    __charge_amount_currency_code: Optional[str] = None
    __charge_type: Optional[str] = None

    @property
    def charge_amount(self) -> Optional[int]:
        """
        | Amount of additional charges associated with the stay of the guest.
        | Note: The currencyCode is presumed to be identical to the order.amountOfMoney.currencyCode.

        Type: int
        """
        return self.__charge_amount

    @charge_amount.setter
    def charge_amount(self, value: Optional[int]) -> None:
        self.__charge_amount = value

    @property
    def charge_amount_currency_code(self) -> Optional[str]:
        """
        | Currency for Charge amount. The code should be in 3 letter ISO format.

        Type: str
        """
        return self.__charge_amount_currency_code

    @charge_amount_currency_code.setter
    def charge_amount_currency_code(self, value: Optional[str]) -> None:
        self.__charge_amount_currency_code = value

    @property
    def charge_type(self) -> Optional[str]:
        """
        | Type of additional charges associated with the stay of the guest.Allowed values:
        
        * lodging
        * telephone
        * restaurant
        * minibar
        * giftshop
        * laundry
        * transport
        * gratuity
        * conferenceRoom
        * audiovisual
        * banquet
        * internet
        * earlyDeparture
        * roomService
        * loungeBar
        * other

        Type: str
        """
        return self.__charge_type

    @charge_type.setter
    def charge_type(self, value: Optional[str]) -> None:
        self.__charge_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(LodgingCharge, self).to_dictionary()
        if self.charge_amount is not None:
            dictionary['chargeAmount'] = self.charge_amount
        if self.charge_amount_currency_code is not None:
            dictionary['chargeAmountCurrencyCode'] = self.charge_amount_currency_code
        if self.charge_type is not None:
            dictionary['chargeType'] = self.charge_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LodgingCharge':
        super(LodgingCharge, self).from_dictionary(dictionary)
        if 'chargeAmount' in dictionary:
            self.charge_amount = dictionary['chargeAmount']
        if 'chargeAmountCurrencyCode' in dictionary:
            self.charge_amount_currency_code = dictionary['chargeAmountCurrencyCode']
        if 'chargeType' in dictionary:
            self.charge_type = dictionary['chargeType']
        return self
