# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.bank_account_bban import BankAccountBban
from worldline.connect.sdk.v1.domain.bank_account_iban import BankAccountIban


class BankDetails(DataObject):

    __bank_account_bban: Optional[BankAccountBban] = None
    __bank_account_iban: Optional[BankAccountIban] = None

    @property
    def bank_account_bban(self) -> Optional[BankAccountBban]:
        """
        | Object that holds the Basic Bank Account Number (BBAN) data

        Type: :class:`worldline.connect.sdk.v1.domain.bank_account_bban.BankAccountBban`
        """
        return self.__bank_account_bban

    @bank_account_bban.setter
    def bank_account_bban(self, value: Optional[BankAccountBban]) -> None:
        self.__bank_account_bban = value

    @property
    def bank_account_iban(self) -> Optional[BankAccountIban]:
        """
        | Object that holds the International Bank Account Number (IBAN) data

        Type: :class:`worldline.connect.sdk.v1.domain.bank_account_iban.BankAccountIban`
        """
        return self.__bank_account_iban

    @bank_account_iban.setter
    def bank_account_iban(self, value: Optional[BankAccountIban]) -> None:
        self.__bank_account_iban = value

    def to_dictionary(self) -> dict:
        dictionary = super(BankDetails, self).to_dictionary()
        if self.bank_account_bban is not None:
            dictionary['bankAccountBban'] = self.bank_account_bban.to_dictionary()
        if self.bank_account_iban is not None:
            dictionary['bankAccountIban'] = self.bank_account_iban.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'BankDetails':
        super(BankDetails, self).from_dictionary(dictionary)
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBban()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        if 'bankAccountIban' in dictionary:
            if not isinstance(dictionary['bankAccountIban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountIban']))
            value = BankAccountIban()
            self.bank_account_iban = value.from_dictionary(dictionary['bankAccountIban'])
        return self
