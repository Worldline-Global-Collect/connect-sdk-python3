# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.customer_account_authentication import CustomerAccountAuthentication
from worldline.connect.sdk.v1.domain.customer_payment_activity import CustomerPaymentActivity
from worldline.connect.sdk.v1.domain.payment_account_on_file import PaymentAccountOnFile


class CustomerAccount(DataObject):
    """
    | Object containing data related to the account the customer has with you
    """

    __authentication: Optional[CustomerAccountAuthentication] = None
    __change_date: Optional[str] = None
    __changed_during_checkout: Optional[bool] = None
    __create_date: Optional[str] = None
    __had_suspicious_activity: Optional[bool] = None
    __has_forgotten_password: Optional[bool] = None
    __has_password: Optional[bool] = None
    __password_change_date: Optional[str] = None
    __password_changed_during_checkout: Optional[bool] = None
    __payment_account_on_file: Optional[PaymentAccountOnFile] = None
    __payment_account_on_file_type: Optional[str] = None
    __payment_activity: Optional[CustomerPaymentActivity] = None

    @property
    def authentication(self) -> Optional[CustomerAccountAuthentication]:
        """
        | Object containing data on the authentication used by the customer to access their account

        Type: :class:`worldline.connect.sdk.v1.domain.customer_account_authentication.CustomerAccountAuthentication`
        """
        return self.__authentication

    @authentication.setter
    def authentication(self, value: Optional[CustomerAccountAuthentication]) -> None:
        self.__authentication = value

    @property
    def change_date(self) -> Optional[str]:
        """
        | The last date (YYYYMMDD) on which the customer made changes to their account with you. These are changes to billing & shipping address details, new payment account (tokens), or new users(s) added.

        Type: str
        """
        return self.__change_date

    @change_date.setter
    def change_date(self, value: Optional[str]) -> None:
        self.__change_date = value

    @property
    def changed_during_checkout(self) -> Optional[bool]:
        """
        | true = the customer made changes to their account during this checkout
        
        | false = the customer didn't change anything to their account during this checkout/n
        
        | The changes ment here are changes to billing & shipping address details, new payment account (tokens), or new users(s) added.

        Type: bool
        """
        return self.__changed_during_checkout

    @changed_during_checkout.setter
    def changed_during_checkout(self, value: Optional[bool]) -> None:
        self.__changed_during_checkout = value

    @property
    def create_date(self) -> Optional[str]:
        """
        | The date (YYYYMMDD) on which the customer created their account with you

        Type: str
        """
        return self.__create_date

    @create_date.setter
    def create_date(self, value: Optional[str]) -> None:
        self.__create_date = value

    @property
    def had_suspicious_activity(self) -> Optional[bool]:
        """
        | Specifies if you have experienced suspicious activity on the account of the customer
        
        | true = you have experienced suspicious activity (including previous fraud) on the customer account used for this transaction
        
        | false = you have experienced no suspicious activity (including previous fraud) on the customer account used for this transaction

        Type: bool
        """
        return self.__had_suspicious_activity

    @had_suspicious_activity.setter
    def had_suspicious_activity(self, value: Optional[bool]) -> None:
        self.__had_suspicious_activity = value

    @property
    def has_forgotten_password(self) -> Optional[bool]:
        """
        | Specifies if the customer (initially) had forgotten their password
        
        * true - The customer has forgotten their password
        * false - The customer has not forgotten their password

        Type: bool
        """
        return self.__has_forgotten_password

    @has_forgotten_password.setter
    def has_forgotten_password(self, value: Optional[bool]) -> None:
        self.__has_forgotten_password = value

    @property
    def has_password(self) -> Optional[bool]:
        """
        | Specifies if the customer entered a password to gain access to an account registered with the you
        
        * true - The customer has used a password to gain access
        * false - The customer has not used a password to gain access

        Type: bool
        """
        return self.__has_password

    @has_password.setter
    def has_password(self, value: Optional[bool]) -> None:
        self.__has_password = value

    @property
    def password_change_date(self) -> Optional[str]:
        """
        | The last date (YYYYMMDD) on which the customer changed their password for the account used in this transaction

        Type: str
        """
        return self.__password_change_date

    @password_change_date.setter
    def password_change_date(self, value: Optional[str]) -> None:
        self.__password_change_date = value

    @property
    def password_changed_during_checkout(self) -> Optional[bool]:
        """
        | Indicates if the password of an account is changed during this checkout
        
        | true = the customer made changes to their password of the account used during this checkout
        
        | alse = the customer didn't change anything to their password of the account used during this checkout

        Type: bool
        """
        return self.__password_changed_during_checkout

    @password_changed_during_checkout.setter
    def password_changed_during_checkout(self, value: Optional[bool]) -> None:
        self.__password_changed_during_checkout = value

    @property
    def payment_account_on_file(self) -> Optional[PaymentAccountOnFile]:
        """
        | Object containing information on the payment account data on file (tokens)

        Type: :class:`worldline.connect.sdk.v1.domain.payment_account_on_file.PaymentAccountOnFile`
        """
        return self.__payment_account_on_file

    @payment_account_on_file.setter
    def payment_account_on_file(self, value: Optional[PaymentAccountOnFile]) -> None:
        self.__payment_account_on_file = value

    @property
    def payment_account_on_file_type(self) -> Optional[str]:
        """
        | Indicates the type of account. For example, for a multi-account card product. 
        
        * not-applicable = the card used doesn't support multiple card products
        * credit = the card used is a credit card
        * debit = the card used is a debit card

        Type: str
        """
        return self.__payment_account_on_file_type

    @payment_account_on_file_type.setter
    def payment_account_on_file_type(self, value: Optional[str]) -> None:
        self.__payment_account_on_file_type = value

    @property
    def payment_activity(self) -> Optional[CustomerPaymentActivity]:
        """
        | Object containing data on the purchase history of the customer with you

        Type: :class:`worldline.connect.sdk.v1.domain.customer_payment_activity.CustomerPaymentActivity`
        """
        return self.__payment_activity

    @payment_activity.setter
    def payment_activity(self, value: Optional[CustomerPaymentActivity]) -> None:
        self.__payment_activity = value

    def to_dictionary(self) -> dict:
        dictionary = super(CustomerAccount, self).to_dictionary()
        if self.authentication is not None:
            dictionary['authentication'] = self.authentication.to_dictionary()
        if self.change_date is not None:
            dictionary['changeDate'] = self.change_date
        if self.changed_during_checkout is not None:
            dictionary['changedDuringCheckout'] = self.changed_during_checkout
        if self.create_date is not None:
            dictionary['createDate'] = self.create_date
        if self.had_suspicious_activity is not None:
            dictionary['hadSuspiciousActivity'] = self.had_suspicious_activity
        if self.has_forgotten_password is not None:
            dictionary['hasForgottenPassword'] = self.has_forgotten_password
        if self.has_password is not None:
            dictionary['hasPassword'] = self.has_password
        if self.password_change_date is not None:
            dictionary['passwordChangeDate'] = self.password_change_date
        if self.password_changed_during_checkout is not None:
            dictionary['passwordChangedDuringCheckout'] = self.password_changed_during_checkout
        if self.payment_account_on_file is not None:
            dictionary['paymentAccountOnFile'] = self.payment_account_on_file.to_dictionary()
        if self.payment_account_on_file_type is not None:
            dictionary['paymentAccountOnFileType'] = self.payment_account_on_file_type
        if self.payment_activity is not None:
            dictionary['paymentActivity'] = self.payment_activity.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerAccount':
        super(CustomerAccount, self).from_dictionary(dictionary)
        if 'authentication' in dictionary:
            if not isinstance(dictionary['authentication'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['authentication']))
            value = CustomerAccountAuthentication()
            self.authentication = value.from_dictionary(dictionary['authentication'])
        if 'changeDate' in dictionary:
            self.change_date = dictionary['changeDate']
        if 'changedDuringCheckout' in dictionary:
            self.changed_during_checkout = dictionary['changedDuringCheckout']
        if 'createDate' in dictionary:
            self.create_date = dictionary['createDate']
        if 'hadSuspiciousActivity' in dictionary:
            self.had_suspicious_activity = dictionary['hadSuspiciousActivity']
        if 'hasForgottenPassword' in dictionary:
            self.has_forgotten_password = dictionary['hasForgottenPassword']
        if 'hasPassword' in dictionary:
            self.has_password = dictionary['hasPassword']
        if 'passwordChangeDate' in dictionary:
            self.password_change_date = dictionary['passwordChangeDate']
        if 'passwordChangedDuringCheckout' in dictionary:
            self.password_changed_during_checkout = dictionary['passwordChangedDuringCheckout']
        if 'paymentAccountOnFile' in dictionary:
            if not isinstance(dictionary['paymentAccountOnFile'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentAccountOnFile']))
            value = PaymentAccountOnFile()
            self.payment_account_on_file = value.from_dictionary(dictionary['paymentAccountOnFile'])
        if 'paymentAccountOnFileType' in dictionary:
            self.payment_account_on_file_type = dictionary['paymentAccountOnFileType']
        if 'paymentActivity' in dictionary:
            if not isinstance(dictionary['paymentActivity'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentActivity']))
            value = CustomerPaymentActivity()
            self.payment_activity = value.from_dictionary(dictionary['paymentActivity'])
        return self
