import unittest

from tests.data.nested_protocols import *
from utils.ACBirdParser import ACBirdParser


class TestNestedProtocol(unittest.TestCase):

    def test_valid_protocol_list(self):
        parsed_nested_protocol_a = ACBirdParser.parse_nested_protocols_list(protocol_a)
        assert parsed_nested_protocol_a == result_protocol_a

        parsed_nested_protocol_b = ACBirdParser.parse_nested_protocols_list(protocol_b)
        assert parsed_nested_protocol_b == result_protocol_b

        parsed_nested_protocol_c = ACBirdParser.parse_nested_protocols_list(protocol_c)
        assert parsed_nested_protocol_c == result_protocol_c

        parsed_nested_protocol_d = ACBirdParser.parse_nested_protocols_list(protocol_d)
        assert parsed_nested_protocol_d == result_protocol_d

    def test_invalid_protocol_list(self):
        assert {'protocols': []} == ACBirdParser.parse_nested_protocols_list(protocol_e)
        assert {'protocols': []} == ACBirdParser.parse_nested_protocols_list(protocol_f)

    def test_empty(self):
        assert ACBirdParser.parse_nested_protocols_list("") is None
        assert ACBirdParser.parse_nested_protocols_list(None) is None