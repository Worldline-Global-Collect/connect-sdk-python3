# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.address_personal import AddressPersonal


class CapturePaymentShipping(DataObject):

    __address: Optional[AddressPersonal] = None
    __email_address: Optional[str] = None
    __shipped_from_zip: Optional[str] = None
    __tracking_number: Optional[str] = None

    @property
    def address(self) -> Optional[AddressPersonal]:
        """
        | Object containing address information

        Type: :class:`worldline.connect.sdk.v1.domain.address_personal.AddressPersonal`
        """
        return self.__address

    @address.setter
    def address(self, value: Optional[AddressPersonal]) -> None:
        self.__address = value

    @property
    def email_address(self) -> Optional[str]:
        """
        | Email address linked to the shipping

        Type: str
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value: Optional[str]) -> None:
        self.__email_address = value

    @property
    def shipped_from_zip(self) -> Optional[str]:
        """
        | The zip/postal code of the location from which the goods were shipped.

        Type: str
        """
        return self.__shipped_from_zip

    @shipped_from_zip.setter
    def shipped_from_zip(self, value: Optional[str]) -> None:
        self.__shipped_from_zip = value

    @property
    def tracking_number(self) -> Optional[str]:
        """
        | Shipment tracking number

        Type: str
        """
        return self.__tracking_number

    @tracking_number.setter
    def tracking_number(self, value: Optional[str]) -> None:
        self.__tracking_number = value

    def to_dictionary(self) -> dict:
        dictionary = super(CapturePaymentShipping, self).to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address
        if self.shipped_from_zip is not None:
            dictionary['shippedFromZip'] = self.shipped_from_zip
        if self.tracking_number is not None:
            dictionary['trackingNumber'] = self.tracking_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CapturePaymentShipping':
        super(CapturePaymentShipping, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = AddressPersonal()
            self.address = value.from_dictionary(dictionary['address'])
        if 'emailAddress' in dictionary:
            self.email_address = dictionary['emailAddress']
        if 'shippedFromZip' in dictionary:
            self.shipped_from_zip = dictionary['shippedFromZip']
        if 'trackingNumber' in dictionary:
            self.tracking_number = dictionary['trackingNumber']
        return self
