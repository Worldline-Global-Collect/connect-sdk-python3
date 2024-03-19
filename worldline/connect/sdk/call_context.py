from typing import Optional


class CallContext(object):
    """
    A call context can be used to send extra information with a request, and to receive extra information from a response.
    
    Please note that this class is not thread-safe. Each request should get its own call context instance.
    """
    __idempotence_key: Optional[str] = None
    __idempotence_request_timestamp: Optional[int] = None

    def __init__(self, idempotence_key: Optional[str] = None):
        """
        Sets the idempotence key to use for the next request for which this call context is used.
        """
        self.__idempotence_key = idempotence_key

    @property
    def idempotence_key(self) -> Optional[str]:
        """
        :return: The idempotence key.
        """
        return self.__idempotence_key

    @property
    def idempotence_request_timestamp(self) -> Optional[int]:
        """
        :return: The idempotence request timestamp from the response to the last
         request for which this call context was used, or None if no idempotence
         request timestamp was present.
        """
        return self.__idempotence_request_timestamp

    @idempotence_request_timestamp.setter
    def idempotence_request_timestamp(self, idempotence_request_timestamp: int) -> None:
        """
        Sets the idempotence request timestamp.
        This method should only be called by Communicator objects based on the
        response to the request for which this call context was used.
        """
        self.__idempotence_request_timestamp = idempotence_request_timestamp
