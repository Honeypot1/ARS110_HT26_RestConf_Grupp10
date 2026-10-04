from interfaces import put_this, get_this

password = "123"

inter = [
    ("192.168.99.11", 1, "192.168.12.1", "LAN mot STO och GBG"),  # ISP
    ("192.168.99.12", 1, "192.168.12.2", "LAN mot ISP och GBG"),  # STO
    ("192.168.99.13", 1, "192.168.12.3", "LAN mot ISP och STO"),  # GBG
]

ospfSettings = [
        # ISP
        ("192.168.99.11", "1.1.1.1", [
            {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
            {"ip": "172.16.0.0", "wildcard": "0.0.255.255", "area": 0},
        ]),  
        # STO
        ("192.168.99.12", "2.2.2.2", [
            {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
            {"ip": "172.17.0.0", "wildcard": "0.0.255.255", "area": 0},
        ]),
        # GBG  
        ("192.168.99.13", "3.3.3.3", [
            {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
            {"ip": "172.18.0.0", "wildcard": "0.0.255.255", "area": 0},
            {"ip": "12.12.12.12", "wildcard": "0.0.0.3", "area": 0},
        ]),  
    ]
for host, port, ip, description in inter:
    put_this(host, port, ip, "255.255.255.0", description, password)



