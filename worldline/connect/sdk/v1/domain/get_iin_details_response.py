# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import List, Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.iin_detail import IINDetail


class GetIINDetailsResponse(DataObject):
    """
    | Output of the retrieval of the IIN details request
    """

    __co_brands: Optional[List[IINDetail]] = None
    __country_code: Optional[str] = None
    __is_allowed_in_context: Optional[bool] = None
    __payment_product_id: Optional[int] = None

    @property
    def co_brands(self) -> Optional[List[IINDetail]]:
        """
        | Populated only if the card has multiple brands.
        | A list with for every brand of the card, the payment product identifier associated with that brand, and if you submitted a payment context, whether that payment product is allowed in the context.

        Type: list[:class:`worldline.connect.sdk.v1.domain.iin_detail.IINDetail`]
        """
        return self.__co_brands

    @co_brands.setter
    def co_brands(self, value: Optional[List[IINDetail]]) -> None:
        self.__co_brands = value

    @property
    def country_code(self) -> Optional[str]:
        """
        | The ISO 3166-1 alpha-2 country code of the country where the card was issued. If we don't know where the card was issued, then the countryCode will return the value '99'.

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def is_allowed_in_context(self) -> Optional[bool]:
        """
        | Populated only if you submitted a payment context.
        
        * true - The payment product is allowed in the submitted context.
        * false - The payment product is not allowed in the submitted context. Note that in this case, none of the brands of the card will be allowed in the submitted context.

        Type: bool
        """
        return self.__is_allowed_in_context

    @is_allowed_in_context.setter
    def is_allowed_in_context(self, value: Optional[bool]) -> None:
        self.__is_allowed_in_context = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | The payment product identifier associated with the card. If the card has multiple brands, then we select the most appropriate payment product based on your configuration and the payment context, if you submitted one.
        | Please see payment products <https://apireference.connect.worldline-solutions.com/s2sapi/v1/en_US/python/paymentproducts.html> for a full overview of possible values

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(GetIINDetailsResponse, self).to_dictionary()
        if self.co_brands is not None:
            dictionary['coBrands'] = []
            for element in self.co_brands:
                if element is not None:
                    dictionary['coBrands'].append(element.to_dictionary())
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.is_allowed_in_context is not None:
            dictionary['isAllowedInContext'] = self.is_allowed_in_context
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetIINDetailsResponse':
        super(GetIINDetailsResponse, self).from_dictionary(dictionary)
        if 'coBrands' in dictionary:
            if not isinstance(dictionary['coBrands'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['coBrands']))
            self.co_brands = []
            for element in dictionary['coBrands']:
                value = IINDetail()
                self.co_brands.append(value.from_dictionary(element))
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'isAllowedInContext' in dictionary:
            self.is_allowed_in_context = dictionary['isAllowedInContext']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
