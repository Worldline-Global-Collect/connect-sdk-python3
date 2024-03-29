import unittest

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID

from worldline.connect.sdk.v1.domain.address import Address
from worldline.connect.sdk.v1.domain.card_without_cvv import CardWithoutCvv
from worldline.connect.sdk.v1.domain.create_token_request import CreateTokenRequest
from worldline.connect.sdk.v1.domain.customer_token import CustomerToken
from worldline.connect.sdk.v1.domain.token_card import TokenCard
from worldline.connect.sdk.v1.domain.token_card_data import TokenCardData
from worldline.connect.sdk.v1.merchant.tokens.delete_token_params import DeleteTokenParams


class TokenTest(unittest.TestCase):
    def test_token(self):
        billing_address = Address()
        billing_address.country_code = "NL"
        customer = CustomerToken()
        customer.billing_address = billing_address
        card_without_ccv = CardWithoutCvv()
        card_without_ccv.cardholder_name = "Jan"
        card_without_ccv.issue_number = "12"
        card_without_ccv.card_number = "4567350000427977"
        card_without_ccv.expiry_date = "1225"
        card_data = TokenCardData()
        card_data.card_without_cvv = card_without_ccv
        card = TokenCard()
        card.customer = customer
        card.data = card_data
        create_token_request = CreateTokenRequest()
        create_token_request.payment_product_id = 1
        create_token_request.card = card

        with init_utils.create_client() as client:
            token_response = client.v1().merchant(MERCHANT_ID).tokens().create(create_token_request)

            self.assertIsNotNone(token_response.token)

            client.v1().merchant(MERCHANT_ID).tokens().delete(token_response.token, DeleteTokenParams())


if __name__ == '__main__':
    unittest.main()
