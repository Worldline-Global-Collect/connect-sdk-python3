# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class ClickToPaySchemeConfigurationBase(DataObject):

    __src_initiator_id: Optional[str] = None
    __srci_dpa_id: Optional[str] = None

    @property
    def src_initiator_id(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__src_initiator_id

    @src_initiator_id.setter
    def src_initiator_id(self, value: Optional[str]) -> None:
        self.__src_initiator_id = value

    @property
    def srci_dpa_id(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__srci_dpa_id

    @srci_dpa_id.setter
    def srci_dpa_id(self, value: Optional[str]) -> None:
        self.__srci_dpa_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(ClickToPaySchemeConfigurationBase, self).to_dictionary()
        if self.src_initiator_id is not None:
            dictionary['srcInitiatorId'] = self.src_initiator_id
        if self.srci_dpa_id is not None:
            dictionary['srciDpaId'] = self.srci_dpa_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ClickToPaySchemeConfigurationBase':
        super(ClickToPaySchemeConfigurationBase, self).from_dictionary(dictionary)
        if 'srcInitiatorId' in dictionary:
            self.src_initiator_id = dictionary['srcInitiatorId']
        if 'srciDpaId' in dictionary:
            self.srci_dpa_id = dictionary['srciDpaId']
        return self
