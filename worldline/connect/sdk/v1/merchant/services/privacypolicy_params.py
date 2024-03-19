# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import List, Optional

from worldline.connect.sdk.communication.param_request import ParamRequest
from worldline.connect.sdk.communication.request_param import RequestParam


class PrivacypolicyParams(ParamRequest):
    """
    Query parameters for Get privacy policy
    
    See also https://apireference.connect.worldline-solutions.com/s2sapi/v1/en_US/python/services/privacypolicy.html
    """

    __locale: Optional[str] = None
    __payment_product_id: Optional[int] = None

    @property
    def locale(self) -> Optional[str]:
        """
        | Locale in which the privacy policy should be returned. Uses your default locale when none is provided.
        
        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | ID of the payment product for which you wish to retrieve the privacy policy. When no ID is provided you will receive all privacy policies for your payment products.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    def to_request_parameters(self) -> List[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.locale is not None:
            result.append(RequestParam("locale", self.locale))
        if self.payment_product_id is not None:
            result.append(RequestParam("paymentProductId", str(self.payment_product_id)))
        return result
