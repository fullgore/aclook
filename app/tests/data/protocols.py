protocol_a = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
ipv6_core01_fr7 BGP        ---        up     2020-04-03    Established
  Description:    IPV6 core01.fr7
  BGP state:          Established
    Neighbor address: 2a05:f440:3::
    Neighbor AS:      35280
    Local AS:         35280
    Neighbor ID:      185.94.141.133
    Local capabilities
      Multiprotocol
        AF announced: ipv6
      Route refresh
      Graceful restart
      4-octet AS numbers
      ADD-PATH
        RX: ipv6
        TX:
      Enhanced refresh
      Long-lived graceful restart
    Neighbor capabilities
      Multiprotocol
        AF announced: ipv6
      Route refresh
      Graceful restart
      4-octet AS numbers
      Long-lived graceful restart
    Session:          internal multihop AS4
    Source address:   2a0e:b700::6
    Hold timer:       84.219/90
    Keepalive timer:  7.427/30
  Channel ipv6
    State:          UP
    Table:          ipv6_table_fr7
    Preference:     100
    Input filter:   bgp_in_v6
    Output filter:  no_routes
    Routes:         80652 imported, 0 exported, 80652 preferred
    Route change stats:     received   rejected   filtered    ignored   accepted
      Import updates:        2613588          0          0          0    2613588
      Import withdraws:        50079          0        ---          0      50079
      Export updates:        2613729    2613729          0        ---          0
      Export withdraws:        50079        ---        ---        ---          0
    BGP Next hop:   2a0e:b700::6
    IGP IPv6 table: ipv6_table_fr7
"""

result_protocol_a = {'source_ip': '2a0e:b700::6', 'state': 'Established', 'exported': 0, 'imported': 80652,
                     'source_asn': 35280, 'peer_ip': '2a05:f440:3::', 'peer_asn': 35280}

protocol_b = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
ipv4_core01_pa4 BGP        ---        up     2020-03-31    Established
  Description:    IPV4 core01.pa4
  BGP state:          Established
    Neighbor address: 185.94.141.138
    Neighbor AS:      35280
    Local AS:         35280
    Neighbor ID:      185.94.141.138
    Local capabilities
      Multiprotocol
        AF announced: ipv4
      Route refresh
      Graceful restart
      4-octet AS numbers
      ADD-PATH
        RX: ipv4
        TX:
      Enhanced refresh
      Long-lived graceful restart
    Neighbor capabilities
      Multiprotocol
        AF announced: ipv4
      Route refresh
      Graceful restart
      4-octet AS numbers
      Long-lived graceful restart
    Session:          internal multihop AS4
    Source address:   45.12.184.6
    Hold timer:       67.498/90
    Keepalive timer:  25.586/30
  Channel ipv4
    State:          UP
    Table:          ipv4_table_pa4
    Preference:     100
    Input filter:   bgp_in_v4
    Output filter:  no_routes
    Routes:         800625 imported, 0 exported, 536409 preferred
    Route change stats:     received   rejected   filtered    ignored   accepted
      Import updates:       14990086          0          0          0   14990086
      Import withdraws:       256829          0        ---          0     256829
      Export updates:       21859542   21859542          0        ---          0
      Export withdraws:       245510        ---        ---        ---          0
    BGP Next hop:   45.12.184.6
    IGP IPv4 table: ipv4_table_pa4
"""

result_protocol_b = {'source_ip': '45.12.184.6', 'state': 'Established', 'exported': 0, 'imported': 800625,
                     'source_asn': 35280, 'peer_ip': '185.94.141.138', 'peer_asn': 35280}

protocol_c = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
ipv4_full_table BGP        ---        start  2020-04-05    Connect       Received: Administrative shutdown
  Description:    IPV4 vpn.acorso.fr
  BGP state:          Connect
    Neighbor address: 45.12.184.3
    Neighbor AS:      35085
    Local AS:         35280
    Last error:       Received: Administrative shutdown
  Channel ipv4
    State:          DOWN
    Table:          master4
    Preference:     100
    Input filter:   no_routes
    Output filter:  accept_all
    IGP IPv4 table: master4
"""

result_protocol_c = {'state': 'Connect', 'source_asn': 35280, 'peer_ip': '45.12.184.3', 'peer_asn': 35085}

protocol_d = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
ipv4_full_table BGP        ---        start  2020-04-05
  Description:    IPV4 vpn.acorso.fr
  BGP state:          Connect
    Neighbor address: 45.12.184.3
    Neighbor AS:      35085
    Last error:       Received: Administrative shutdown
  Channel ipv4
    State:          DOWN
    Table:          master4
    Preference:     100
    Input filter:   no_routes
    Output filter:  accept_all
    IGP IPv4 table: master4
"""

result_protocol_d = {}

protocol_e = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
    Preference:     100
    Input filter:   no_routes
    Output filter:  accept_all
    IGP IPv4 table: master4
"""

result_protocol_e = {}

protocol_f = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
routinator RPKI       ---        up     2020-04-03    Established
  Cache server:     45.12.184.6:3323
  Status:           Established
  Transport:        Unprotected over TCP
  Protocol version: 1
  Session ID:       49867
  Serial number:    439
  Last update:      before 8.114 s
  Refresh timer   : 21.885/30
  Retry timer     : ---
  Expire timer    : 7191.885/7200
  Channel roa4
    State:          UP
    Table:          roa_r4
    Preference:     100
    Input filter:   ACCEPT
    Output filter:  REJECT
    Routes:         118135 imported, 0 exported, 3460 preferred
    Route change stats:     received   rejected   filtered    ignored   accepted
      Import updates:         121022          0          0          0     121022
      Import withdraws:         2887          0        ---          0       2887
      Export updates:              0          0          0        ---          0
      Export withdraws:            0        ---        ---        ---          0
  Channel roa6
    State:          UP
    Table:          roa_r6
    Preference:     100
    Input filter:   ACCEPT
    Output filter:  REJECT
    Routes:         19854 imported, 0 exported, 598 preferred
    Route change stats:     received   rejected   filtered    ignored   accepted
      Import updates:          20347          0          0          0      20347
      Import withdraws:          493          0        ---          0        493
      Export updates:              0          0          0        ---          0
      Export withdraws:            0        ---        ---        ---          0
"""

result_protocol_f = {'ipv4_routes': 118135, 'serial_number': 439, 'cache_server': '45.12.184.6:3323',
                     'ipv6_routes': 19854, 'state': 'Established'}

protocol_g = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
routinator RPKI       ---        up     2020-04-03    Established
  Cache server:     45.12.184.6:3323
  Status:           Established
  Transport:        Unprotected over TCP
  Protocol version: 1
  Session ID:       49867
  Serial number:    487
  Last update:      before 12.776 s
  Refresh timer   : 17.223/30
  Retry timer     : ---
  Expire timer    : 7187.223/7200
  Channel roa4
    State:          UP
    Table:          roa_r4
    Preference:     100
    Input filter:   ACCEPT
    Output filter:  REJECT
    Routes:         118302 imported, 0 exported, 3654 preferred
    Route change stats:     received   rejected   filtered    ignored   accepted
      Import updates:         121248          0          0          0     121248
      Import withdraws:         2946          0        ---          0       2946
      Export updates:              0          0          0        ---          0
      Export withdraws:            0        ---        ---        ---          0
  Channel roa6
    State:          UP
    Table:          roa_r6
    Preference:     100
    Input filter:   ACCEPT
    Output filter:  REJECT
    Routes:         19866 imported, 0 exported, 619 preferred
    Route change stats:     received   rejected   filtered    ignored   accepted
      Import updates:          20369          0          0          0      20369
      Import withdraws:          503          0        ---          0        503
      Export updates:              0          0          0        ---          0
      Export withdraws:            0        ---        ---        ---          0
"""

result_protocol_g = {'ipv4_routes': 118302, 'serial_number': 487, 'cache_server': '45.12.184.6:3323',
                     'ipv6_routes': 19866, 'state': 'Established'}


protocol_h = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
  Cache server:     45.12.184.6:3323
  Status:           Established
  Transport:        Unprotected over TCP
  Protocol version: 1
  Session ID:       49867
  Serial number:    487
  Last update:      before 12.776 s
  Refresh timer   : 17.223/30
  Retry timer     : ---
  Expire timer    : 7187.223/7200
  Channel roa4
    State:          UP
    Table:          roa_r4
    Preference:     100
    Input filter:   ACCEPT
    Output filter:  REJECT
    Routes:         118302 imported, 0 exported, 3654 preferred
    Route change stats:     received   rejected   filtered    ignored   accepted
      Import updates:         121248          0          0          0     121248
      Import withdraws:         2946          0        ---          0       2946
      Export updates:              0          0          0        ---          0
      Export withdraws:            0        ---        ---        ---          0
  Channel roa6
    State:          UP
    Table:          roa_r6
    Preference:     100
    Input filter:   ACCEPT
    Output filter:  REJECT
    Routes:         19866 imported, 0 exported, 619 preferred
    Route change stats:     received   rejected   filtered    ignored   accepted
      Import updates:          20369          0          0          0      20369
      Import withdraws:          503          0        ---          0        503
      Export updates:              0          0          0        ---          0
      Export withdraws:            0        ---        ---        ---          0
"""

result_protocol_h = {}

protocol_i = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
"""

result_protocol_i = {}