from interfaces import put_this, put_loopback
from ospf import set_ospf, set_default, set_default_route, set_if_ospf
from grund import set_hostname, save_config

password = "123"

ISP = "192.168.99.11"
STO = "192.168.99.12"
GBG = "192.168.99.13"

# mgmt sitter på Gi0/0/1 nu, flyttas till Gi0/0/0 senare: byt då LAN = 1 och PC = 0
LAN = 0
PC = 1

namn = [
    (ISP, "ISP"),
    (STO, "STO"),
    (GBG, "GBG"),
]

inter = [
    (ISP, LAN, "192.168.12.1", "255.255.255.0", "LAN mot STO och GBG"),
    (STO, LAN, "192.168.12.2", "255.255.255.0", "LAN mot ISP och GBG"),
    (GBG, LAN, "192.168.12.3", "255.255.255.0", "LAN mot ISP och STO"),
    (GBG, PC, "12.12.12.13", "255.255.255.252", "Mot PC"),
]

loopbacks = [
    (ISP, "172.16.0.1", "255.255.0.0", "Internet"),
    (STO, "172.17.0.1", "255.255.0.0", "STO loopback"),
    (GBG, "172.18.0.1", "255.255.0.0", "GBG loopback"),
]

ospfSettings = [
    (ISP, "1.1.1.1", [
        {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
        {"ip": "172.16.0.0", "wildcard": "0.0.255.255", "area": 0},
    ]),
    (STO, "2.2.2.2", [
        {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
        {"ip": "172.17.0.0", "wildcard": "0.0.255.255", "area": 0},
    ]),
     (GBG, "3.3.3.3", [
         {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
         {"ip": "172.18.0.0", "wildcard": "0.0.255.255", "area": 0},
         {"ip": "12.12.12.12", "wildcard": "0.0.0.3", "area": 0},
     ]),
]

ifOspf = [
    (ISP, LAN, {"priority": 0}),    # aldrig DR/BDR
    (STO, LAN, {"priority": 255}),  # DR
    (GBG, PC, {"cost": 14}),       # länk mot PC
]

for host, hostname in namn:
    set_hostname(host, hostname, password)

for host, port, ip, netmask, description in inter:
    put_this(host, port, ip, netmask, description, password)

for host, ip, netmask, description in loopbacks:
    put_loopback(host, ip, netmask, description, password)

for host, router_id, networks in ospfSettings:
    set_ospf(host, router_id, networks, password)

for host, port, settings in ifOspf:
    set_if_ospf(host, port, settings, password)

set_default_route(ISP, "Loopback0", password)
set_default(ISP, password)

for host, hostname in namn:
    save_config(host, password)
