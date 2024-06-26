# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class MobilePaymentProductSession302SpecificInput(DataObject):

    __display_name: Optional[str] = None
    __domain_name: Optional[str] = None
    __validation_url: Optional[str] = None

    @property
    def display_name(self) -> Optional[str]:
        """
        | Used as an input for the Apple Pay payment button. Provide your company name in a human readable form.

        Type: str
        """
        return self.__display_name

    @display_name.setter
    def display_name(self, value: Optional[str]) -> None:
        self.__display_name = value

    @property
    def domain_name(self) -> Optional[str]:
        """
        | Provide a fully qualified domain name of your own payment page that will be showing an Apple Pay button.

        Type: str
        """
        return self.__domain_name

    @domain_name.setter
    def domain_name(self, value: Optional[str]) -> None:
        self.__domain_name = value

    @property
    def validation_url(self) -> Optional[str]:
        """
        | Provide the validation URL that has been provided by Apple once you have started an Apple Pay session.

        Type: str
        """
        return self.__validation_url

    @validation_url.setter
    def validation_url(self, value: Optional[str]) -> None:
        self.__validation_url = value

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentProductSession302SpecificInput, self).to_dictionary()
        if self.display_name is not None:
            dictionary['displayName'] = self.display_name
        if self.domain_name is not None:
            dictionary['domainName'] = self.domain_name
        if self.validation_url is not None:
            dictionary['validationUrl'] = self.validation_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentProductSession302SpecificInput':
        super(MobilePaymentProductSession302SpecificInput, self).from_dictionary(dictionary)
        if 'displayName' in dictionary:
            self.display_name = dictionary['displayName']
        if 'domainName' in dictionary:
            self.domain_name = dictionary['domainName']
        if 'validationUrl' in dictionary:
            self.validation_url = dictionary['validationUrl']
        return self
