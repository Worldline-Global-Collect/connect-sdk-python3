# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class CapturePaymentRequest(DataObject):

    __amount: Optional[int] = None
    __is_final: Optional[bool] = None

    @property
    def amount(self) -> Optional[int]:
        """
        | Here you can specify the amount that you want to capture (specified in cents, where single digit currencies are presumed to have 2 digits).
        | The amount can be lower than the amount that was authorized, but not higher.
        | If left empty, the full amount will be captured and the request will be final.
        | If the full amount is captured, the request will also be final.

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: Optional[int]) -> None:
        self.__amount = value

    @property
    def is_final(self) -> Optional[bool]:
        """
        | This property indicates whether this will be the final capture of this transaction.
        | The default value for this property is false.

        Type: bool
        """
        return self.__is_final

    @is_final.setter
    def is_final(self, value: Optional[bool]) -> None:
        self.__is_final = value

    def to_dictionary(self) -> dict:
        dictionary = super(CapturePaymentRequest, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        if self.is_final is not None:
            dictionary['isFinal'] = self.is_final
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CapturePaymentRequest':
        super(CapturePaymentRequest, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'isFinal' in dictionary:
            self.is_final = dictionary['isFinal']
        return self
