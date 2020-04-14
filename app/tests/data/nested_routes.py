route_a = """
Table master4:
1.1.1.0/24           unreachable [ipv4_core01_ny8 2020-03-31 from 185.94.141.136] * (100) [AS13335i]
                     unreachable [ipv4_core01_ams9 2020-04-03 from 185.94.141.142] (100) [AS13335i]
                     unreachable [ipv4_core02_ams9 2020-04-03 from 185.94.141.143] (100) [AS13335i]
                     unreachable [ipv4_core01_fr7 2020-04-03 from 185.94.141.133] (100) [AS13335i]
                     unreachable [ipv4_core02_sg3 2020-04-02 from 185.94.141.152] (100) [AS13335i]
                     unreachable [ipv4_core01_sv10 2020-04-02 from 185.94.141.147] (100) [AS13335i]
                     unreachable [ipv4_core01_sg3 2020-04-02 from 185.94.141.151] (100) [AS13335i]
                     unreachable [ipv4_core01_wes 2020-04-02 from 185.94.141.146] (100) [AS13335i]
                     unreachable [ipv4_core02_sv10 2020-03-31 from 185.94.141.148] (100) [AS13335i]
                     unreachable [ipv4_core01_sp4 2020-03-31 from 185.94.141.153] (100) [AS13335i]
                     unreachable [ipv4_core01_dc12 2020-03-31 from 185.94.141.145] (100) [AS13335i]
                     unreachable [ipv4_core02_ny8 2020-03-31 from 185.94.141.137] (100) [AS13335i]
                     unreachable [ipv4_core02_pa4 2020-03-31 from 185.94.141.139] (100) [AS13335i]
                     unreachable [ipv4_core02_ty8 2020-03-31 from 185.94.141.150] (100) [AS13335i]
                     unreachable [ipv4_core01_pa4 2020-03-31 from 185.94.141.138] (100) [AS13335i]
                     unreachable [ipv4_core01_pa2 2020-03-31 from 185.94.141.130] (100) [AS13335i]
                     unreachable [ipv4_core01_ty8 2020-03-31 from 185.94.141.149] (100) [AS13335i]
                     unreachable [ipv4_core02_tn2 2020-03-31 from 185.94.141.141] (100) [AS13335i]
                     unreachable [ipv4_core02_pa2 2020-03-31 from 185.94.141.135] (100) [AS13335i]
                     unreachable [ipv4_core01_tn2 2020-03-31 from 185.94.141.140] (100) [AS13335i]
                     unreachable [ipv4_core01_th2 2020-03-31 from 185.94.141.131] (100) [AS13335i]
"""

result_route_a = {'routes': [{'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_ny8'}, {'network': '1.1.1.0/24', 'since': '2020-04-03', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_ams9'}, {'network': '1.1.1.0/24', 'since': '2020-04-03', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core02_ams9'}, {'network': '1.1.1.0/24', 'since': '2020-04-03', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_fr7'}, {'network': '1.1.1.0/24', 'since': '2020-04-02', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core02_sg3'}, {'network': '1.1.1.0/24', 'since': '2020-04-02', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_sv10'}, {'network': '1.1.1.0/24', 'since': '2020-04-02', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_sg3'}, {'network': '1.1.1.0/24', 'since': '2020-04-02', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_wes'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core02_sv10'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_sp4'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_dc12'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core02_ny8'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core02_pa4'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core02_ty8'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_pa4'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_pa2'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_ty8'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core02_tn2'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core02_pa2'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_tn2'}, {'network': '1.1.1.0/24', 'since': '2020-03-31', 'origin_asn': 13335, 'active': True, 'protocol': 'ipv4_core01_th2'}]}

route_b = """
BIRD 2.0.7 ready.
Table master6:
2a0e:b700::/32       unreachable [ipv6_core01_pa2 2020-04-03 from 2a05:f440::] * (100) [AS35085i]
                     unreachable [ipv6_core01_fr7 2020-04-03 from 2a05:f440:3::] (100) [AS35085i]
                     unreachable [ipv6_core01_ty8 2020-04-03 from 2a05:f440:c::] (100) [AS35085i]
                     unreachable [ipv6_core02_ty8 2020-04-03 from 2a05:f440:c::1] (100) [AS35085i]
                     unreachable [ipv6_core02_sv10 2020-04-03 from 2a05:f440:b::1] (100) [AS35085i]
                     unreachable [ipv6_core01_wes 2020-04-03 from 2a05:f440:a::] (100) [AS35085i]
                     unreachable [ipv6_core01_sv10 2020-04-03 from 2a05:f440:b::] (100) [AS35085i]
                     unreachable [ipv6_core02_sg3 2020-04-03 from 2a05:f440:d::1] (100) [AS35085i]
                     unreachable [ipv6_core02_ny8 2020-04-03 from 2a05:f440:5::1] (100) [AS35085i]
                     unreachable [ipv6_core01_dc12 2020-04-03 from 2a05:f440:9::] (100) [AS35085i]
                     unreachable [ipv6_core01_sg3 2020-04-03 from 2a05:f440:d::] (100) [AS35085i]
                     unreachable [ipv6_core01_ny8 2020-04-03 from 2a05:f440:5::] (100) [AS35085i]
                     unreachable [ipv6_core01_tn2 2020-04-03 from 2a05:f440:7::] (100) [AS35085i]
                     unreachable [ipv6_core01_th2 2020-04-03 from 2a05:f440:1::] (100) [AS35085i]
                     unreachable [ipv6_core02_tn2 2020-04-03 from 2a05:f440:7::1] (100) [AS35085i]
                     unreachable [ipv6_core02_pa4 2020-04-03 from 2a05:f440:2::2] (100) [AS35085i]
                     unreachable [ipv6_core02_pa2 2020-04-03 from 2a05:f440::1] (100) [AS35085i]
                     unreachable [ipv6_core02_ams9 2020-04-03 from 2a05:f440:6::1] (100) [AS35085i]
                     unreachable [ipv6_core01_ams9 2020-04-03 from 2a05:f440:6::] (100) [AS35085i]
                     unreachable [ipv6_core01_pa4 2020-04-03 from 2a05:f440:2::1] (100) [AS35085i]
"""

result_route_b = {'routes': [{'protocol': 'ipv6_core01_pa2', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_fr7', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_ty8', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core02_ty8', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core02_sv10', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_wes', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_sv10', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core02_sg3', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core02_ny8', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_dc12', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_sg3', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_ny8', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_tn2', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_th2', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core02_tn2', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core02_pa4', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core02_pa2', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core02_ams9', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_ams9', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}, {'protocol': 'ipv6_core01_pa4', 'origin_asn': 35085, 'active': True, 'since': '2020-04-03', 'network': '2a0e:b700::/32'}]}


route_c = """
BIRD 2.0.7 ready.
Table master4:
0.0.0.0/0            unreachable [ipv4_core01_fr7 2020-04-03 from 185.94.141.133] * (100) [i]
                     unreachable [ipv4_core02_pa2 2020-03-31 from 185.94.141.135] (100) [i]
                     unreachable [ipv4_core01_wes 2020-03-31 from 185.94.141.146] (100) [i]
                     unreachable [ipv4_core01_sp4 2020-03-31 from 185.94.141.153] (100) [i]
                     unreachable [ipv4_core01_sg3 2020-03-31 from 185.94.141.151] (100) [i]
                     unreachable [ipv4_core02_ty8 2020-03-31 from 185.94.141.150] (100) [i]
                     unreachable [ipv4_core02_sv10 2020-03-31 from 185.94.141.148] (100) [i]
                     unreachable [ipv4_core01_dc12 2020-03-31 from 185.94.141.145] (100) [i]
                     unreachable [ipv4_core02_sg3 2020-03-31 from 185.94.141.152] (100) [i]
                     unreachable [ipv4_core01_ty8 2020-03-31 from 185.94.141.149] (100) [i]
                     unreachable [ipv4_core01_ny8 2020-03-31 from 185.94.141.136] (100) [i]
                     unreachable [ipv4_core01_sv10 2020-03-31 from 185.94.141.147] (100) [i]
                     unreachable [ipv4_core02_ny8 2020-03-31 from 185.94.141.137] (100) [i]
                     unreachable [ipv4_core01_pa2 2020-03-31 from 185.94.141.130] (100) [i]
                     unreachable [ipv4_core01_pa4 2020-03-31 from 185.94.141.138] (100) [i]
                     unreachable [ipv4_core02_tn2 2020-03-31 from 185.94.141.141] (100) [i]
                     unreachable [ipv4_core01_tn2 2020-03-31 from 185.94.141.140] (100) [i]
                     unreachable [ipv4_core01_th2 2020-03-31 from 185.94.141.131] (100) [i]
                     unreachable [ipv4_core02_ams9 2020-03-31 from 185.94.141.143] (100) [i]
                     unreachable [ipv4_core02_pa4 2020-03-31 from 185.94.141.139] (100) [i]
                     unreachable [ipv4_core01_ams9 2020-03-31 from 185.94.141.142] (100) [i]
"""

result_route_c = {'routes': [{'network': '0.0.0.0/0', 'active': True, 'since': '2020-04-03', 'protocol': 'ipv4_core01_fr7'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core02_pa2'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_wes'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_sp4'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_sg3'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core02_ty8'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core02_sv10'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_dc12'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core02_sg3'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_ty8'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_ny8'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_sv10'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core02_ny8'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_pa2'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_pa4'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core02_tn2'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_tn2'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_th2'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core02_ams9'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core02_pa4'}, {'network': '0.0.0.0/0', 'active': True, 'since': '2020-03-31', 'protocol': 'ipv4_core01_ams9'}]}


route_d = """
BIRD 2.0.7 ready.
Table master6:
::/0                 unreachable [ipv6_core02_pa2 2020-03-31 from 2a05:f440::1] * (100) [i]
                     unreachable [ipv6_core01_fr7 2020-04-03 from 2a05:f440:3::] (100) [i]
                     unreachable [ipv6_core02_sg3 2020-03-31 from 2a05:f440:d::1] (100) [i]
                     unreachable [ipv6_core01_sg3 2020-03-31 from 2a05:f440:d::] (100) [i]
                     unreachable [ipv6_core01_ty8 2020-03-31 from 2a05:f440:c::] (100) [i]
                     unreachable [ipv6_core02_sv10 2020-03-31 from 2a05:f440:b::1] (100) [i]
                     unreachable [ipv6_core01_dc12 2020-03-31 from 2a05:f440:9::] (100) [i]
                     unreachable [ipv6_core01_sv10 2020-03-31 from 2a05:f440:b::] (100) [i]
                     unreachable [ipv6_core02_ty8 2020-03-31 from 2a05:f440:c::1] (100) [i]
                     unreachable [ipv6_core01_ny8 2020-03-31 from 2a05:f440:5::] (100) [i]
                     unreachable [ipv6_core01_wes 2020-03-31 from 2a05:f440:a::] (100) [i]
                     unreachable [ipv6_core01_tn2 2020-03-31 from 2a05:f440:7::] (100) [i]
                     unreachable [ipv6_core02_pa4 2020-03-31 from 2a05:f440:2::2] (100) [i]
                     unreachable [ipv6_core02_ams9 2020-03-31 from 2a05:f440:6::1] (100) [i]
                     unreachable [ipv6_core02_ny8 2020-03-31 from 2a05:f440:5::1] (100) [i]
                     unreachable [ipv6_core02_tn2 2020-03-31 from 2a05:f440:7::1] (100) [i]
                     unreachable [ipv6_core01_ams9 2020-03-31 from 2a05:f440:6::] (100) [i]
                     unreachable [ipv6_core01_th2 2020-03-31 from 2a05:f440:1::] (100) [i]
                     unreachable [ipv6_core01_pa2 2020-03-31 from 2a05:f440::] (100) [i]
                     unreachable [ipv6_core01_pa4 2020-03-31 from 2a05:f440:2::1] (100) [i]
"""

result_route_d = {'routes': [{'active': True, 'protocol': 'ipv6_core02_pa2', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_fr7', 'network': '::/0', 'since': '2020-04-03'}, {'active': True, 'protocol': 'ipv6_core02_sg3', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_sg3', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_ty8', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core02_sv10', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_dc12', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_sv10', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core02_ty8', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_ny8', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_wes', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_tn2', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core02_pa4', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core02_ams9', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core02_ny8', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core02_tn2', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_ams9', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_th2', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_pa2', 'network': '::/0', 'since': '2020-03-31'}, {'active': True, 'protocol': 'ipv6_core01_pa4', 'network': '::/0', 'since': '2020-03-31'}]}

route_e = """
BIRD 2.0.7 ready.
Table master6:
                     unreachable [ipv6_core01_fr7 2020-04-03 from 2a05:f440:3::] (100) [i]
                     unreachable [ipv6_core02_sg3 2020-03-31 from 2a05:f440:d::1] (100) [i]
                     unreachable [ipv6_core01_sg3 2020-03-31 from 2a05:f440:d::] (100) [i]
                     unreachable [ipv6_core01_ty8 2020-03-31 from 2a05:f440:c::] (100) [i]
                     unreachable [ipv6_core02_sv10 2020-03-31 from 2a05:f440:b::1] (100) [i]
                     unreachable [ipv6_core01_dc12 2020-03-31 from 2a05:f440:9::] (100) [i]
                     unreachable [ipv6_core01_sv10 2020-03-31 from 2a05:f440:b::] (100) [i]
                     unreachable [ipv6_core02_ty8 2020-03-31 from 2a05:f440:c::1] (100) [i]
                     unreachable [ipv6_core01_ny8 2020-03-31 from 2a05:f440:5::] (100) [i]
                     unreachable [ipv6_core01_wes 2020-03-31 from 2a05:f440:a::] (100) [i]
                     unreachable [ipv6_core01_tn2 2020-03-31 from 2a05:f440:7::] (100) [i]
                     unreachable [ipv6_core02_pa4 2020-03-31 from 2a05:f440:2::2] (100) [i]
                     unreachable [ipv6_core02_ams9 2020-03-31 from 2a05:f440:6::1] (100) [i]
                     unreachable [ipv6_core02_ny8 2020-03-31 from 2a05:f440:5::1] (100) [i]
                     unreachable [ipv6_core02_tn2 2020-03-31 from 2a05:f440:7::1] (100) [i]
                     unreachable [ipv6_core01_ams9 2020-03-31 from 2a05:f440:6::] (100) [i]
                     unreachable [ipv6_core01_th2 2020-03-31 from 2a05:f440:1::] (100) [i]
                     unreachable [ipv6_core01_pa2 2020-03-31 from 2a05:f440::] (100) [i]
                     unreachable [ipv6_core01_pa4 2020-03-31 from 2a05:f440:2::1] (100) [i]
"""

route_f = """
BIRD 2.0.7 ready.
Table master6:
                     unreachable [ipv4_core01_dc12 2020-03-31 from 185.94.141.145] (100) [AS13335i]
                     unreachable [ipv4_core02_ny8 2020-03-31 from 185.94.141.137] (100) [AS13335i]
                     unreachable [ipv4_core02_pa4 2020-03-31 from 185.94.141.139] (100) [AS13335i]
                     unreachable [ipv4_core02_ty8 2020-03-31 from 185.94.141.150] (100) [AS13335i]
                     unreachable [ipv4_core01_pa4 2020-03-31 from 185.94.141.138] (100) [AS13335i]
                     unreachable [ipv4_core01_pa2 2020-03-31 from 185.94.141.130] (100) [AS13335i]
"""

