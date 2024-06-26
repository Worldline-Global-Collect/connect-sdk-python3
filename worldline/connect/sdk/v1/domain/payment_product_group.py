# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import List, Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.account_on_file import AccountOnFile
from worldline.connect.sdk.v1.domain.payment_product_display_hints import PaymentProductDisplayHints
from worldline.connect.sdk.v1.domain.payment_product_field import PaymentProductField


class PaymentProductGroup(DataObject):
    """
    | Definition of the details of a single payment product group
    """

    __accounts_on_file: Optional[List[AccountOnFile]] = None
    __allows_installments: Optional[bool] = None
    __device_fingerprint_enabled: Optional[bool] = None
    __display_hints: Optional[PaymentProductDisplayHints] = None
    __fields: Optional[List[PaymentProductField]] = None
    __id: Optional[str] = None

    @property
    def accounts_on_file(self) -> Optional[List[AccountOnFile]]:
        """
        | Only populated in the Client API

        Type: list[:class:`worldline.connect.sdk.v1.domain.account_on_file.AccountOnFile`]
        """
        return self.__accounts_on_file

    @accounts_on_file.setter
    def accounts_on_file(self, value: Optional[List[AccountOnFile]]) -> None:
        self.__accounts_on_file = value

    @property
    def allows_installments(self) -> Optional[bool]:
        """
        | Indicates if the product supports installments
        
        * true - This payment supports installments
        * false - This payment does not support installments

        Type: bool
        """
        return self.__allows_installments

    @allows_installments.setter
    def allows_installments(self, value: Optional[bool]) -> None:
        self.__allows_installments = value

    @property
    def device_fingerprint_enabled(self) -> Optional[bool]:
        """
        | Indicates if device fingerprint is enabled for the product group
        
        * true
        * false

        Type: bool
        """
        return self.__device_fingerprint_enabled

    @device_fingerprint_enabled.setter
    def device_fingerprint_enabled(self, value: Optional[bool]) -> None:
        self.__device_fingerprint_enabled = value

    @property
    def display_hints(self) -> Optional[PaymentProductDisplayHints]:
        """
        | Object containing display hints like the order of the group when shown in a list, the name of the group and the logo. Note that the order of the group is the lowest order among the payment products that belong to the group.

        Type: :class:`worldline.connect.sdk.v1.domain.payment_product_display_hints.PaymentProductDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value: Optional[PaymentProductDisplayHints]) -> None:
        self.__display_hints = value

    @property
    def fields(self) -> Optional[List[PaymentProductField]]:
        """
        | Object containing all the fields and their details that are associated with this payment product group. If you are not interested in the these fields you can have us filter them out (using hide=fields in the query-string)

        Type: list[:class:`worldline.connect.sdk.v1.domain.payment_product_field.PaymentProductField`]
        """
        return self.__fields

    @fields.setter
    def fields(self, value: Optional[List[PaymentProductField]]) -> None:
        self.__fields = value

    @property
    def id(self) -> Optional[str]:
        """
        | The ID of the payment product group in our system

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductGroup, self).to_dictionary()
        if self.accounts_on_file is not None:
            dictionary['accountsOnFile'] = []
            for element in self.accounts_on_file:
                if element is not None:
                    dictionary['accountsOnFile'].append(element.to_dictionary())
        if self.allows_installments is not None:
            dictionary['allowsInstallments'] = self.allows_installments
        if self.device_fingerprint_enabled is not None:
            dictionary['deviceFingerprintEnabled'] = self.device_fingerprint_enabled
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.fields is not None:
            dictionary['fields'] = []
            for element in self.fields:
                if element is not None:
                    dictionary['fields'].append(element.to_dictionary())
        if self.id is not None:
            dictionary['id'] = self.id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductGroup':
        super(PaymentProductGroup, self).from_dictionary(dictionary)
        if 'accountsOnFile' in dictionary:
            if not isinstance(dictionary['accountsOnFile'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['accountsOnFile']))
            self.accounts_on_file = []
            for element in dictionary['accountsOnFile']:
                value = AccountOnFile()
                self.accounts_on_file.append(value.from_dictionary(element))
        if 'allowsInstallments' in dictionary:
            self.allows_installments = dictionary['allowsInstallments']
        if 'deviceFingerprintEnabled' in dictionary:
            self.device_fingerprint_enabled = dictionary['deviceFingerprintEnabled']
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'fields' in dictionary:
            if not isinstance(dictionary['fields'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['fields']))
            self.fields = []
            for element in dictionary['fields']:
                value = PaymentProductField()
                self.fields.append(value.from_dictionary(element))
        if 'id' in dictionary:
            self.id = dictionary['id']
        return self
