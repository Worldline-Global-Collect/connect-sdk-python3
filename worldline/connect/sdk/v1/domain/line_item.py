# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.line_item_invoice_data import LineItemInvoiceData
from worldline.connect.sdk.v1.domain.line_item_level3_interchange_information import LineItemLevel3InterchangeInformation
from worldline.connect.sdk.v1.domain.order_line_details import OrderLineDetails


class LineItem(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __invoice_data: Optional[LineItemInvoiceData] = None
    __level3_interchange_information: Optional[LineItemLevel3InterchangeInformation] = None
    __order_line_details: Optional[OrderLineDetails] = None

    @property
    def amount_of_money(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes
        | Note: make sure you submit the amount and currency code for each line item

        Type: :class:`worldline.connect.sdk.v1.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: Optional[AmountOfMoney]) -> None:
        self.__amount_of_money = value

    @property
    def invoice_data(self) -> Optional[LineItemInvoiceData]:
        """
        | Object containing the line items of the invoice or shopping cart. The '+' character is not allowed in this property for transactions that are processed by TechProcess Payment Platform.

        Type: :class:`worldline.connect.sdk.v1.domain.line_item_invoice_data.LineItemInvoiceData`
        """
        return self.__invoice_data

    @invoice_data.setter
    def invoice_data(self, value: Optional[LineItemInvoiceData]) -> None:
        self.__invoice_data = value

    @property
    def level3_interchange_information(self) -> Optional[LineItemLevel3InterchangeInformation]:
        """
        | Object containing additional information that when supplied can have a beneficial effect on the discountrates

        Type: :class:`worldline.connect.sdk.v1.domain.line_item_level3_interchange_information.LineItemLevel3InterchangeInformation`

        Deprecated; Use orderLineDetails instead
        """
        return self.__level3_interchange_information

    @level3_interchange_information.setter
    def level3_interchange_information(self, value: Optional[LineItemLevel3InterchangeInformation]) -> None:
        self.__level3_interchange_information = value

    @property
    def order_line_details(self) -> Optional[OrderLineDetails]:
        """
        | Object containing additional information that when supplied can have a beneficial effect on the discountrates

        Type: :class:`worldline.connect.sdk.v1.domain.order_line_details.OrderLineDetails`
        """
        return self.__order_line_details

    @order_line_details.setter
    def order_line_details(self, value: Optional[OrderLineDetails]) -> None:
        self.__order_line_details = value

    def to_dictionary(self) -> dict:
        dictionary = super(LineItem, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.invoice_data is not None:
            dictionary['invoiceData'] = self.invoice_data.to_dictionary()
        if self.level3_interchange_information is not None:
            dictionary['level3InterchangeInformation'] = self.level3_interchange_information.to_dictionary()
        if self.order_line_details is not None:
            dictionary['orderLineDetails'] = self.order_line_details.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'LineItem':
        super(LineItem, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'invoiceData' in dictionary:
            if not isinstance(dictionary['invoiceData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['invoiceData']))
            value = LineItemInvoiceData()
            self.invoice_data = value.from_dictionary(dictionary['invoiceData'])
        if 'level3InterchangeInformation' in dictionary:
            if not isinstance(dictionary['level3InterchangeInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['level3InterchangeInformation']))
            value = LineItemLevel3InterchangeInformation()
            self.level3_interchange_information = value.from_dictionary(dictionary['level3InterchangeInformation'])
        if 'orderLineDetails' in dictionary:
            if not isinstance(dictionary['orderLineDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['orderLineDetails']))
            value = OrderLineDetails()
            self.order_line_details = value.from_dictionary(dictionary['orderLineDetails'])
        return self
