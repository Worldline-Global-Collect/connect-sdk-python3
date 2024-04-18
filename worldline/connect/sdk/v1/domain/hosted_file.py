# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject


class HostedFile(DataObject):
    """
    | File items.
    """

    __file_name: Optional[str] = None
    __file_size: Optional[str] = None
    __file_type: Optional[str] = None
    __id: Optional[str] = None

    @property
    def file_name(self) -> Optional[str]:
        """
        | The name of the file.

        Type: str
        """
        return self.__file_name

    @file_name.setter
    def file_name(self, value: Optional[str]) -> None:
        self.__file_name = value

    @property
    def file_size(self) -> Optional[str]:
        """
        | The size of the file in bytes.

        Type: str
        """
        return self.__file_size

    @file_size.setter
    def file_size(self, value: Optional[str]) -> None:
        self.__file_size = value

    @property
    def file_type(self) -> Optional[str]:
        """
        | The type of the file.

        Type: str
        """
        return self.__file_type

    @file_type.setter
    def file_type(self, value: Optional[str]) -> None:
        self.__file_type = value

    @property
    def id(self) -> Optional[str]:
        """
        | The numeric identifier of the file.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    def to_dictionary(self) -> dict:
        dictionary = super(HostedFile, self).to_dictionary()
        if self.file_name is not None:
            dictionary['fileName'] = self.file_name
        if self.file_size is not None:
            dictionary['fileSize'] = self.file_size
        if self.file_type is not None:
            dictionary['fileType'] = self.file_type
        if self.id is not None:
            dictionary['id'] = self.id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'HostedFile':
        super(HostedFile, self).from_dictionary(dictionary)
        if 'fileName' in dictionary:
            self.file_name = dictionary['fileName']
        if 'fileSize' in dictionary:
            self.file_size = dictionary['fileSize']
        if 'fileType' in dictionary:
            self.file_type = dictionary['fileType']
        if 'id' in dictionary:
            self.id = dictionary['id']
        return self
