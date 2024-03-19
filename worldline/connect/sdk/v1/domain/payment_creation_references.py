# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class PaymentCreationReferences(DataObject):

    __additional_reference: Optional[str] = None
    __external_reference: Optional[str] = None

    @property
    def additional_reference(self) -> Optional[str]:
        """
        | The additional reference identifier for this transaction. Data in this property will also be returned in our report files, allowing you to reconcile them.
        
        Type: str
        """
        return self.__additional_reference

    @additional_reference.setter
    def additional_reference(self, value: Optional[str]) -> None:
        self.__additional_reference = value

    @property
    def external_reference(self) -> Optional[str]:
        """
        | The external reference identifier for this transaction. Data in this property will also be returned in our report files, allowing you to reconcile them.
        
        Type: str
        """
        return self.__external_reference

    @external_reference.setter
    def external_reference(self, value: Optional[str]) -> None:
        self.__external_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentCreationReferences, self).to_dictionary()
        if self.additional_reference is not None:
            dictionary['additionalReference'] = self.additional_reference
        if self.external_reference is not None:
            dictionary['externalReference'] = self.external_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentCreationReferences':
        super(PaymentCreationReferences, self).from_dictionary(dictionary)
        if 'additionalReference' in dictionary:
            self.additional_reference = dictionary['additionalReference']
        if 'externalReference' in dictionary:
            self.external_reference = dictionary['externalReference']
        return self
