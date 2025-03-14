# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class SchemeTokenData(DataObject):

    __cardholder_name: Optional[str] = None
    __cryptogram: Optional[str] = None
    __eci: Optional[str] = None
    __network_token: Optional[str] = None
    __token_expiry_date: Optional[str] = None

    @property
    def cardholder_name(self) -> Optional[str]:
        """
        | The card holder's name on the card. Minimum length of 2, maximum length of 51 characters.

        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value: Optional[str]) -> None:
        self.__cardholder_name = value

    @property
    def cryptogram(self) -> Optional[str]:
        """
        | The Token Cryptogram is a dynamic one-time use value that is used to verify the authenticity of the transaction and the integrity of the data used in the generation of the Token Cryptogram. Visa calls this the Token Authentication Verification Value (TAVV) cryptogram.

        Type: str
        """
        return self.__cryptogram

    @cryptogram.setter
    def cryptogram(self, value: Optional[str]) -> None:
        self.__cryptogram = value

    @property
    def eci(self) -> Optional[str]:
        """
        | The Electronic Commerce Indicator you got with the Token Cryptogram

        Type: str
        """
        return self.__eci

    @eci.setter
    def eci(self, value: Optional[str]) -> None:
        self.__eci = value

    @property
    def network_token(self) -> Optional[str]:
        """
        | The network token. Note: This is called Payment Token in the EMVCo documentation

        Type: str
        """
        return self.__network_token

    @network_token.setter
    def network_token(self, value: Optional[str]) -> None:
        self.__network_token = value

    @property
    def token_expiry_date(self) -> Optional[str]:
        """
        | The expiry date of the network token

        Type: str
        """
        return self.__token_expiry_date

    @token_expiry_date.setter
    def token_expiry_date(self, value: Optional[str]) -> None:
        self.__token_expiry_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(SchemeTokenData, self).to_dictionary()
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.cryptogram is not None:
            dictionary['cryptogram'] = self.cryptogram
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.network_token is not None:
            dictionary['networkToken'] = self.network_token
        if self.token_expiry_date is not None:
            dictionary['tokenExpiryDate'] = self.token_expiry_date
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SchemeTokenData':
        super(SchemeTokenData, self).from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'cryptogram' in dictionary:
            self.cryptogram = dictionary['cryptogram']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'networkToken' in dictionary:
            self.network_token = dictionary['networkToken']
        if 'tokenExpiryDate' in dictionary:
            self.token_expiry_date = dictionary['tokenExpiryDate']
        return self
