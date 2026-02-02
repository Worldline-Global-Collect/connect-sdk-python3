# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class BaseBillingDetails(DataObject):

    __description: Optional[str] = None

    @property
    def description(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self.__description = value

    def to_dictionary(self) -> dict:
        dictionary = super(BaseBillingDetails, self).to_dictionary()
        if self.description is not None:
            dictionary['description'] = self.description
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'BaseBillingDetails':
        super(BaseBillingDetails, self).from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        return self
