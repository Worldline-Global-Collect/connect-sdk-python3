# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.click_to_pay_configuration_mastercard import ClickToPayConfigurationMastercard
from worldline.connect.sdk.v1.domain.click_to_pay_configuration_visa import ClickToPayConfigurationVisa
from worldline.connect.sdk.v1.domain.click_to_pay_display_hints import ClickToPayDisplayHints


class ClickToPayConfiguration(DataObject):
    """
    | Object containing the configuration parameters for each scheme supporting Click to Pay for the provided country and currency combination. These parameters initialize SRC System SDK for the scheme. This object is only returned for card products with allowsClickToPay set to true.
    """

    __display_hints: Optional[ClickToPayDisplayHints] = None
    __mastercard: Optional[ClickToPayConfigurationMastercard] = None
    __visa: Optional[ClickToPayConfigurationVisa] = None

    @property
    def display_hints(self) -> Optional[ClickToPayDisplayHints]:
        """
        | Object containing Click to Pay logo display hints

        Type: :class:`worldline.connect.sdk.v1.domain.click_to_pay_display_hints.ClickToPayDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value: Optional[ClickToPayDisplayHints]) -> None:
        self.__display_hints = value

    @property
    def mastercard(self) -> Optional[ClickToPayConfigurationMastercard]:
        """
        | Scheme onboarding value returned for the card products supporting Click to Pay with Mastercard.

        Type: :class:`worldline.connect.sdk.v1.domain.click_to_pay_configuration_mastercard.ClickToPayConfigurationMastercard`
        """
        return self.__mastercard

    @mastercard.setter
    def mastercard(self, value: Optional[ClickToPayConfigurationMastercard]) -> None:
        self.__mastercard = value

    @property
    def visa(self) -> Optional[ClickToPayConfigurationVisa]:
        """
        | Scheme onboarding value returned for the card products supporting Click to Pay with Visa.

        Type: :class:`worldline.connect.sdk.v1.domain.click_to_pay_configuration_visa.ClickToPayConfigurationVisa`
        """
        return self.__visa

    @visa.setter
    def visa(self, value: Optional[ClickToPayConfigurationVisa]) -> None:
        self.__visa = value

    def to_dictionary(self) -> dict:
        dictionary = super(ClickToPayConfiguration, self).to_dictionary()
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.mastercard is not None:
            dictionary['mastercard'] = self.mastercard.to_dictionary()
        if self.visa is not None:
            dictionary['visa'] = self.visa.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ClickToPayConfiguration':
        super(ClickToPayConfiguration, self).from_dictionary(dictionary)
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = ClickToPayDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'mastercard' in dictionary:
            if not isinstance(dictionary['mastercard'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mastercard']))
            value = ClickToPayConfigurationMastercard()
            self.mastercard = value.from_dictionary(dictionary['mastercard'])
        if 'visa' in dictionary:
            if not isinstance(dictionary['visa'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['visa']))
            value = ClickToPayConfigurationVisa()
            self.visa = value.from_dictionary(dictionary['visa'])
        return self
