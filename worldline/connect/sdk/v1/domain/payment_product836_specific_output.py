# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class PaymentProduct836SpecificOutput(DataObject):

    __security_indicator: Optional[str] = None

    @property
    def security_indicator(self) -> Optional[str]:
        """
        | Indicates if SofortBank could estabilish if the transaction could successfully be processed.
        
        * 0 - You should wait for the transaction to be reported as paid before shipping any goods.
        * 1 - You can ship the goods. In case the transaction is not reported as paid you can initiate a claims process with SofortBank.

        Type: str
        """
        return self.__security_indicator

    @security_indicator.setter
    def security_indicator(self, value: Optional[str]) -> None:
        self.__security_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct836SpecificOutput, self).to_dictionary()
        if self.security_indicator is not None:
            dictionary['securityIndicator'] = self.security_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct836SpecificOutput':
        super(PaymentProduct836SpecificOutput, self).from_dictionary(dictionary)
        if 'securityIndicator' in dictionary:
            self.security_indicator = dictionary['securityIndicator']
        return self
