# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.v1.domain.abstract_card_payment_method_specific_input import AbstractCardPaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.card import Card
from worldline.connect.sdk.v1.domain.external_cardholder_authentication_data import ExternalCardholderAuthenticationData
from worldline.connect.sdk.v1.domain.scheme_token_data import SchemeTokenData
from worldline.connect.sdk.v1.domain.three_d_secure import ThreeDSecure


class CardPaymentMethodSpecificInput(AbstractCardPaymentMethodSpecificInput):

    __card: Optional[Card] = None
    __external_cardholder_authentication_data: Optional[ExternalCardholderAuthenticationData] = None
    __is_recurring: Optional[bool] = None
    __merchant_initiated_reason_indicator: Optional[str] = None
    __network_token_data: Optional[SchemeTokenData] = None
    __return_url: Optional[str] = None
    __three_d_secure: Optional[ThreeDSecure] = None

    @property
    def card(self) -> Optional[Card]:
        """
        | Object containing card details. The card details will be ignored in case the property networkTokenData is present.

        Type: :class:`worldline.connect.sdk.v1.domain.card.Card`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[Card]) -> None:
        self.__card = value

    @property
    def external_cardholder_authentication_data(self) -> Optional[ExternalCardholderAuthenticationData]:
        """
        | Object containing 3D secure details.

        Type: :class:`worldline.connect.sdk.v1.domain.external_cardholder_authentication_data.ExternalCardholderAuthenticationData`

        Deprecated; Use threeDSecure.externalCardholderAuthenticationData instead
        """
        return self.__external_cardholder_authentication_data

    @external_cardholder_authentication_data.setter
    def external_cardholder_authentication_data(self, value: Optional[ExternalCardholderAuthenticationData]) -> None:
        self.__external_cardholder_authentication_data = value

    @property
    def is_recurring(self) -> Optional[bool]:
        """
        | Indicates if this transaction is of a one-off or a recurring type
        
        * true - This is recurring
        * false - This is one-off

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: Optional[bool]) -> None:
        self.__is_recurring = value

    @property
    def merchant_initiated_reason_indicator(self) -> Optional[str]:
        """
        | Indicates reason behind the merchant initiated transaction. These are industry specific.
        | Possible values:
        
        * delayedCharges - Delayed charges are performed to process a supplemental account charge after original services have been rendered and respective payment has been processed. This is typically used in hotel, cruise lines and vehicle rental environments to perform a supplemental payment after the original services are rendered.
        * noShow - Cardholders can use their cards to make a guaranteed reservation with certain merchant segments. A guaranteed reservation ensures that the reservation will be honored and allows a merchant to perform a No Show transaction to charge the cardholder a penalty according to the merchant’s cancellation policy. For merchants that accept token-based payment credentials to guarantee a reservation, it is necessary to perform a customer initiated (Account Verification) at the time of reservation to be able perform a No Show transaction later.

        Type: str
        """
        return self.__merchant_initiated_reason_indicator

    @merchant_initiated_reason_indicator.setter
    def merchant_initiated_reason_indicator(self, value: Optional[str]) -> None:
        self.__merchant_initiated_reason_indicator = value

    @property
    def network_token_data(self) -> Optional[SchemeTokenData]:
        """
        | Object holding data that describes a network token

        Type: :class:`worldline.connect.sdk.v1.domain.scheme_token_data.SchemeTokenData`
        """
        return self.__network_token_data

    @network_token_data.setter
    def network_token_data(self, value: Optional[SchemeTokenData]) -> None:
        self.__network_token_data = value

    @property
    def return_url(self) -> Optional[str]:
        """
        | The URL that the customer is redirect to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process.
        | Note: The provided URL should be absolute and contain the https:// protocol. IP addresses are not supported, neither localhost. For use on mobile devices a custom protocol can be used in the form of *protocol*://. This protocol must be registered on the device first.
        | URLs without a protocol will be rejected.

        Type: str

        Deprecated; Use threeDSecure.redirectionData.returnUrl instead
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value: Optional[str]) -> None:
        self.__return_url = value

    @property
    def three_d_secure(self) -> Optional[ThreeDSecure]:
        """
        | Object containing specific data regarding 3-D Secure

        Type: :class:`worldline.connect.sdk.v1.domain.three_d_secure.ThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value: Optional[ThreeDSecure]) -> None:
        self.__three_d_secure = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardPaymentMethodSpecificInput, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.external_cardholder_authentication_data is not None:
            dictionary['externalCardholderAuthenticationData'] = self.external_cardholder_authentication_data.to_dictionary()
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.merchant_initiated_reason_indicator is not None:
            dictionary['merchantInitiatedReasonIndicator'] = self.merchant_initiated_reason_indicator
        if self.network_token_data is not None:
            dictionary['networkTokenData'] = self.network_token_data.to_dictionary()
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentMethodSpecificInput':
        super(CardPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        if 'externalCardholderAuthenticationData' in dictionary:
            if not isinstance(dictionary['externalCardholderAuthenticationData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['externalCardholderAuthenticationData']))
            value = ExternalCardholderAuthenticationData()
            self.external_cardholder_authentication_data = value.from_dictionary(dictionary['externalCardholderAuthenticationData'])
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'merchantInitiatedReasonIndicator' in dictionary:
            self.merchant_initiated_reason_indicator = dictionary['merchantInitiatedReasonIndicator']
        if 'networkTokenData' in dictionary:
            if not isinstance(dictionary['networkTokenData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['networkTokenData']))
            value = SchemeTokenData()
            self.network_token_data = value.from_dictionary(dictionary['networkTokenData'])
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = ThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self
