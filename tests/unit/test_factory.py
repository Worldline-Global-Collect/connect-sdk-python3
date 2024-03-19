import os
import unittest
import warnings

from urllib.parse import urlparse

from tests.unit.test_default_connection import DefaultConnectionTest

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.authentication.authorization_type import AuthorizationType
from worldline.connect.sdk.authentication.v1hmac_authenticator import V1HMACAuthenticator
from worldline.connect.sdk.communication.default_connection import DefaultConnection
from worldline.connect.sdk.communication.metadata_provider import MetadataProvider
from worldline.connect.sdk.json.default_marshaller import DefaultMarshaller

PROPERTIES_URI = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.ini"))
API_KEY_ID = "someKey"
SECRET_API_KEY = "someSecret"


class FactoryTest(unittest.TestCase):
    """Tests that the factory is capable of correctly creating communicators and communicator configurations"""

    def test_create_configuration(self):
        """Tests that the factory is correctly able to create a communicator configuration"""
        configuration = Factory.create_configuration(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        self.assertEqual(urlparse("https://api.preprod.connect.worldline-solutions.com"), configuration.api_endpoint)
        self.assertEqual(AuthorizationType.get_authorization("v1HMAC"), configuration.authorization_type)
        self.assertEqual(-1, configuration.connect_timeout)
        self.assertEqual(-1, configuration.socket_timeout)
        self.assertEqual(100, configuration.max_connections)
        self.assertEqual(API_KEY_ID, configuration.api_key_id)
        self.assertEqual(SECRET_API_KEY, configuration.secret_api_key)
        self.assertIsNone(configuration.proxy_configuration)

    # noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
    def test_create_communicator(self):
        """Tests that the factory is correctly able to create a communicator"""
        communicator = Factory.create_communicator_from_file(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)

        self.assertIs(communicator.marshaller, DefaultMarshaller.instance())

        connection = communicator._Communicator__connection
        self.assertIsInstance(connection, DefaultConnection)
        DefaultConnectionTest.assertConnection(self, connection, None, None, 100, None)

        authenticator = communicator._Communicator__authenticator
        self.assertIsInstance(authenticator, V1HMACAuthenticator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertEqual(API_KEY_ID, authenticator._V1HMACAuthenticator__api_key_id)
            self.assertEqual(SECRET_API_KEY, authenticator._V1HMACAuthenticator__secret_api_key)

        metadata_provider = communicator._Communicator__metadata_provider
        self.assertIsInstance(metadata_provider, MetadataProvider)
        request_headers = metadata_provider.metadata_headers
        self.assertEqual(1, len(request_headers))
        self.assertEqual("X-GCS-ServerMetaInfo", request_headers[0].name)


if __name__ == '__main__':
    unittest.main()
