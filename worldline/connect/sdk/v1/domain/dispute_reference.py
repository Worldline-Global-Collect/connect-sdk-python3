# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class DisputeReference(DataObject):

    __merchant_order_id: Optional[str] = None
    __merchant_reference: Optional[str] = None
    __payment_reference: Optional[str] = None
    __provider_id: Optional[str] = None
    __provider_reference: Optional[str] = None

    @property
    def merchant_order_id(self) -> Optional[str]:
        """
        | The merchant’s order ID of the transaction to which this dispute is linked.
        
        Type: str
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value: Optional[str]) -> None:
        self.__merchant_order_id = value

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Your (unique) reference for the transaction that you can use to reconcile our report files.
        
        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

    @property
    def payment_reference(self) -> Optional[str]:
        """
        | Payment Reference generated by WebCollect.
        
        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value: Optional[str]) -> None:
        self.__payment_reference = value

    @property
    def provider_id(self) -> Optional[str]:
        """
        | The numerical identifier of the Service Provider (Acquirer).
        
        Type: str
        """
        return self.__provider_id

    @provider_id.setter
    def provider_id(self, value: Optional[str]) -> None:
        self.__provider_id = value

    @property
    def provider_reference(self) -> Optional[str]:
        """
        | The Service Provider’s reference.
        
        Type: str
        """
        return self.__provider_reference

    @provider_reference.setter
    def provider_reference(self, value: Optional[str]) -> None:
        self.__provider_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeReference, self).to_dictionary()
        if self.merchant_order_id is not None:
            dictionary['merchantOrderId'] = self.merchant_order_id
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.payment_reference is not None:
            dictionary['paymentReference'] = self.payment_reference
        if self.provider_id is not None:
            dictionary['providerId'] = self.provider_id
        if self.provider_reference is not None:
            dictionary['providerReference'] = self.provider_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeReference':
        super(DisputeReference, self).from_dictionary(dictionary)
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'providerId' in dictionary:
            self.provider_id = dictionary['providerId']
        if 'providerReference' in dictionary:
            self.provider_reference = dictionary['providerReference']
        return self
