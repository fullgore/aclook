import unittest

from tests.data.nested_routes import *
from utils.ACBirdParser import ACBirdParser


class TestNestedRoute(unittest.TestCase):

    def test_valid_route(self):
        assert ACBirdParser.parse_nested_route_list(route_a) == result_route_a
        assert ACBirdParser.parse_nested_route_list(route_b) == result_route_b

    def test_unknown_route(self):
        assert ACBirdParser.parse_nested_route_list(route_c) == result_route_c
        assert ACBirdParser.parse_nested_route_list(route_d) == result_route_d