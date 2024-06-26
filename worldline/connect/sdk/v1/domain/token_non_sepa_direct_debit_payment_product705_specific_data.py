# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.bank_account_bban import BankAccountBban


class TokenNonSepaDirectDebitPaymentProduct705SpecificData(DataObject):

    __authorisation_id: Optional[str] = None
    __bank_account_bban: Optional[BankAccountBban] = None

    @property
    def authorisation_id(self) -> Optional[str]:
        """
        | Core reference number for the direct debit instruction in UK

        Type: str
        """
        return self.__authorisation_id

    @authorisation_id.setter
    def authorisation_id(self, value: Optional[str]) -> None:
        self.__authorisation_id = value

    @property
    def bank_account_bban(self) -> Optional[BankAccountBban]:
        """
        | Object containing account holder name and bank account information

        Type: :class:`worldline.connect.sdk.v1.domain.bank_account_bban.BankAccountBban`
        """
        return self.__bank_account_bban

    @bank_account_bban.setter
    def bank_account_bban(self, value: Optional[BankAccountBban]) -> None:
        self.__bank_account_bban = value

    def to_dictionary(self) -> dict:
        dictionary = super(TokenNonSepaDirectDebitPaymentProduct705SpecificData, self).to_dictionary()
        if self.authorisation_id is not None:
            dictionary['authorisationId'] = self.authorisation_id
        if self.bank_account_bban is not None:
            dictionary['bankAccountBban'] = self.bank_account_bban.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TokenNonSepaDirectDebitPaymentProduct705SpecificData':
        super(TokenNonSepaDirectDebitPaymentProduct705SpecificData, self).from_dictionary(dictionary)
        if 'authorisationId' in dictionary:
            self.authorisation_id = dictionary['authorisationId']
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBban()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        return self
