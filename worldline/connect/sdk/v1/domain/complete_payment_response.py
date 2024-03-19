# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.create_payment_result import CreatePaymentResult


class CompletePaymentResponse(CreatePaymentResult):

    def to_dictionary(self) -> dict:
        dictionary = super(CompletePaymentResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CompletePaymentResponse':
        super(CompletePaymentResponse, self).from_dictionary(dictionary)
        return self
