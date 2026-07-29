# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class AbstractRedirectPaymentProduct838SpecificInput(DataObject):

    __network_data: Optional[str] = None
    __network_session_token: Optional[str] = None

    @property
    def network_data(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__network_data

    @network_data.setter
    def network_data(self, value: Optional[str]) -> None:
        self.__network_data = value

    @property
    def network_session_token(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__network_session_token

    @network_session_token.setter
    def network_session_token(self, value: Optional[str]) -> None:
        self.__network_session_token = value

    def to_dictionary(self) -> dict:
        dictionary = super(AbstractRedirectPaymentProduct838SpecificInput, self).to_dictionary()
        if self.network_data is not None:
            dictionary['networkData'] = self.network_data
        if self.network_session_token is not None:
            dictionary['networkSessionToken'] = self.network_session_token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AbstractRedirectPaymentProduct838SpecificInput':
        super(AbstractRedirectPaymentProduct838SpecificInput, self).from_dictionary(dictionary)
        if 'networkData' in dictionary:
            self.network_data = dictionary['networkData']
        if 'networkSessionToken' in dictionary:
            self.network_session_token = dictionary['networkSessionToken']
        return self
