# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class RefundReferences(DataObject):

    __merchant_reference: Optional[str] = None

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Note that the maximum length of this field for transactions processed on the GlobalCollect platform is 30. Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files.

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(RefundReferences, self).to_dictionary()
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundReferences':
        super(RefundReferences, self).from_dictionary(dictionary)
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
