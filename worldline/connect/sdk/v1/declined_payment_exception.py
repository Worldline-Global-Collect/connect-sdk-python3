#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from .declined_transaction_exception import DeclinedTransactionException
from worldline.connect.sdk.v1.domain.create_payment_result import CreatePaymentResult
from worldline.connect.sdk.v1.domain.payment_error_response import PaymentErrorResponse


class DeclinedPaymentException(DeclinedTransactionException):
    """
    Represents an error response from a create payment call.
    """

    def __init__(self, status_code: int, response_body: str, errors: Optional[PaymentErrorResponse]):
        if errors is not None:
            super(DeclinedPaymentException, self).__init__(status_code, response_body, errors.error_id, errors.errors,
                                                           DeclinedPaymentException.__create_message(errors))
        else:
            super(DeclinedPaymentException, self).__init__(status_code, response_body, None, None,
                                                           DeclinedPaymentException.__create_message(errors))
        self.__errors = errors

    @staticmethod
    def __create_message(errors: Optional[PaymentErrorResponse]) -> str:
        if errors is not None and errors.payment_result is not None:
            payment = errors.payment_result.payment
        else:
            payment = None
        if payment is not None:
            return "declined payment '" + payment.id + "' with status '" + payment.status + "'"
        else:
            return "the Worldline Global Collect platform returned a declined payment response"

    @property
    def create_payment_result(self) -> Optional[CreatePaymentResult]:
        """
        :return: The result of creating a payment if available, otherwise None.
        """
        if self.__errors is None:
            return None
        else:
            return self.__errors.payment_result
