# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class CompanyInformation(DataObject):

    __name: Optional[str] = None
    __vat_number: Optional[str] = None

    @property
    def name(self) -> Optional[str]:
        """
        | Name of company, as a customer

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: Optional[str]) -> None:
        self.__name = value

    @property
    def vat_number(self) -> Optional[str]:
        """
        | Local VAT number of the company

        Type: str
        """
        return self.__vat_number

    @vat_number.setter
    def vat_number(self, value: Optional[str]) -> None:
        self.__vat_number = value

    def to_dictionary(self) -> dict:
        dictionary = super(CompanyInformation, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name
        if self.vat_number is not None:
            dictionary['vatNumber'] = self.vat_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CompanyInformation':
        super(CompanyInformation, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'vatNumber' in dictionary:
            self.vat_number = dictionary['vatNumber']
        return self
