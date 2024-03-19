import unittest

from tests.unit.comparable_param import ComparableParam

from worldline.connect.sdk.v1.merchant.productgroups.find_productgroups_params import FindProductgroupsParams
from worldline.connect.sdk.v1.merchant.products.find_products_params import FindProductsParams


class FindProductParamsTest(unittest.TestCase):
    """Tests if instances of the FindProductsParams class for products
    can be correctly converted to RequestParameter objects"""

    def test_empty_request_parameters(self):
        """Tests that the FindProductsParams object correctly functions when values are not set"""
        params = FindProductsParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the FindProductsParams object can correctly store and convert its data to RequestParameters"""
        params = FindProductsParams()
        expected = []
        params.amount = 1000
        expected.append(ComparableParam("amount", "1000"))
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))
        params.is_recurring = True
        expected.append(ComparableParam("isRecurring", "True"))
        params.locale = "nl_NL"
        expected.append(ComparableParam("locale", "nl_NL"))
        params.add_hide("fields")
        expected.append(ComparableParam("hide", "fields"))
        params.add_hide("accounts_on_file")
        expected.append(ComparableParam("hide", "accounts_on_file"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the FindProductsParams object"""
        params = FindProductsParams()
        expected = []
        params.amount = 1000
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.amount = None
        params.currency_code = None
        params.country_code = None

        request_params = params.to_request_parameters()

        self.assertCountEqual(expected, request_params)


class FindProductGroupsParamsTest(unittest.TestCase):
    """Tests if instances of the FindProductgroupsParams class for product groups
    can be correctly converted to RequestParameter objects
    """

    def test_empty_request_parameters(self):
        """Tests that the FindProductgroupsParams object correctly functions when values are not set"""
        params = FindProductgroupsParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the FindProductgroupsParams object can correctly store and convert its data to RequestParameters
        """
        params = FindProductgroupsParams()
        expected = []
        params.amount = 1000
        expected.append(ComparableParam("amount", "1000"))
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))
        params.is_recurring = True
        expected.append(ComparableParam("isRecurring", "True"))
        params.locale = "nl_NL"
        expected.append(ComparableParam("locale", "nl_NL"))
        params.add_hide("fields")
        expected.append(ComparableParam("hide", "fields"))
        params.add_hide("accounts_on_file")
        expected.append(ComparableParam("hide", "accounts_on_file"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the FindProductgroupsParams object"""
        params = FindProductgroupsParams()
        expected = []
        params.amount = 1000
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.amount = None
        params.currency_code = None
        params.country_code = None

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)


if __name__ == '__main__':
    unittest.main()
