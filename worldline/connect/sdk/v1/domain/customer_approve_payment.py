# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class CustomerApprovePayment(DataObject):

    __account_type: Optional[str] = None

    @property
    def account_type(self) -> Optional[str]:
        """
        | Type of the customer account that is used to place this order. Can have one of the following values:
        
        * none - The account that was used to place the order is a guest account or no account was used at all
        * created - The customer account was created during this transaction
        * existing - The customer account was an already existing account prior to this transaction

        Type: str
        """
        return self.__account_type

    @account_type.setter
    def account_type(self, value: Optional[str]) -> None:
        self.__account_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(CustomerApprovePayment, self).to_dictionary()
        if self.account_type is not None:
            dictionary['accountType'] = self.account_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerApprovePayment':
        super(CustomerApprovePayment, self).from_dictionary(dictionary)
        if 'accountType' in dictionary:
            self.account_type = dictionary['accountType']
        return self
