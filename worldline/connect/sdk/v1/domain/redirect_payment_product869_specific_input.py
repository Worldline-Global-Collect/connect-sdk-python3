# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class RedirectPaymentProduct869SpecificInput(DataObject):

    __issuer_id: Optional[str] = None
    __resident_id_name: Optional[str] = None
    __resident_id_number: Optional[str] = None

    @property
    def issuer_id(self) -> Optional[str]:
        """
        | ID of the issuing bank of the customer. A list of available issuerIDs can be obtained by using the retrieve payment product directory API.

        Type: str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value: Optional[str]) -> None:
        self.__issuer_id = value

    @property
    def resident_id_name(self) -> Optional[str]:
        """
        | The name as described on the Resident Identity Card of the People's Republic of China.

        Type: str
        """
        return self.__resident_id_name

    @resident_id_name.setter
    def resident_id_name(self, value: Optional[str]) -> None:
        self.__resident_id_name = value

    @property
    def resident_id_number(self) -> Optional[str]:
        """
        | The identification number as described on the Resident Identity Card of the People's Republic of China.

        Type: str
        """
        return self.__resident_id_number

    @resident_id_number.setter
    def resident_id_number(self, value: Optional[str]) -> None:
        self.__resident_id_number = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct869SpecificInput, self).to_dictionary()
        if self.issuer_id is not None:
            dictionary['issuerId'] = self.issuer_id
        if self.resident_id_name is not None:
            dictionary['residentIdName'] = self.resident_id_name
        if self.resident_id_number is not None:
            dictionary['residentIdNumber'] = self.resident_id_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct869SpecificInput':
        super(RedirectPaymentProduct869SpecificInput, self).from_dictionary(dictionary)
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        if 'residentIdName' in dictionary:
            self.resident_id_name = dictionary['residentIdName']
        if 'residentIdNumber' in dictionary:
            self.resident_id_number = dictionary['residentIdNumber']
        return self
