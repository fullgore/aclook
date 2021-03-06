
import re
import ipaddress
import logging

from utils.ACBird import ACBird
from utils.ACBirdParser import ACBirdParser

logger = logging.getLogger(__name__)


class ACBirdCommand(ACBird):

    def __init__(self, socket_file: str, **kwargs):
        super().__init__(socket_file, **kwargs)

    @staticmethod
    def _verify_ip_network(network):
        logger.debug(f"[Network] {network}")
        if not network:
            return
        regex_network = re.compile(r"^.*\d+$")
        if regex_network.search(network):
            try:
                valid_network = ipaddress.ip_network(network)
                return str(valid_network)
            except ValueError:
                return
        else:
            try:
                valid_ip = ipaddress.ip_address(network)
                return str(valid_ip)
            except ValueError:
                return

    @staticmethod
    def _is_valid_protocol(protocol_name):
        logger.debug(f"[Protocol nam] {protocol_name}")
        if not protocol_name:
            return
        regex_protocol_name = re.compile(r"^[A-Za-z_0-9]+$")
        return regex_protocol_name.search(protocol_name)

    @staticmethod
    def _is_valid_asn(asn):
        logger.debug(f"ASN: {asn}")
        if not asn:
            return False
        try:
            value = int(asn)
            return 0 < value < 4294967295
        except ValueError:
            return False

    @staticmethod
    def _is_valid_community(community):
        logger.debug(f"[Community] {community}")
        if not community:
            return False
        regex_community = re.compile(r"^\((?P<left>[0-9]{1,5}):(?P<right>[0-9]{1,5})\)$")
        match = regex_community.search(community)
        if not match:
            return False
        left, right = match.group("left", "right")
        logger.debug(f"[Community] left:{left} right:{right}")
        return 0 <= int(left) < 2**16 and 0 <= int(right) < 2**16

    @staticmethod
    def _is_valid_large_community(community):
        logger.debug(f"[Large community]: {community}")
        if not community:
            return False
        regex_community = re.compile(r"^\((?P<left>[0-9]{1,10}):(?P<middle>[0-9]{1,10}):(?P<right>[0-9]{1,10})\)$")
        match = regex_community.search(community)
        if not match:
            return False
        left, middle, right = match.group("left", "middle", "right")
        logger.debug(f"[Large community] left:{left} middle:{middle} right:{right}")
        return 0 <= int(left) < 2**32 and 0 <= int(middle) < 2**32 and 0 <= int(right) < 2**32

    @staticmethod
    def _is_valid_data(data):
        if not data:
            return False
        return data.get("valid", False)

    def _return_route_parsed_with_data(self, data, detail=False):
        if not data:
            logger.debug(f"[Data] = None")
            return f"No data"
        if not self._is_valid_data(data):
            logger.debug(f"[Data] not valid")
            return f"Return cmd is not valid ({data.get('warning')} {data.get('text')}) \
- Please contact the administrator"
        if detail:
            return ACBirdParser.parse_route_list(data.get("text"))
        else:
            return ACBirdParser.parse_nested_route_list(data.get("text"))

    def get_protocol_list(self):
        command = "show protocols"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        if not self._is_valid_data:
            return
        return ACBirdParser.parse_nested_protocols_list(data.get("text"))

    def get_protocol(self, protocol_name):
        command = f"show protocols {protocol_name}"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        if not self._is_valid_data:
            return
        return ACBirdParser.parse_nested_protocol(data.get("text"))

    def get_protocol_detail(self, protocol_name):
        command = f"show protocols all {protocol_name}"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        if not self._is_valid_data:
            return
        return ACBirdParser.parse_protocol(data.get("text"))

    def get_route(self, network, detail=False):
        valid_network = self._verify_ip_network(network)
        if not valid_network:
            return "Route not valid"
        command = f"show route for {valid_network}"
        if detail:
            command = f"{command} all"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        return self._return_route_parsed_with_data(data, detail=detail)

    def get_route_from_protocol(self, network, protocol_name, detail=False):
        valid_network = self._verify_ip_network(network)
        valid_protocol_name = self._is_valid_protocol(protocol_name)
        if not valid_network:
            return "Route not valid"
        if not valid_protocol_name:
            return "Protocol name not valid"
        command = f"show route for {valid_network} protocol {protocol_name}"
        if detail:
            command = f"{command} all"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        return self._return_route_parsed_with_data(data, detail=detail)

    def get_route_from_asn(self, asn, detail=False):
        valid_asn = self._is_valid_asn(asn)
        if not valid_asn:
            return "ASN not valid"
        command = f"show route where bgp_path.first = {asn}"
        if detail:
            command = f"{command} all"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        return self._return_route_parsed_with_data(data, detail=detail)

    def get_route_origin_asn(self, asn, detail=False):
        valid_asn = self._is_valid_asn(asn)
        if not valid_asn:
            return "ASN not valid"
        command = f"show route where bgp_path.last = {asn}"
        if detail:
            command = f"{command} all"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        return self._return_route_parsed_with_data(data, detail=detail)

    def get_route_with_community(self, community, detail=False):
        valid_community = self._is_valid_community(community)
        if not valid_community:
            return "Community not valid"
        command = f"show route where {community} ~ bgp_community"
        if detail:
            command = f"{command} all"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        return self._return_route_parsed_with_data(data, detail=detail)

    def get_route_with_large_community(self, community, detail=False):
        valid_community = self._is_valid_community(community)
        if not valid_community:
            return "Large community not valid"
        command = f"show route where {community} ~ bgp_large_community"
        if detail:
            command = f"{command} all"
        logger.debug(f"[Command] {command}")
        data = self.execute_cmd(command)
        return self._return_route_parsed_with_data(data, detail=detail)
