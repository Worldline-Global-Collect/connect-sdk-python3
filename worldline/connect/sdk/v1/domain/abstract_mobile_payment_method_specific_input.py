# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.v1.domain.abstract_payment_method_specific_input import AbstractPaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.card_recurrence_details import CardRecurrenceDetails


class AbstractMobilePaymentMethodSpecificInput(AbstractPaymentMethodSpecificInput):

    __authorization_mode: Optional[str] = None
    __customer_reference: Optional[str] = None
    __initial_scheme_transaction_id: Optional[str] = None
    __recurring: Optional[CardRecurrenceDetails] = None
    __requires_approval: Optional[bool] = None
    __skip_fraud_service: Optional[bool] = None
    __token: Optional[str] = None
    __tokenize: Optional[bool] = None
    __unscheduled_card_on_file_requestor: Optional[str] = None
    __unscheduled_card_on_file_sequence_indicator: Optional[str] = None

    @property
    def authorization_mode(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value: Optional[str]) -> None:
        self.__authorization_mode = value

    @property
    def customer_reference(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__customer_reference

    @customer_reference.setter
    def customer_reference(self, value: Optional[str]) -> None:
        self.__customer_reference = value

    @property
    def initial_scheme_transaction_id(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__initial_scheme_transaction_id

    @initial_scheme_transaction_id.setter
    def initial_scheme_transaction_id(self, value: Optional[str]) -> None:
        self.__initial_scheme_transaction_id = value

    @property
    def recurring(self) -> Optional[CardRecurrenceDetails]:
        """
        Type: :class:`worldline.connect.sdk.v1.domain.card_recurrence_details.CardRecurrenceDetails`
        """
        return self.__recurring

    @recurring.setter
    def recurring(self, value: Optional[CardRecurrenceDetails]) -> None:
        self.__recurring = value

    @property
    def requires_approval(self) -> Optional[bool]:
        """
        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value: Optional[bool]) -> None:
        self.__requires_approval = value

    @property
    def skip_fraud_service(self) -> Optional[bool]:
        """
        Type: bool
        """
        return self.__skip_fraud_service

    @skip_fraud_service.setter
    def skip_fraud_service(self, value: Optional[bool]) -> None:
        self.__skip_fraud_service = value

    @property
    def token(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    @property
    def tokenize(self) -> Optional[bool]:
        """
        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value: Optional[bool]) -> None:
        self.__tokenize = value

    @property
    def unscheduled_card_on_file_requestor(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__unscheduled_card_on_file_requestor

    @unscheduled_card_on_file_requestor.setter
    def unscheduled_card_on_file_requestor(self, value: Optional[str]) -> None:
        self.__unscheduled_card_on_file_requestor = value

    @property
    def unscheduled_card_on_file_sequence_indicator(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__unscheduled_card_on_file_sequence_indicator

    @unscheduled_card_on_file_sequence_indicator.setter
    def unscheduled_card_on_file_sequence_indicator(self, value: Optional[str]) -> None:
        self.__unscheduled_card_on_file_sequence_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super(AbstractMobilePaymentMethodSpecificInput, self).to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.customer_reference is not None:
            dictionary['customerReference'] = self.customer_reference
        if self.initial_scheme_transaction_id is not None:
            dictionary['initialSchemeTransactionId'] = self.initial_scheme_transaction_id
        if self.recurring is not None:
            dictionary['recurring'] = self.recurring.to_dictionary()
        if self.requires_approval is not None:
            dictionary['requiresApproval'] = self.requires_approval
        if self.skip_fraud_service is not None:
            dictionary['skipFraudService'] = self.skip_fraud_service
        if self.token is not None:
            dictionary['token'] = self.token
        if self.tokenize is not None:
            dictionary['tokenize'] = self.tokenize
        if self.unscheduled_card_on_file_requestor is not None:
            dictionary['unscheduledCardOnFileRequestor'] = self.unscheduled_card_on_file_requestor
        if self.unscheduled_card_on_file_sequence_indicator is not None:
            dictionary['unscheduledCardOnFileSequenceIndicator'] = self.unscheduled_card_on_file_sequence_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AbstractMobilePaymentMethodSpecificInput':
        super(AbstractMobilePaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'customerReference' in dictionary:
            self.customer_reference = dictionary['customerReference']
        if 'initialSchemeTransactionId' in dictionary:
            self.initial_scheme_transaction_id = dictionary['initialSchemeTransactionId']
        if 'recurring' in dictionary:
            if not isinstance(dictionary['recurring'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurring']))
            value = CardRecurrenceDetails()
            self.recurring = value.from_dictionary(dictionary['recurring'])
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        if 'skipFraudService' in dictionary:
            self.skip_fraud_service = dictionary['skipFraudService']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        if 'unscheduledCardOnFileRequestor' in dictionary:
            self.unscheduled_card_on_file_requestor = dictionary['unscheduledCardOnFileRequestor']
        if 'unscheduledCardOnFileSequenceIndicator' in dictionary:
            self.unscheduled_card_on_file_sequence_indicator = dictionary['unscheduledCardOnFileSequenceIndicator']
        return self
