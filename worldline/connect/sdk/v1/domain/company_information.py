# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class CompanyInformation(DataObject):

    __date_of_incorporation: Optional[str] = None
    __name: Optional[str] = None
    __vat_number: Optional[str] = None

    @property
    def date_of_incorporation(self) -> Optional[str]:
        """
        | The date of incorporation is the specific date when the company was registered with the relevant authority.
        | Format: YYYYMMDD

        Type: str
        """
        return self.__date_of_incorporation

    @date_of_incorporation.setter
    def date_of_incorporation(self, value: Optional[str]) -> None:
        self.__date_of_incorporation = value

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
        if self.date_of_incorporation is not None:
            dictionary['dateOfIncorporation'] = self.date_of_incorporation
        if self.name is not None:
            dictionary['name'] = self.name
        if self.vat_number is not None:
            dictionary['vatNumber'] = self.vat_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CompanyInformation':
        super(CompanyInformation, self).from_dictionary(dictionary)
        if 'dateOfIncorporation' in dictionary:
            self.date_of_incorporation = dictionary['dateOfIncorporation']
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'vatNumber' in dictionary:
            self.vat_number = dictionary['vatNumber']
        return self
