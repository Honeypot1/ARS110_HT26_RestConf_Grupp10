from interfaces import put_this, get_this


routrar = [
    ("192.168.99.11", 1, "192.168.12.1", "LAN mot STO och GBG"),  # ISP
    ("192.168.99.12", 1, "192.168.12.2", "LAN mot ISP och GBG"),  # STO
    ("192.168.99.13", 1, "192.168.12.3", "LAN mot ISP och STO"),  # GBG
]

for host, port, ip, description in routrar:
    put_this(host, port, ip, "255.255.255.0", description, password)



for host, port in routrar:
    get_this(host, port)
