# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.v1.domain.key_value_pair import KeyValuePair


class AccountOnFileAttribute(KeyValuePair):

    __must_write_reason: Optional[str] = None
    __status: Optional[str] = None

    @property
    def must_write_reason(self) -> Optional[str]:
        """
        | The reason why the status is MUST_WRITE. Currently only "IN_THE_PAST" is possible as value (for expiry date), but this can be extended with new values in the future.

        Type: str
        """
        return self.__must_write_reason

    @must_write_reason.setter
    def must_write_reason(self, value: Optional[str]) -> None:
        self.__must_write_reason = value

    @property
    def status(self) -> Optional[str]:
        """
        | Possible values:
        
        * READ_ONLY - attribute cannot be updated and should be presented in that way to the user
        * CAN_WRITE - attribute can be updated and should be presented as an editable field, for example an expiration date that will expire very soon
        * MUST_WRITE - attribute should be updated and must be presented as an editable field, for example an expiration date that has already expired
        
        | Any updated values that are entered for CAN_WRITE or MUST_WRITE will be used to update the values stored in the token.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    def to_dictionary(self) -> dict:
        dictionary = super(AccountOnFileAttribute, self).to_dictionary()
        if self.must_write_reason is not None:
            dictionary['mustWriteReason'] = self.must_write_reason
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AccountOnFileAttribute':
        super(AccountOnFileAttribute, self).from_dictionary(dictionary)
        if 'mustWriteReason' in dictionary:
            self.must_write_reason = dictionary['mustWriteReason']
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self
