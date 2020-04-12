import unittest

from utils.ACBirdCommand import ACBirdCommand


class TestVerifyNetwork(unittest.TestCase):

    def test_valid_ipv4(self):
        assert ACBirdCommand._verify_ip_network("1.1.1.1") == "1.1.1.1/32"
        assert ACBirdCommand._verify_ip_network("9.9.9.9") == "9.9.9.9/32"
        assert ACBirdCommand._verify_ip_network("21.32.21.21") == "21.32.21.21/32"
        assert ACBirdCommand._verify_ip_network("21.32.21.0/24") == "21.32.21.0/24"
        assert ACBirdCommand._verify_ip_network("8.2.0.0/16") == "8.2.0.0/16"

    def test_valid_ipv6(self):
        assert ACBirdCommand._verify_ip_network("2222::") == "2222::"
        assert ACBirdCommand._verify_ip_network("3333:1::2") == "3333:1::2/128"
        assert ACBirdCommand._verify_ip_network("2222::/64") == "2222::/64"
        assert ACBirdCommand._verify_ip_network("2345:1::/32") == "2345:1::/32"

    def test_nott_valid(self):
        assert ACBirdCommand._verify_ip_network("alex") is None
        assert ACBirdCommand._verify_ip_network("1234") is None
        assert ACBirdCommand._verify_ip_network(None) is None
        assert ACBirdCommand._verify_ip_network("") is None
        assert ACBirdCommand._verify_ip_network("12.287.444.23") is None


class TestIsProtocol(unittest.TestCase):

    def test_valid(self):
        assert ACBirdCommand._is_valid_protocol("protocol_name") is not None
        assert ACBirdCommand._is_valid_protocol("protocol") is not None
        assert ACBirdCommand._is_valid_protocol("protocol12_name") is not None
        assert ACBirdCommand._is_valid_protocol("PRotocol_name12") is not None
        assert ACBirdCommand._is_valid_protocol("ipv4_name12") is not None

    def test_not_valid(self):
        assert ACBirdCommand._is_valid_protocol("protocol-name") is None
        assert ACBirdCommand._is_valid_protocol("protocol.name") is None
        assert ACBirdCommand._is_valid_protocol("protocol]name") is None
        assert ACBirdCommand._is_valid_protocol("protocol/name") is None
        assert ACBirdCommand._is_valid_protocol(None) is None
        assert ACBirdCommand._is_valid_protocol("protocol name") is None


class TestIsASN(unittest.TestCase):

    def test_valid(self):
        assert ACBirdCommand._is_valid_asn("1") is True
        assert ACBirdCommand._is_valid_asn("666") is True
        assert ACBirdCommand._is_valid_asn("65535") is True
        assert ACBirdCommand._is_valid_asn("420000000") is True
        assert ACBirdCommand._is_valid_asn("35085") is True

    def test_not_valid(self):
        assert ACBirdCommand._is_valid_asn("0") is False
        assert ACBirdCommand._is_valid_asn("alex") is False
        assert ACBirdCommand._is_valid_asn("334a") is False
        assert ACBirdCommand._is_valid_asn("33 33") is False
        assert ACBirdCommand._is_valid_asn("666666666666") is False


class TestIsCommunity(unittest.TestCase):

    def test_valid(self):
        assert ACBirdCommand._is_valid_community("(655:666)") is True
        assert ACBirdCommand._is_valid_community("(0:65535)") is True
        assert ACBirdCommand._is_valid_community("(0:0)") is True
        assert ACBirdCommand._is_valid_community("(1:1)") is True
        assert ACBirdCommand._is_valid_community("(65535:0)") is True

    def test_not_valid(self):
        assert ACBirdCommand._is_valid_community("(65536:0)") is False
        assert ACBirdCommand._is_valid_community("(1:a)") is False
        assert ACBirdCommand._is_valid_community("1:2") is False
        assert ACBirdCommand._is_valid_community("(1 1)") is False
        assert ACBirdCommand._is_valid_community("666666666666") is False


class TestIsLargeCommunity(unittest.TestCase):

    def test_valid(self):
        assert ACBirdCommand._is_valid_large_community("(655:666:123)") is True
        assert ACBirdCommand._is_valid_large_community("(0:65535:0)") is True
        assert ACBirdCommand._is_valid_large_community("(5666666:8876363:987712)") is True
        assert ACBirdCommand._is_valid_large_community("(1:2:3)") is True
        assert ACBirdCommand._is_valid_large_community("(4653:0:4294967295)") is True

    def test_not_valid(self):
        assert ACBirdCommand._is_valid_large_community("(4653:0:4294967296)") is False
        assert ACBirdCommand._is_valid_large_community("(1:a:a)") is False
        assert ACBirdCommand._is_valid_large_community("1:2:1") is False
        assert ACBirdCommand._is_valid_large_community("(1 1 2)") is False
        assert ACBirdCommand._is_valid_large_community("666666666666") is False