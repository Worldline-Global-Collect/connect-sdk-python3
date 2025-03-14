# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.payment_product_filters_hosted_checkout import PaymentProductFiltersHostedCheckout
from worldline.connect.sdk.v1.domain.recurring_payments_data import RecurringPaymentsData


class HostedCheckoutSpecificInput(DataObject):

    __is_recurring: Optional[bool] = None
    __locale: Optional[str] = None
    __payment_product_filters: Optional[PaymentProductFiltersHostedCheckout] = None
    __recurring_payments_data: Optional[RecurringPaymentsData] = None
    __return_cancel_state: Optional[bool] = None
    __return_url: Optional[str] = None
    __show_result_page: Optional[bool] = None
    __tokens: Optional[str] = None
    __validate_shopping_cart: Optional[bool] = None
    __variant: Optional[str] = None

    @property
    def is_recurring(self) -> Optional[bool]:
        """
        * true - Only payment products that support recurring payments will be shown. Any transactions created will also be tagged as being a first of a recurring sequence.
        * false - Only payment products that support one-off payments will be shown.
        
        | The default value for this property is false.

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: Optional[bool]) -> None:
        self.__is_recurring = value

    @property
    def locale(self) -> Optional[str]:
        """
        | Locale to use to present the MyCheckout payment pages to the customer. Please make sure that a language pack is configured for the locale you are submitting. If you submit a locale that is not setup on your account we will use the default language pack for your account. You can easily upload additional language packs and set the default language pack in the Configuration Center.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def payment_product_filters(self) -> Optional[PaymentProductFiltersHostedCheckout]:
        """
        | Contains the payment product ids and payment product groups that will be used for manipulating the payment products available for the payment to the customer.

        Type: :class:`worldline.connect.sdk.v1.domain.payment_product_filters_hosted_checkout.PaymentProductFiltersHostedCheckout`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value: Optional[PaymentProductFiltersHostedCheckout]) -> None:
        self.__payment_product_filters = value

    @property
    def recurring_payments_data(self) -> Optional[RecurringPaymentsData]:
        """
        | The object containing reference data for the text that can be displayed on MyCheckout hosted payment page with subscription information.
        
        | Note:
        
        | The data in this object is only meant for displaying recurring payments-related data on your checkout page.
        | You still need to submit all the recurring payment-related data in the corresponding payment product-specific input. (example: cardPaymentMethodSpecificInput.recurring and cardPaymentMethodSpecificInput.isRecurring)

        Type: :class:`worldline.connect.sdk.v1.domain.recurring_payments_data.RecurringPaymentsData`
        """
        return self.__recurring_payments_data

    @recurring_payments_data.setter
    def recurring_payments_data(self, value: Optional[RecurringPaymentsData]) -> None:
        self.__recurring_payments_data = value

    @property
    def return_cancel_state(self) -> Optional[bool]:
        """
        | This flag affects the status of a Hosted Checkout when a customer presses the cancel button and is returned to you as a result.
        | If set to true, then the status will be CANCELLED_BY_CONSUMER. If set to false, then the status will be IN_PROGRESS.
        | The default value is false. This flag was added to introduce the additional CANCELLED_BY_CONSUMER state as a non-breaking change.

        Type: bool
        """
        return self.__return_cancel_state

    @return_cancel_state.setter
    def return_cancel_state(self, value: Optional[bool]) -> None:
        self.__return_cancel_state = value

    @property
    def return_url(self) -> Optional[str]:
        """
        | The URL that the customer is redirect to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process.
        | Note: The provided URL should be absolute and contain the https:// protocol. IP addresses are not supported, neither localhost. For use on mobile devices a custom protocol can be used in the form of *protocol*://. This protocol must be registered on the device first.
        | URLs without a protocol will be rejected.

        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value: Optional[str]) -> None:
        self.__return_url = value

    @property
    def show_result_page(self) -> Optional[bool]:
        """
        * true - MyCheckout will show a result page to the customer when applicable. Default.
        * false - MyCheckout will redirect the customer back to the provided returnUrl when this is possible.
        
        | The default value for this property is true.

        Type: bool
        """
        return self.__show_result_page

    @show_result_page.setter
    def show_result_page(self, value: Optional[bool]) -> None:
        self.__show_result_page = value

    @property
    def tokens(self) -> Optional[str]:
        """
        | String containing comma separated tokens (no spaces) associated with the customer of this hosted checkout. Valid tokens will be used to present the customer the option to re-use previously used payment details. This means the customer for instance does not have to re-enter their card details again, which a big plus when the customer is using their mobile phone to complete the checkout.

        Type: str
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: Optional[str]) -> None:
        self.__tokens = value

    @property
    def validate_shopping_cart(self) -> Optional[bool]:
        """
        | By default, validation is done for all the information required to display the shopping cart. Set this value to false if you would like to turn that feature off for a hosted checkout on the Ogone Payment Platform, in which case the rendering of the shopping cart will be skipped if any required information is missing. Use this when you want fraud-checks to be performed on the shopping cart, but do not want to suply all data needed for displaying it in the hosted checkout. The default value for this property is true.

        Type: bool
        """
        return self.__validate_shopping_cart

    @validate_shopping_cart.setter
    def validate_shopping_cart(self, value: Optional[bool]) -> None:
        self.__validate_shopping_cart = value

    @property
    def variant(self) -> Optional[str]:
        """
        | Using the Configuration Center it is possible to create multiple variations of your MyCheckout payment pages. By specifying a specific variant you can force the use of another variant then the default. This allows you to test out the effect of certain changes to your MyCheckout payment pages in a controlled manner. Please note that you need to specify the ID of the variant.

        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value: Optional[str]) -> None:
        self.__variant = value

    def to_dictionary(self) -> dict:
        dictionary = super(HostedCheckoutSpecificInput, self).to_dictionary()
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.payment_product_filters is not None:
            dictionary['paymentProductFilters'] = self.payment_product_filters.to_dictionary()
        if self.recurring_payments_data is not None:
            dictionary['recurringPaymentsData'] = self.recurring_payments_data.to_dictionary()
        if self.return_cancel_state is not None:
            dictionary['returnCancelState'] = self.return_cancel_state
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        if self.show_result_page is not None:
            dictionary['showResultPage'] = self.show_result_page
        if self.tokens is not None:
            dictionary['tokens'] = self.tokens
        if self.validate_shopping_cart is not None:
            dictionary['validateShoppingCart'] = self.validate_shopping_cart
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'HostedCheckoutSpecificInput':
        super(HostedCheckoutSpecificInput, self).from_dictionary(dictionary)
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'paymentProductFilters' in dictionary:
            if not isinstance(dictionary['paymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductFilters']))
            value = PaymentProductFiltersHostedCheckout()
            self.payment_product_filters = value.from_dictionary(dictionary['paymentProductFilters'])
        if 'recurringPaymentsData' in dictionary:
            if not isinstance(dictionary['recurringPaymentsData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurringPaymentsData']))
            value = RecurringPaymentsData()
            self.recurring_payments_data = value.from_dictionary(dictionary['recurringPaymentsData'])
        if 'returnCancelState' in dictionary:
            self.return_cancel_state = dictionary['returnCancelState']
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'showResultPage' in dictionary:
            self.show_result_page = dictionary['showResultPage']
        if 'tokens' in dictionary:
            self.tokens = dictionary['tokens']
        if 'validateShoppingCart' in dictionary:
            self.validate_shopping_cart = dictionary['validateShoppingCart']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self
