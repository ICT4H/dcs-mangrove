
import unittest
from mangrove.transport.contract.transport_info import TransportInfo
from mangrove.transport.contract.request import Request

class TestTransport(unittest.TestCase):
    def test_should_throw_error_if_transport_is_none(self):
        with self.assertRaises(AssertionError):
            TransportInfo(transport=None, source="", destination="")

    def test_should_throw_error_if_source_is_none(self):
        with self.assertRaises(AssertionError):
            TransportInfo(transport="", source=None, destination="")

    def test_should_throw_error_if_destination_is_none(self):
        with self.assertRaises(AssertionError):
            TransportInfo(transport="", source="", destination=None)


class TestRequest(unittest.TestCase):
    def test_should_throw_error_if_transportInfo_is_none(self):
        with self.assertRaises(AssertionError):
            Request(transportInfo=None, message="")

    def test_should_throw_error_if_message_is_none(self):
        with self.assertRaises(AssertionError):
            transport = TransportInfo(transport="", source="", destination="")
            Request(transportInfo=transport, message=None)

