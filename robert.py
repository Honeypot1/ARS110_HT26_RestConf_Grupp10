import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

password = "123"

ISP = "192.168.99.11"
STO = "192.168.99.12"
GBG = "192.168.99.13"

# samma som i main.py
LAN = 0
PC = 1

kontroller = [
    # host, url, det som ska finnas i svaret, vad vi kollar
    (ISP, f"restconf/data/Cisco-IOS-XE-native:native/hostname", "ISP", "ISP hostname"),
    (STO, f"restconf/data/Cisco-IOS-XE-native:native/hostname", "STO", "STO hostname"),
    # (GBG, f"restconf/data/Cisco-IOS-XE-native:native/hostname", "GBG", "GBG hostname"),

    (ISP, f"restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F{LAN}", "192.168.12.1", "ISP LAN-IP"),
    (ISP, f"restconf/data/ietf-interfaces:interfaces/interface=Loopback0", "172.16.0.1", "ISP loopback"),
    (STO, f"restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F{LAN}", "192.168.12.2", "STO LAN-IP"),
    (STO, f"restconf/data/ietf-interfaces:interfaces/interface=Loopback0", "172.17.0.1", "STO loopback"),
    # (GBG, f"restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F{LAN}", "192.168.12.3", "GBG LAN-IP"),
    # (GBG, f"restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F{PC}", "12.12.12.13", "GBG PC-IP"),
    # (GBG, f"restconf/data/ietf-interfaces:interfaces/interface=Loopback0", "172.18.0.1", "GBG loopback"),

    (ISP, f"restconf/data/Cisco-IOS-XE-native:native/router", "1.1.1.1", "ISP router-id"),
    (STO, f"restconf/data/Cisco-IOS-XE-native:native/router", "2.2.2.2", "STO router-id"),
    # (GBG, f"restconf/data/Cisco-IOS-XE-native:native/router", "3.3.3.3", "GBG router-id"),

    (ISP, f"restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F{LAN}/ip", '"priority": 0', "ISP prio 0"),
    (STO, f"restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F{LAN}/ip", '"priority": 255', "STO prio 255"),
    # (GBG, f"restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F{PC}/ip", '"cost": 14', "GBG cost 14"),

    (ISP, f"restconf/data/ietf-routing:routing", "0.0.0.0/0", "ISP default-route"),
    (ISP, f"restconf/data/Cisco-IOS-XE-native:native/router", "originate", "ISP skickar default i OSPF"),

    (STO, f"restconf/data/Cisco-IOS-XE-ospf-oper:ospf-oper-data", '"dr": "192.168.12.2"', "STO är DR"),
    (STO, f"restconf/data/ietf-routing:routing-state", "0.0.0.0/0", "STO har fått default via OSPF"),
]

for host, url, finns, text in kontroller:
    svar = requests.get(f"https://{host}/{url}",
                        headers={"Accept": "application/yang-data+json"},
                        auth=("admin", password),
                        verify=False)
    if finns in svar.text:
        print("OK ", text)
    else:
        print("FEL", text, svar.status_code)
