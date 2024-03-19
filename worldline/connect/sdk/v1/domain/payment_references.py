# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class PaymentReferences(DataObject):

    __merchant_order_id: Optional[int] = None
    __merchant_reference: Optional[str] = None
    __payment_reference: Optional[str] = None
    __provider_id: Optional[str] = None
    __provider_merchant_id: Optional[str] = None
    __provider_reference: Optional[str] = None
    __reference_orig_payment: Optional[str] = None

    @property
    def merchant_order_id(self) -> Optional[int]:
        """
        | Your order ID for this transaction that is also returned in our report files
        
        Type: int
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value: Optional[int]) -> None:
        self.__merchant_order_id = value

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files.
        
        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

    @property
    def payment_reference(self) -> Optional[str]:
        """
        | Payment Reference generated by WebCollect
        
        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value: Optional[str]) -> None:
        self.__payment_reference = value

    @property
    def provider_id(self) -> Optional[str]:
        """
        | Provides an additional means of reconciliation for Gateway merchants
        
        Type: str
        """
        return self.__provider_id

    @provider_id.setter
    def provider_id(self, value: Optional[str]) -> None:
        self.__provider_id = value

    @property
    def provider_merchant_id(self) -> Optional[str]:
        """
        | Provides an additional means of reconciliation, this is the MerchantId used at the provider
        
        Type: str
        """
        return self.__provider_merchant_id

    @provider_merchant_id.setter
    def provider_merchant_id(self, value: Optional[str]) -> None:
        self.__provider_merchant_id = value

    @property
    def provider_reference(self) -> Optional[str]:
        """
        | Provides an additional means of reconciliation for Gateway merchants
        
        Type: str
        """
        return self.__provider_reference

    @provider_reference.setter
    def provider_reference(self, value: Optional[str]) -> None:
        self.__provider_reference = value

    @property
    def reference_orig_payment(self) -> Optional[str]:
        """
        | When you did not supply a merchantReference for your payment, you need to fill this property with the reference of the original payment when you want to refund it
        
        Type: str
        """
        return self.__reference_orig_payment

    @reference_orig_payment.setter
    def reference_orig_payment(self, value: Optional[str]) -> None:
        self.__reference_orig_payment = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentReferences, self).to_dictionary()
        if self.merchant_order_id is not None:
            dictionary['merchantOrderId'] = self.merchant_order_id
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.payment_reference is not None:
            dictionary['paymentReference'] = self.payment_reference
        if self.provider_id is not None:
            dictionary['providerId'] = self.provider_id
        if self.provider_merchant_id is not None:
            dictionary['providerMerchantId'] = self.provider_merchant_id
        if self.provider_reference is not None:
            dictionary['providerReference'] = self.provider_reference
        if self.reference_orig_payment is not None:
            dictionary['referenceOrigPayment'] = self.reference_orig_payment
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentReferences':
        super(PaymentReferences, self).from_dictionary(dictionary)
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'providerId' in dictionary:
            self.provider_id = dictionary['providerId']
        if 'providerMerchantId' in dictionary:
            self.provider_merchant_id = dictionary['providerMerchantId']
        if 'providerReference' in dictionary:
            self.provider_reference = dictionary['providerReference']
        if 'referenceOrigPayment' in dictionary:
            self.reference_orig_payment = dictionary['referenceOrigPayment']
        return self
