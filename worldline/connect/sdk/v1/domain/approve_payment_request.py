# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.approve_payment_non_sepa_direct_debit_payment_method_specific_input import ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.approve_payment_sepa_direct_debit_payment_method_specific_input import ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.order_approve_payment import OrderApprovePayment


class ApprovePaymentRequest(DataObject):

    __amount: Optional[int] = None
    __direct_debit_payment_method_specific_input: Optional[ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput] = None
    __order: Optional[OrderApprovePayment] = None
    __sepa_direct_debit_payment_method_specific_input: Optional[ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput] = None

    @property
    def amount(self) -> Optional[int]:
        """
        | In case you want to approve the capture of a different lower amount you can specify this here (specified in cents, where single digit currencies are presumed to have 2 digits)

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: Optional[int]) -> None:
        self.__amount = value

    @property
    def direct_debit_payment_method_specific_input(self) -> Optional[ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput]:
        """
        | Object that holds non-SEPA Direct Debit specific input data

        Type: :class:`worldline.connect.sdk.v1.domain.approve_payment_non_sepa_direct_debit_payment_method_specific_input.ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput`
        """
        return self.__direct_debit_payment_method_specific_input

    @direct_debit_payment_method_specific_input.setter
    def direct_debit_payment_method_specific_input(self, value: Optional[ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput]) -> None:
        self.__direct_debit_payment_method_specific_input = value

    @property
    def order(self) -> Optional[OrderApprovePayment]:
        """
        | Object that holds the order data

        Type: :class:`worldline.connect.sdk.v1.domain.order_approve_payment.OrderApprovePayment`
        """
        return self.__order

    @order.setter
    def order(self, value: Optional[OrderApprovePayment]) -> None:
        self.__order = value

    @property
    def sepa_direct_debit_payment_method_specific_input(self) -> Optional[ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput]:
        """
        | Object that holds SEPA Direct Debit specific input data

        Type: :class:`worldline.connect.sdk.v1.domain.approve_payment_sepa_direct_debit_payment_method_specific_input.ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value: Optional[ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput]) -> None:
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super(ApprovePaymentRequest, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        if self.direct_debit_payment_method_specific_input is not None:
            dictionary['directDebitPaymentMethodSpecificInput'] = self.direct_debit_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_input is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificInput'] = self.sepa_direct_debit_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ApprovePaymentRequest':
        super(ApprovePaymentRequest, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'directDebitPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['directDebitPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['directDebitPaymentMethodSpecificInput']))
            value = ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput()
            self.direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['directDebitPaymentMethodSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = OrderApprovePayment()
            self.order = value.from_dictionary(dictionary['order'])
        if 'sepaDirectDebitPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificInput']))
            value = ApprovePaymentSepaDirectDebitPaymentMethodSpecificInput()
            self.sepa_direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificInput'])
        return self
