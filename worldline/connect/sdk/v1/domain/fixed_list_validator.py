# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import List, Optional

from worldline.connect.sdk.domain.data_object import DataObject


class FixedListValidator(DataObject):

    __allowed_values: Optional[List[str]] = None

    @property
    def allowed_values(self) -> Optional[List[str]]:
        """
        | List of the allowed values that the field will be validated against
        
        Type: list[str]
        """
        return self.__allowed_values

    @allowed_values.setter
    def allowed_values(self, value: Optional[List[str]]) -> None:
        self.__allowed_values = value

    def to_dictionary(self) -> dict:
        dictionary = super(FixedListValidator, self).to_dictionary()
        if self.allowed_values is not None:
            dictionary['allowedValues'] = []
            for element in self.allowed_values:
                if element is not None:
                    dictionary['allowedValues'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'FixedListValidator':
        super(FixedListValidator, self).from_dictionary(dictionary)
        if 'allowedValues' in dictionary:
            if not isinstance(dictionary['allowedValues'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['allowedValues']))
            self.allowed_values = []
            for element in dictionary['allowedValues']:
                self.allowed_values.append(element)
        return self
