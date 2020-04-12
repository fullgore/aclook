import unittest

from tests.data.protocols import *
from utils.ACBirdParser import ACBirdParser


class TestBGPProtocol(unittest.TestCase):

    def test_valid_bgp_protocol(self):
        assert ACBirdParser.parse_bgp_protocol(protocol_a) == result_protocol_a
        assert ACBirdParser.parse_bgp_protocol(protocol_b) == result_protocol_b
        assert ACBirdParser.parse_bgp_protocol(protocol_c) == result_protocol_c
        assert ACBirdParser.parse_protocol(protocol_a) == result_protocol_a
        assert ACBirdParser.parse_protocol(protocol_b) == result_protocol_b
        assert ACBirdParser.parse_protocol(protocol_c) == result_protocol_c

    def test_invalid_bgp_protocol(self):
        assert ACBirdParser.parse_bgp_protocol(protocol_d) == result_protocol_d
        assert ACBirdParser.parse_bgp_protocol(protocol_e) == result_protocol_e
        assert ACBirdParser.parse_protocol(protocol_d) is None
        assert ACBirdParser.parse_protocol(protocol_e) is None

    def test_empty_bgp_protocol(self):
        assert ACBirdParser.parse_bgp_protocol("") is None
        assert ACBirdParser.parse_bgp_protocol(None) is None
        assert ACBirdParser.parse_protocol("") is None
        assert ACBirdParser.parse_protocol(None) is None


class TestRPKIProtocol(unittest.TestCase):

    def test_valid_rpki_protocol(self):
        assert ACBirdParser.parse_rpki_protocol(protocol_f) == result_protocol_f
        assert ACBirdParser.parse_rpki_protocol(protocol_g) == result_protocol_g
        assert ACBirdParser.parse_protocol(protocol_f) == result_protocol_f
        assert ACBirdParser.parse_protocol(protocol_g) == result_protocol_g

    def test_invalid_rpki_protocol(self):
        assert ACBirdParser.parse_rpki_protocol(protocol_h) == result_protocol_h
        assert ACBirdParser.parse_rpki_protocol(protocol_i) == result_protocol_i
        assert ACBirdParser.parse_protocol(protocol_h) is None
        assert ACBirdParser.parse_protocol(protocol_i) is None

    def test_empty_rpki_protocol(self):
        assert ACBirdParser.parse_rpki_protocol("") is None
        assert ACBirdParser.parse_rpki_protocol(None) is None