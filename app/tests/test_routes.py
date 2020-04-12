import unittest

from tests.data.routes import *
from utils.ACBirdParser import ACBirdParser


class TestRoute(unittest.TestCase):

    def test_valid_route_v4(self):
        assert ACBirdParser.parse_route_list(route_a) == result_route_a

    def test_valid_route_v6(self):
        assert ACBirdParser.parse_route_list(route_b) == result_route_b
