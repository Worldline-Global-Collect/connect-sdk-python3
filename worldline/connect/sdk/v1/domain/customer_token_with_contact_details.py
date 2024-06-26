# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.v1.domain.contact_details_token import ContactDetailsToken
from worldline.connect.sdk.v1.domain.customer_token import CustomerToken


class CustomerTokenWithContactDetails(CustomerToken):

    __contact_details: Optional[ContactDetailsToken] = None

    @property
    def contact_details(self) -> Optional[ContactDetailsToken]:
        """
        | Object containing contact details like email address and phone number

        Type: :class:`worldline.connect.sdk.v1.domain.contact_details_token.ContactDetailsToken`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value: Optional[ContactDetailsToken]) -> None:
        self.__contact_details = value

    def to_dictionary(self) -> dict:
        dictionary = super(CustomerTokenWithContactDetails, self).to_dictionary()
        if self.contact_details is not None:
            dictionary['contactDetails'] = self.contact_details.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerTokenWithContactDetails':
        super(CustomerTokenWithContactDetails, self).from_dictionary(dictionary)
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = ContactDetailsToken()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        return self
