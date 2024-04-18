# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class MicrosoftFraudResults(DataObject):

    __clause_name: Optional[str] = None
    __device_country_code: Optional[str] = None
    __device_id: Optional[str] = None
    __fraud_score: Optional[int] = None
    __policy_applied: Optional[str] = None
    __true_ip_address: Optional[str] = None
    __user_device_type: Optional[str] = None

    @property
    def clause_name(self) -> Optional[str]:
        """
        | Name of the clause within the applied policy that was triggered during the evaluation of this transaction.

        Type: str
        """
        return self.__clause_name

    @clause_name.setter
    def clause_name(self, value: Optional[str]) -> None:
        self.__clause_name = value

    @property
    def device_country_code(self) -> Optional[str]:
        """
        | The country of the customer determined by Microsoft Device Fingerprinting.

        Type: str
        """
        return self.__device_country_code

    @device_country_code.setter
    def device_country_code(self, value: Optional[str]) -> None:
        self.__device_country_code = value

    @property
    def device_id(self) -> Optional[str]:
        """
        | This is the device fingerprint value. Based on the amount of data that the device fingerprint collector script was able to collect, this will be a proxy ID for the device used by the customer. 

        Type: str
        """
        return self.__device_id

    @device_id.setter
    def device_id(self, value: Optional[str]) -> None:
        self.__device_id = value

    @property
    def fraud_score(self) -> Optional[int]:
        """
        | Result of the Microsoft Fraud Protection check. This contains the normalized fraud score from a scale of 0 to 100. A higher score indicates an increased risk of fraud.

        Type: int
        """
        return self.__fraud_score

    @fraud_score.setter
    def fraud_score(self, value: Optional[int]) -> None:
        self.__fraud_score = value

    @property
    def policy_applied(self) -> Optional[str]:
        """
        | Name of the policy that was applied on during the evaluation of this transaction.

        Type: str
        """
        return self.__policy_applied

    @policy_applied.setter
    def policy_applied(self, value: Optional[str]) -> None:
        self.__policy_applied = value

    @property
    def true_ip_address(self) -> Optional[str]:
        """
        | The true IP address as determined by Microsoft Device Fingerprinting.

        Type: str
        """
        return self.__true_ip_address

    @true_ip_address.setter
    def true_ip_address(self, value: Optional[str]) -> None:
        self.__true_ip_address = value

    @property
    def user_device_type(self) -> Optional[str]:
        """
        | The type of device used by the customer.

        Type: str
        """
        return self.__user_device_type

    @user_device_type.setter
    def user_device_type(self, value: Optional[str]) -> None:
        self.__user_device_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(MicrosoftFraudResults, self).to_dictionary()
        if self.clause_name is not None:
            dictionary['clauseName'] = self.clause_name
        if self.device_country_code is not None:
            dictionary['deviceCountryCode'] = self.device_country_code
        if self.device_id is not None:
            dictionary['deviceId'] = self.device_id
        if self.fraud_score is not None:
            dictionary['fraudScore'] = self.fraud_score
        if self.policy_applied is not None:
            dictionary['policyApplied'] = self.policy_applied
        if self.true_ip_address is not None:
            dictionary['trueIpAddress'] = self.true_ip_address
        if self.user_device_type is not None:
            dictionary['userDeviceType'] = self.user_device_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MicrosoftFraudResults':
        super(MicrosoftFraudResults, self).from_dictionary(dictionary)
        if 'clauseName' in dictionary:
            self.clause_name = dictionary['clauseName']
        if 'deviceCountryCode' in dictionary:
            self.device_country_code = dictionary['deviceCountryCode']
        if 'deviceId' in dictionary:
            self.device_id = dictionary['deviceId']
        if 'fraudScore' in dictionary:
            self.fraud_score = dictionary['fraudScore']
        if 'policyApplied' in dictionary:
            self.policy_applied = dictionary['policyApplied']
        if 'trueIpAddress' in dictionary:
            self.true_ip_address = dictionary['trueIpAddress']
        if 'userDeviceType' in dictionary:
            self.user_device_type = dictionary['userDeviceType']
        return self
