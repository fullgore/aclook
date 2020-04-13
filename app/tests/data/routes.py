
route_a = """
BIRD 2.0.7 ready.
Table master4:
45.12.184.0/24       unreachable [ipv4_core01_pa2 2020-03-31 from 185.94.141.130] * (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.130
                     unreachable [ipv4_core01_fr7 2020-04-03 from 185.94.141.133] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.133 185.94.141.130
                     unreachable [ipv4_core01_sp4 2020-03-31 from 185.94.141.153] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.153 185.94.141.130
                     unreachable [ipv4_core02_sg3 2020-03-31 from 185.94.141.152] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.152 185.94.141.130
                     unreachable [ipv4_core01_ams9 2020-03-31 from 185.94.141.142] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.142 185.94.141.130
                     unreachable [ipv4_core01_pa4 2020-03-31 from 185.94.141.138] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.138
                     unreachable [ipv4_core01_ny8 2020-03-31 from 185.94.141.136] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.136
                     unreachable [ipv4_core02_pa2 2020-03-31 from 185.94.141.135] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.135 185.94.141.130
                     unreachable [ipv4_core02_sv10 2020-03-31 from 185.94.141.148] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.148 185.94.141.130
                     unreachable [ipv4_core02_ty8 2020-03-31 from 185.94.141.150] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.150 185.94.141.130
                     unreachable [ipv4_core01_th2 2020-03-31 from 185.94.141.131] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.131 185.94.141.130
                     unreachable [ipv4_core01_wes 2020-03-31 from 185.94.141.146] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.146 185.94.141.130
                     unreachable [ipv4_core01_sv10 2020-03-31 from 185.94.141.147] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.147 185.94.141.130
                     unreachable [ipv4_core02_ny8 2020-03-31 from 185.94.141.137] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.137 185.94.141.130
                     unreachable [ipv4_core02_ams9 2020-03-31 from 185.94.141.143] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.143 185.94.141.130
                     unreachable [ipv4_core02_pa4 2020-03-31 from 185.94.141.139] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.139 185.94.141.130
                     unreachable [ipv4_core01_dc12 2020-03-31 from 185.94.141.145] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.145 185.94.141.130
                     unreachable [ipv4_core01_tn2 2020-03-31 from 185.94.141.140] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.140 185.94.141.130
                     unreachable [ipv4_core01_ty8 2020-03-31 from 185.94.141.149] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.149 185.94.141.130
                     unreachable [ipv4_core02_tn2 2020-03-31 from 185.94.141.141] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.141 185.94.141.130
                     unreachable [ipv4_core01_sg3 2020-03-31 from 185.94.141.151] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 100.65.0.131
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.151 185.94.141.130
"""

result_route_a = {'routes': [{'since': '2020-03-31', 'protocol': 'ipv4_core01_pa2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-04-03', 'protocol': 'ipv4_core01_fr7', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_sp4', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core02_sg3', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_ams9', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_pa4', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_ny8', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core02_pa2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core02_sv10', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core02_ty8', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_th2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_wes', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_sv10', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core02_ny8', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core02_ams9', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core02_pa4', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_dc12', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_tn2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_ty8', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core02_tn2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}, {'since': '2020-03-31', 'protocol': 'ipv4_core01_sg3', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,300) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '45.12.184.0/24', 'local_pref': 10000, 'next_hop': '100.65.0.131'}]}

route_b = """
BIRD 2.0.7 ready.
Table master6:
2a0e:b700::/32       unreachable [ipv6_core01_pa2 2020-04-03 from 2a05:f440::] * (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_fr7 2020-04-03 from 2a05:f440:3::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.133 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_ty8 2020-04-03 from 2a05:f440:c::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.149 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core02_ty8 2020-04-03 from 2a05:f440:c::1] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.150 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core02_sv10 2020-04-03 from 2a05:f440:b::1] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.147 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_wes 2020-04-03 from 2a05:f440:a::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.148 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_sv10 2020-04-03 from 2a05:f440:b::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.146 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core02_sg3 2020-04-03 from 2a05:f440:d::1] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.152 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core02_ny8 2020-04-03 from 2a05:f440:5::1] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.137 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_dc12 2020-04-03 from 2a05:f440:9::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.145 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_sg3 2020-04-03 from 2a05:f440:d::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.151 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_ny8 2020-04-03 from 2a05:f440:5::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.136
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_tn2 2020-04-03 from 2a05:f440:7::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.140 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_th2 2020-04-03 from 2a05:f440:1::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.131 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core02_tn2 2020-04-03 from 2a05:f440:7::1] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.141 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core02_pa4 2020-04-03 from 2a05:f440:2::2] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.139 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core02_pa2 2020-04-03 from 2a05:f440::1] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.135 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core02_ams9 2020-04-03 from 2a05:f440:6::1] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.143 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_ams9 2020-04-03 from 2a05:f440:6::] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.142 185.94.141.130
	BGP.large_community: (35085, 0, 35085)
                     unreachable [ipv6_core01_pa4 2020-04-03 from 2a05:f440:2::1] (100) [AS35085i]
	Type: BGP univ
	BGP.origin: IGP
	BGP.as_path: 35085
	BGP.next_hop: 2a05:f440::2
	BGP.local_pref: 10000
	BGP.community: (35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)
	BGP.originator_id: 100.65.0.131
	BGP.cluster_list: 185.94.141.138
	BGP.large_community: (35085, 0, 35085)
"""

result_route_b = {'routes': [{'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_pa2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_fr7', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_ty8', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core02_ty8', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core02_sv10', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_wes', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_sv10', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core02_sg3', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core02_ny8', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_dc12', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_sg3', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_ny8', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_tn2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_th2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core02_tn2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core02_pa4', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core02_pa2', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core02_ams9', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_ams9', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}, {'large_community': '(35085, 0, 35085)', 'since': '2020-04-03', 'protocol': 'ipv6_core01_pa4', 'origin_asn': 35085, 'as_path': [35085], 'community': '(35085,35085) (35280,1010) (35280,2010) (35280,3010) (35280,30000) (64999,35085) (35280,10)', 'network': '2a0e:b700::/32', 'local_pref': 10000, 'next_hop': '2a05:f440::2'}]}
