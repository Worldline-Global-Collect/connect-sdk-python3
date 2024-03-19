#
# This file was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Any, List, Optional

from .api_exception import ApiException
from .authorization_exception import AuthorizationException
from .declined_payment_exception import DeclinedPaymentException
from .declined_payout_exception import DeclinedPayoutException
from .declined_refund_exception import DeclinedRefundException
from .idempotence_exception import IdempotenceException
from .platform_exception import PlatformException
from .reference_exception import ReferenceException
from .validation_exception import ValidationException
from worldline.connect.sdk.call_context import CallContext
from worldline.connect.sdk.v1.domain.api_error import APIError
from worldline.connect.sdk.v1.domain.error_response import ErrorResponse
from worldline.connect.sdk.v1.domain.payment_error_response import PaymentErrorResponse
from worldline.connect.sdk.v1.domain.payout_error_response import PayoutErrorResponse
from worldline.connect.sdk.v1.domain.refund_error_response import RefundErrorResponse


def create_exception(status_code: int, body: str, error_object: Any, context: Optional[CallContext]) -> Exception:
    """Return a raisable api-exception based on the error object given"""
    def create_exception_from_errors(error_id: Optional[str], errors: Optional[List[APIError]]) -> Exception:
        if is_idempotence_error(errors):
            return IdempotenceException(context.idempotence_key, context.idempotence_request_timestamp,
                                        status_code, body, error_id, errors)
        # get error based on status code, defaulting to ApiException
        return ERROR_MAP.get(status_code, ApiException)(status_code, body, error_id, errors)

    def is_idempotence_error(errors: List[APIError]) -> bool:
        return status_code == 409 \
            and context is not None \
            and context.idempotence_key is not None \
            and len(errors) == 1 \
            and errors[0].code

    if isinstance(error_object, PaymentErrorResponse):
        if error_object.payment_result is not None:
            return DeclinedPaymentException(status_code=status_code,
                                            response_body=body,
                                            errors=error_object)
        return create_exception_from_errors(error_object.error_id, error_object.errors)
    if isinstance(error_object, PayoutErrorResponse):
        if error_object.payout_result is not None:
            return DeclinedPayoutException(status_code=status_code,
                                           response_body=body,
                                           errors=error_object)
        return create_exception_from_errors(error_object.error_id, error_object.errors)
    if isinstance(error_object, RefundErrorResponse):
        if error_object.refund_result is not None:
            return DeclinedRefundException(status_code=status_code,
                                           response_body=body,
                                           errors=error_object)
        return create_exception_from_errors(error_object.error_id, error_object.errors)
    if not isinstance(error_object, ErrorResponse):
        raise ValueError("Unsupported error object encountered: {}".format(error_object.__class__.__name__))

    return create_exception_from_errors(error_object.error_id, error_object.errors)


ERROR_MAP = {
    400: ValidationException,
    403: AuthorizationException,
    404: ReferenceException,
    409: ReferenceException,  # idempotence has already been tested
    410: ReferenceException,
    500: PlatformException,
    502: PlatformException,
}
