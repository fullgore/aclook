import re

# List codes
# https://gitlab.labs.nic.cz/labs/bird/blob/master/doc/reply_codes
# Reply codes of BIRD command-line interface
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 0xxx  Action suceessfully completed
# 1xxx  Table entry
# 2xxx  Table heading
# 8xxx  Run-time error
# 9xxx  Parse-time error
# <space> Continuation
# + Spontaneous printout

BIRD_SUCCESS_CODE_END = "0000"

BIRD_UNUSED_CODE = "3000"
BIRD_UNKNOWN_MESSAGE = "No message"

BIRD_SUCCESS_CODES = {
    "0000": "OK",
    "0001": "Welcome",
    "0002": "Reading configuration",
    "0003": "Reconfigured",
    "0004": "Reconfiguration in progress",
    "0005": "Reconfiguration already in progress, queueing",
    "0006": "Reconfiguration ignored, shutting down",
    "0007": "Shutdown ordered",
    "0008": "Already disabled",
    "0009": "Disabled",
    "0010": "Already enabled",
    "0011": "Enabled",
    "0012": "Restarted",
    "0013": "Status report",
    "0014": "Route count",
    "0015": "Reloading",
    "0016": "Access restricted",
    "0017": "Reconfiguration already in progress, removing queued config",
    "0018": "Reconfiguration confirmed",
    "0019": "Nothing to do (configure undo/confirm)",
    "0020": "Configuration OK",
    "0021": "Undo requested",
    "0022": "Undo scheduled",
    "0023": "Evaluation of expression",
    "0024": "Graceful restart status report",
}

BIRD_ENTRY_CODES = {
    "1000": "BIRD version",
    "1001": "Interface list",
    "1002": "Protocol list",
    "1003": "Interface address",
    "1004": "Interface flags",
    "1005": "Interface summary",
    "1006": "Protocol details",
    "1007": "Route list",
    "1008": "Route details",
    "1009": "Static route list",
    "1010": "Symbol list",
    "1011": "Uptime",
    "1012": "Route extended attribute list",
    "1013": "Show ospf neighbors",
    "1014": "Show ospf",
    "1015": "Show ospf interface",
    "1016": "Show ospf state/topology",
    "1017": "Show ospf lsadb",
    "1018": "Show memory",
    "1019": "Show ROA list",
    "1020": "Show BFD sessions",
    "1021": "Show RIP interface",
    "1022": "Show RIP neighbors",
    "1023": "Show Babel interfaces",
    "1024": "Show Babel neighbors",
    "1025": "Show Babel entries",
}

BIRD_RUNNING_CODES = {
    "8000": "Reply too long",
    "8001": "Route not found",
    "8002": "Configuration file error",
    "8003": "No protocols match",
    "8004": "Stopped due to reconfiguration",
    "8005": "Protocol is down => cannot dump",
    "8006": "Reload failed",
    "8007": "Access denied",
    "8008": "Evaluation runtime error",
}

BIRD_PARSING_ERROR_CODES = {
    "9000": "Command too long",
    "9001": "Parse error",
    "9002": "Invalid symbol type",
}

BIRD_RETURN_CODE = list(BIRD_SUCCESS_CODES.keys()) \
    + list(BIRD_ENTRY_CODES.keys()) \
    + list(BIRD_RUNNING_CODES.keys()) \
    + list(BIRD_PARSING_ERROR_CODES.keys())

#
# List of parsing dictionnary
#

RE_BGP_HEADER = re.compile(
    r"(?P<name>.+) BGP --- (?P<state>.+) (?P<since>\d+-\d+-\d+|\d+:\d+:\d+.\d+) (?P<info>.*|$)")
RE_RPKI_HEADER = re.compile(
    r"(?P<name>.+) RPKI --- (?P<state>.+) (?P<since>\d+-\d+-\d+|\d+:\d+:\d+.\d+) (?P<info>.*|$)")

DICT_BIRD_PROTOCOL = {
    "rpki": RE_RPKI_HEADER,
    "bgp": RE_BGP_HEADER,
}

DICT_BIRD_BGP_PROTOCOL = {
    "header": RE_BGP_HEADER,
    "state": re.compile(r"BGP state: (?P<state>.*)"),
    "source_ip": re.compile(r"Source address: (?P<ip>.*)"),
    "peer_ip": re.compile(r"Neighbor address: (?P<ip>.*)"),
    "source_asn": re.compile(r"Local AS: (?P<asn>\d+)"),
    "peer_asn": re.compile(r"Neighbor AS: (?P<asn>\d+)"),
    "description": re.compile(r"Description: (?P<description>.*)"),
    "routes": re.compile(
        r"Routes: (?P<imported>\d+) imported, (?P<exported>\d+) exported, (?P<preferred>\d+) preferred"),
    "filter_in": re.compile(r"Input filter: (?P<filter_name>.*)"),
    "filter_out": re.compile(r"Output filter: (?P<filter_name>.*)")
}

DICT_BIRD_RPKI_PROTOCOL = {
    "header": RE_RPKI_HEADER,
    "state": re.compile(r"Status: (?P<state>.*)"),
    "cache_server": re.compile(r"Cache server: (?P<cache_server>.*)"),
    "serial_number": re.compile(r"Serial number: (?P<serial_number>.*)"),
    "routes": re.compile(
        r"Routes: (?P<imported>\d+) imported, (?P<exported>\d+) exported, (?P<preferred>\d+) preferred"),
    "is_ipv4": re.compile(r"Channel roa4"),
    "is_ipv6": re.compile(r"Channel roa6"),
}

RE_ACTIVE_ROUTE = re.compile(
    r"(?P<network>(.*/\d+)) (?P<via>(unreachable|.*)) \[(?P<protocol>.*) (?P<since>((\d+:\d+:\d+.\d+)|(\d+-\d+-\d+))) "
    r"from (?P<source>.*)\] (?P<active>.*) \((?P<distance>.*)\) \[AS(?P<origin_asn>\d+)(?P<origin>.*)\]")
RE_NEXT_ROUTE = re.compile(
    r"(?P<via>(unreachable|.*)) \[(?P<protocol>.*) (?P<since>((\d+:\d+:\d+.\d+)|(\d+-\d+-\d+))) "
    r"from (?P<source>.*)\] \((?P<distance>.*)\) \[AS(?P<origin_asn>\d+)(?P<origin>.*)\]")

DICT_BIRD_NESTED_ROUTE = {
    "active_route": RE_ACTIVE_ROUTE,
    "next_route": RE_NEXT_ROUTE,
}

DICT_BIRD_ROUTE = {
    "active_route": RE_ACTIVE_ROUTE,
    "next_route": RE_NEXT_ROUTE,
    "origin": re.compile(r"^BGP\.origin: (?P<origin>.s)"),
    "as_path": re.compile(r"^BGP\.as_path: (?P<as_path>.*)"),
    "next_hop": re.compile(r"^BGP\.next_hop: (?P<next_hop>.*)"),
    "med": re.compile(r"^BGP\.med: (?P<med>\d+)"),
    "local_pref": re.compile(r"^BGP\.local_pref: (?P<local_pref>\d+)"),
    "community": re.compile(r"^BGP\.community: (?P<community>.*)"),  # (INT,INT)
    "large_community": re.compile(r"^BGP.large_community: (?P<large_community>.*)"),  # (INT, INT ,INT)
}
