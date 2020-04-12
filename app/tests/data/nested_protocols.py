protocol_a = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
device1    Device     ---        up     2020-03-31
routinator RPKI       ---        up     2020-04-03    Established
gortr      RPKI       ---        up     2020-04-03    Established
ipv4_pipe_pa2 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_pa2
ipv4_pipe_pa4 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_pa4
ipv4_pipe_ny8 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_ny8
ipv4_pipe_tn2 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_tn2
ipv4_pipe_ams9 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_ams9
ipv4_pipe_dc1 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_dc1
ipv4_pipe_th2 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_th2
ipv4_pipe_dc12 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_dc12
ipv4_pipe_wes Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_wes
ipv4_pipe_sv10 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_sv10
ipv4_pipe_ty8 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_ty8
ipv4_pipe_sg3 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_sg3
ipv4_pipe_sp4 Pipe       ---        up     2020-03-31    master4 <=> ipv4_table_sp4
ipv4_pipe_fr7 Pipe       ---        up     2020-04-03    master4 <=> ipv4_table_fr7
ipv6_pipe_pa2 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_pa2
ipv6_pipe_pa4 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_pa4
ipv6_pipe_ny8 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_ny8
ipv6_pipe_tn2 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_tn2
ipv6_pipe_ams9 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_ams9
ipv6_pipe_dc1 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_dc1
ipv6_pipe_th2 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_th2
ipv6_pipe_dc12 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_dc12
ipv6_pipe_wes Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_wes
ipv6_pipe_sv10 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_sv10
ipv6_pipe_ty8 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_ty8
ipv6_pipe_sg3 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_sg3
ipv6_pipe_sp4 Pipe       ---        up     2020-03-31    master6 <=> ipv6_table_sp4
ipv6_pipe_fr7 Pipe       ---        up     2020-04-03    master6 <=> ipv6_table_fr7
ipv4_core01_ams9 BGP        ---        up     2020-03-31    Established
ipv4_core01_ny8 BGP        ---        up     2020-03-31    Established
ipv4_core01_pa2 BGP        ---        up     2020-03-31    Established
ipv4_core01_pa4 BGP        ---        up     2020-03-31    Established
ipv4_core01_th2 BGP        ---        up     2020-03-31    Established
ipv4_core01_tn2 BGP        ---        up     2020-03-31    Established
ipv4_core02_ams9 BGP        ---        up     2020-03-31    Established
ipv4_core02_ny8 BGP        ---        up     2020-03-31    Established
ipv4_core02_pa2 BGP        ---        up     2020-03-31    Established
ipv4_core02_pa4 BGP        ---        up     2020-03-31    Established
ipv4_core02_tn2 BGP        ---        up     2020-03-31    Established
ipv4_core01_dc12 BGP        ---        up     2020-03-31    Established
ipv4_core01_wes BGP        ---        up     2020-03-31    Established
ipv4_core01_sv10 BGP        ---        up     2020-03-31    Established
ipv4_core02_sv10 BGP        ---        up     2020-03-31    Established
ipv4_core01_ty8 BGP        ---        up     2020-03-31    Established
ipv4_core02_ty8 BGP        ---        up     2020-03-31    Established
ipv4_core01_sg3 BGP        ---        up     2020-03-31    Established
ipv4_core02_sg3 BGP        ---        up     2020-03-31    Established
ipv4_core01_sp4 BGP        ---        up     2020-03-31    Established
ipv4_core01_fr7 BGP        ---        up     2020-04-03    Established
ipv6_core01_ams9 BGP        ---        up     2020-03-31    Established
ipv6_core01_ny8 BGP        ---        up     2020-03-31    Established
ipv6_core01_pa2 BGP        ---        up     2020-03-31    Established
ipv6_core01_pa4 BGP        ---        up     2020-03-31    Established
ipv6_core01_th2 BGP        ---        up     2020-03-31    Established
ipv6_core01_tn2 BGP        ---        up     2020-03-31    Established
ipv6_core02_ams9 BGP        ---        up     2020-03-31    Established
ipv6_core02_ny8 BGP        ---        up     2020-03-31    Established
ipv6_core02_pa2 BGP        ---        up     2020-03-31    Established
ipv6_core02_pa4 BGP        ---        up     2020-03-31    Established
ipv6_core02_tn2 BGP        ---        up     2020-03-31    Established
ipv6_core01_dc12 BGP        ---        up     2020-03-31    Established
ipv6_core01_wes BGP        ---        up     2020-03-31    Established
ipv6_core01_sv10 BGP        ---        up     2020-03-31    Established
ipv6_core02_sv10 BGP        ---        up     2020-03-31    Established
ipv6_core01_ty8 BGP        ---        up     2020-03-31    Established
ipv6_core02_ty8 BGP        ---        up     2020-03-31    Established
ipv6_core01_sg3 BGP        ---        up     2020-03-31    Established
ipv6_core02_sg3 BGP        ---        up     2020-03-31    Established
ipv6_core01_sp4 BGP        ---        start  2020-03-31    Connect       Socket: Network is unreachable
ipv6_core01_fr7 BGP        ---        up     2020-04-03    Established
ipv4_full_table BGP        ---        start  2020-04-05    Connect       Received: Administrative shutdown
"""

result_protocol_a = {'protocols': [{'type': 'rpki', 'name': 'routinator', 'info': 'Established', 'state': 'up'},
                                   {'type': 'rpki', 'name': 'gortr', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_ams9', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_ny8', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_pa2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_pa4', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_th2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_tn2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core02_ams9', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core02_ny8', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core02_pa2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core02_pa4', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core02_tn2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_dc12', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_wes', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_sv10', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core02_sv10', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_ty8', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core02_ty8', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_sg3', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core02_sg3', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_sp4', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_core01_fr7', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_ams9', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_ny8', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_pa2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_pa4', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_th2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_tn2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core02_ams9', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core02_ny8', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core02_pa2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core02_pa4', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core02_tn2', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_dc12', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_wes', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_sv10', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core02_sv10', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_ty8', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core02_ty8', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_sg3', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core02_sg3', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_sp4',
                                    'info': 'Connect Socket: Network is unreachable', 'state': 'start'},
                                   {'type': 'bgp', 'name': 'ipv6_core01_fr7', 'info': 'Established', 'state': 'up'},
                                   {'type': 'bgp', 'name': 'ipv4_full_table',
                                    'info': 'Connect Received: Administrative shutdown', 'state': 'start'}]}

protocol_b = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
ipv6_core01_fr7 BGP        ---        up     2020-04-03    Established
"""

result_protocol_b = {'protocols': [{'info': 'Established', 'type': 'bgp', 'name': 'ipv6_core01_fr7', 'state': 'up'}]}

protocol_c = """
> # docker exec -ti bird birdc show protocols gortr
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
gortr      RPKI       ---        up     2020-04-03    Established
"""

result_protocol_c = {'protocols': [{'info': 'Established', 'type': 'rpki', 'name': 'gortr', 'state': 'up'}]}

protocol_d = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
ipv4_full_table BGP        ---        start  2020-04-05    Connect       Received: Administrative shutdown
"""

result_protocol_d = {'protocols': [
    {'info': 'Connect Received: Administrative shutdown', 'type': 'bgp', 'name': 'ipv4_full_table', 'state': 'start'}]}

protocol_e = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
"""

protocol_f = """
BIRD 2.0.7 ready.
Name       Proto      Table      State  Since         Info
ipv4_full_table BGP        ---        start  2020-04-05
"""
