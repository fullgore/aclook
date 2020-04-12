__all__ = [
    'NestedRoute',
    'NestedRouteListSchema',
    'RouteSchema',
    'RouteListSchema',
    'NestedProtocolSchema',
    'NestedProtocolListSchema',
    'BGPProtocolSchema',
    'RPKIProtocolSchema',
    'ACBirdParser',
]

import logging
import re

from marshmallow import Schema, fields, EXCLUDE

from utils.constants import \
    DICT_BIRD_PROTOCOL, \
    DICT_BIRD_BGP_PROTOCOL, \
    DICT_BIRD_RPKI_PROTOCOL, \
    DICT_BIRD_NESTED_ROUTE, \
    DICT_BIRD_ROUTE

logger = logging.getLogger(__name__)


class NestedProtocolSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    name = fields.String()
    type = fields.String(required=True)
    state = fields.String()
    info = fields.String()


class NestedProtocolListSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    protocols = fields.List(fields.Nested(NestedProtocolSchema))


class BGPProtocolSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    state = fields.String()
    source_ip = fields.String()
    peer_ip = fields.String()
    source_asn = fields.Integer()
    peer_asn = fields.Integer()
    exported = fields.Integer()
    imported = fields.Integer()


class RPKIProtocolSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    state = fields.String()
    cache_server = fields.String()
    serial_number = fields.Integer()
    ipv4_routes = fields.Integer()
    ipv6_routes = fields.Integer()


class NestedRoute(Schema):
    class Meta:
        unknown = EXCLUDE
    network = fields.String()
    since = fields.String()
    source = fields.String()
    protocol = fields.String()
    origin_asn = fields.Integer()
    active = fields.Boolean()


class NestedRouteListSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    routes = fields.List(fields.Nested(NestedRoute))


class RouteSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    network = fields.String()
    next_hop = fields.String()
    since = fields.String()
    origin = fields.String()
    origin_asn = fields.Integer()
    local_pref = fields.Integer()
    med = fields.Integer()
    as_path = fields.List(fields.Integer)
    community = fields.String()
    large_community = fields.String()


class RouteListSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    routes = fields.List(fields.Nested(RouteSchema))


PROTOCOL_TYPE_PARSER = {
    "bgp": 'parse_bgp_protocol',
    "rpki": 'parse_rpki_protocol'
}


class ACBirdParser:

    @staticmethod
    def _parse_line(_dict_parser: dict, line: str) -> tuple:
        for key, rx in _dict_parser.items():
            match = rx.search(line)
            if match:
                return key, match
        # if there are no matches
        return None, None

    @staticmethod
    def parse_nested_protocol(text: str):

        if not text:
            return None

        _protocol = {}

        for line in text.splitlines():

            line = re.sub(r'\s{2,}', ' ', line.strip())
            logger.debug(f"Line: {line}")
            key, re_value = ACBirdParser._parse_line(DICT_BIRD_PROTOCOL, line)
            logger.debug(f"[{key}] {re_value}")

            if key in ["rpki"]:
                name, state, info = re_value.group("name", "state", "info")
                logger.debug(f"[{key}]: {name} - {state}")
                _protocol = NestedProtocolSchema().dump({
                    "name": name, "type": key, "state": state, 'info': info
                })
            if key in ["bgp"]:
                name, state, info = re_value.group("name", "state", "info")
                logger.debug(f"[{key}]: {name} - {state} - {info}")
                _protocol = NestedProtocolSchema().dump({
                    "name": name, "type": key, "state": state, 'info': info
                })

        return NestedProtocolSchema().dump(_protocol)

    @staticmethod
    def parse_nested_protocols_list(text: str):

        if not text:
            return None

        _protocol_list = []

        for line in text.splitlines():
            _protocol = ACBirdParser.parse_nested_protocol(line)
            if _protocol:
                _protocol_list.append(_protocol)

        return NestedProtocolListSchema().dump({"protocols": _protocol_list})

    @staticmethod
    def parse_protocol(text: str):

        if not text:
            return

        nested_protocol = ACBirdParser.parse_nested_protocol(text)
        if not nested_protocol:
            return
        protocol_type = nested_protocol.get("type")
        parser_method = getattr(ACBirdParser, PROTOCOL_TYPE_PARSER.get(protocol_type))
        return parser_method(text)

    @staticmethod
    def parse_bgp_protocol(text: str):

        if not text:
            return

        _protocol = {}
        header_valid = False

        for line in text.splitlines():
            line = re.sub(r'\s{2,}', ' ', line.strip())
            logger.debug(f"Line: {line}")
            key, re_value = ACBirdParser._parse_line(DICT_BIRD_BGP_PROTOCOL, line)
            logger.debug(f"[{key}] {re_value}")

            if not key:
                continue

            if key in ["header"]:
                header_valid = True
            if not header_valid:
                continue

            if key in ["state", "description"]:
                value = re_value.group(key)
                logger.debug(f"[{key}]: {value}")
                _protocol[key] = value

            if key in ["source_ip", "peer_ip"]:
                value = re_value.group("ip")
                logger.debug(f"[{key}]: {value}")
                _protocol[key] = value

            if key in ["source_asn", "peer_asn"]:
                value = re_value.group("asn")
                logger.debug(f"[{key}]: {value}")
                _protocol[key] = value

            if key in ["filter_in", "filter_out"]:
                value = re_value.group("filter_name")
                logger.debug(f"[{key}]: {value}")
                _protocol[key] = value

            if key in ["routes"]:
                imported, exported, preferred = re_value.group("imported", "exported", "preferred")
                logger.debug(f"[{key}]: {imported} - {exported} - {preferred}")
                _protocol["imported"] = imported
                _protocol["exported"] = exported
                _protocol["preferred"] = preferred

        return BGPProtocolSchema().dump(_protocol)

    @staticmethod
    def parse_rpki_protocol(text: str):

        if not text:
            return

        _protocol = {}

        is_ipv4 = False
        is_ipv6 = False
        header_valid = False

        for line in text.splitlines():
            line = re.sub(r'\s{2,}', ' ', line.strip())
            logger.debug(f"Line: {line}")
            key, re_value = ACBirdParser._parse_line(DICT_BIRD_RPKI_PROTOCOL, line)
            logger.debug(f"[{key}] {re_value}")

            if not key:
                continue

            if key in ["header"]:
                header_valid = True
            if not header_valid:
                continue

            if key in ["state", "serial_number", "cache_server"]:
                value = re_value.group(key)
                logger.debug(f"[{key}]: {value}")
                _protocol[key] = value

            if key in ["is_ipv4"]:
                is_ipv4 = True
                is_ipv6 = False

            if key in ["is_ipv6"]:
                is_ipv4 = False
                is_ipv6 = True

            if key in ["routes"]:
                imported, exported, preferred = re_value.group("imported", "exported", "preferred")
                logger.debug(f"[{key}]: {imported} - {exported} - {preferred}")
                if is_ipv4:
                    _protocol["ipv4_routes"] = imported
                if is_ipv6:
                    _protocol["ipv6_routes"] = imported

        return RPKIProtocolSchema().dump(_protocol)

    @staticmethod
    def parse_nested_route_list(text: str) -> dict:

        _nested_route = []
        current_network = None

        for line in text.splitlines():

            line = re.sub(r'\s{2,}', ' ', line.strip())
            logger.debug(f"Line: {line}")
            key, re_value = ACBirdParser._parse_line(DICT_BIRD_NESTED_ROUTE, line)
            logger.debug(f"[{key}] {re_value}")

            if key in ["active_route"]:
                network, protocol, origin_asn, since = re_value.group("network", "protocol", "origin_asn", "since")
                logger.debug(f"[{key}]: {network} - {protocol} - {origin_asn} - {since}")
                current_network = network
                _nested_route.append(NestedRoute().dump({
                    "network": network, "protocol": protocol, "origin_asn": origin_asn, "active": True, "since": since,
                }))

            if key in ["next_route"]:
                protocol, origin_asn, since = re_value.group("protocol", "origin_asn", "since")
                if not current_network:
                    continue
                network = current_network
                logger.debug(f"[{key}]: {network} - {protocol} - {origin_asn} - {since}")
                _nested_route.append(NestedRoute().dump({
                    "network": network, "protocol": protocol, "origin_asn": origin_asn, "since": since,
                }))

        return NestedRouteListSchema().dump({"routes": _nested_route})

    @staticmethod
    def parse_route_list(text: str) -> dict:

        route_list = []
        current_route = None

        for line in text.splitlines():

            logger.debug(f"Route: {current_route}")

            line = re.sub(r'\s{2,}', ' ', line.strip())
            logger.debug(f"Line: {line}")
            key, re_value = ACBirdParser._parse_line(DICT_BIRD_ROUTE, line)
            logger.debug(f"[{key}] {re_value}")

            if key in ["active_route"]:
                network, protocol, origin_asn, since = re_value.group("network", "protocol", "origin_asn", "since")
                logger.debug(f"[{key}]: {network} - {protocol} - {origin_asn} - {since}")
                if current_route:
                    route_list.append(RouteSchema().dump(current_route))
                else:
                    current_route = {"network": network, "protocol": protocol, "origin_asn": origin_asn, "since": since}

            if key in ["next_route"]:
                if not current_route:
                    continue
                network = current_route.get("network")
                protocol, origin_asn, since = re_value.group("protocol", "origin_asn", "since")
                logger.debug(f"[{key}]: {network} - {protocol} - {origin_asn} - {since}")
                route_list.append(RouteSchema().dump(current_route))
                current_route = {"network": network, "protocol": protocol, "origin_asn": origin_asn, "since": since}

            if key in ["med", "local_pref"]:
                value = re_value.group(key)
                logger.debug(f"[{key}]: {value}")
                if current_route:
                    current_route[key] = value

            if key in ["origin", "next_hop"]:
                value = re_value.group(key)
                logger.debug(f"[{key}]: {value}")
                if current_route:
                    current_route[key] = value

            if key in ["as_path"]:
                values = re_value.group(key)
                logger.debug(f"[{key}]: {values}")
                as_path = re.findall(r"\d+", values)
                if current_route:
                    current_route[key] = as_path

            if key in ["community"]:
                values = re_value.group(key)
                logger.debug(f"[{key}]: {values}")
                if current_route:
                    current_route[key] = values

            if key in ["large_community"]:
                values = re_value.group(key)
                logger.debug(f"[{key}]: {values}")
                if current_route:
                    current_route[key] = values

        # Is a last route available
        if current_route:
            route_list.append(RouteSchema().dump(current_route))

        return RouteListSchema().dump({"routes": route_list})
