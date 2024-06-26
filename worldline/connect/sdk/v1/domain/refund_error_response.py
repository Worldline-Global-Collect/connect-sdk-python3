# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import List, Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.api_error import APIError
from worldline.connect.sdk.v1.domain.refund_result import RefundResult


class RefundErrorResponse(DataObject):

    __error_id: Optional[str] = None
    __errors: Optional[List[APIError]] = None
    __refund_result: Optional[RefundResult] = None

    @property
    def error_id(self) -> Optional[str]:
        """
        | Unique reference, for debugging purposes, of this error response

        Type: str
        """
        return self.__error_id

    @error_id.setter
    def error_id(self, value: Optional[str]) -> None:
        self.__error_id = value

    @property
    def errors(self) -> Optional[List[APIError]]:
        """
        | List of one or more errors

        Type: list[:class:`worldline.connect.sdk.v1.domain.api_error.APIError`]
        """
        return self.__errors

    @errors.setter
    def errors(self, value: Optional[List[APIError]]) -> None:
        self.__errors = value

    @property
    def refund_result(self) -> Optional[RefundResult]:
        """
        | Object that contains details on the created refund in case one has been created

        Type: :class:`worldline.connect.sdk.v1.domain.refund_result.RefundResult`
        """
        return self.__refund_result

    @refund_result.setter
    def refund_result(self, value: Optional[RefundResult]) -> None:
        self.__refund_result = value

    def to_dictionary(self) -> dict:
        dictionary = super(RefundErrorResponse, self).to_dictionary()
        if self.error_id is not None:
            dictionary['errorId'] = self.error_id
        if self.errors is not None:
            dictionary['errors'] = []
            for element in self.errors:
                if element is not None:
                    dictionary['errors'].append(element.to_dictionary())
        if self.refund_result is not None:
            dictionary['refundResult'] = self.refund_result.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundErrorResponse':
        super(RefundErrorResponse, self).from_dictionary(dictionary)
        if 'errorId' in dictionary:
            self.error_id = dictionary['errorId']
        if 'errors' in dictionary:
            if not isinstance(dictionary['errors'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['errors']))
            self.errors = []
            for element in dictionary['errors']:
                value = APIError()
                self.errors.append(value.from_dictionary(element))
        if 'refundResult' in dictionary:
            if not isinstance(dictionary['refundResult'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundResult']))
            value = RefundResult()
            self.refund_result = value.from_dictionary(dictionary['refundResult'])
        return self
