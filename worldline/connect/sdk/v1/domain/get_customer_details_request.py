# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import List, Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.key_value_pair import KeyValuePair


class GetCustomerDetailsRequest(DataObject):
    """
    | Input for the retrieval of a customer's details.
    """

    __country_code: Optional[str] = None
    __values: Optional[List[KeyValuePair]] = None

    @property
    def country_code(self) -> Optional[str]:
        """
        | The code of the country where the customer should reside.

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def values(self) -> Optional[List[KeyValuePair]]:
        """
        | A list of keys with a value used to retrieve the details of a customer. Depending on the country code, different keys are required. These can be determined with a getPaymentProduct call and using payment product properties with the property usedForLookup set to true.

        Type: list[:class:`worldline.connect.sdk.v1.domain.key_value_pair.KeyValuePair`]
        """
        return self.__values

    @values.setter
    def values(self, value: Optional[List[KeyValuePair]]) -> None:
        self.__values = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetCustomerDetailsRequest, self).to_dictionary()
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.values is not None:
            dictionary['values'] = []
            for element in self.values:
                if element is not None:
                    dictionary['values'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetCustomerDetailsRequest':
        super(GetCustomerDetailsRequest, self).from_dictionary(dictionary)
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'values' in dictionary:
            if not isinstance(dictionary['values'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['values']))
            self.values = []
            for element in dictionary['values']:
                value = KeyValuePair()
                self.values.append(value.from_dictionary(element))
        return self
