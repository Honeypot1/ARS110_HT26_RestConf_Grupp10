import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def set_ospf(host, router_id, networks, password):
    headers = {"Content-Type": "application/yang-data+json"}
    #url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"
    url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/router"
    payload = {
        "Cisco-IOS-XE-native:router": {
            "Cisco-IOS-XE-ospf:router-ospf": {
                "ospf": {
                    "process-id": [{
                        "id": 1,
                        "router-id": router_id,
                        "network": networks
                    }]
                }
            }
        }
    }

    svar = requests.patch(url,
                            json=payload,
                            headers=headers,
                            auth=("admin", password),
                            verify=False)
    print(svar.status_code, svar.text)


def set_default(host, password):
    headers = {"Content-Type": "application/yang-data+json"}
    url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/router"
    payload = {
        "Cisco-IOS-XE-native:router": {
            "Cisco-IOS-XE-ospf:router-ospf": {
                "ospf": {
                    "process-id": [{
                        "id": 1,
                        "default-information": {"originate": {}}
                    }]
                }
            }
        }
    }

    svar = requests.patch(url,
                            json=payload,
                            headers=headers,
                            auth=("admin", password),
                            verify=False)
    print(svar.status_code, svar.text)

def set_if_ospf(host, port, settings, password):
    headers = {"Content-Type": "application/yang-data+json"}
    url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F{port}"
    payload = {
            }



if __name__ == "__main__":
    password = "123"
    for host, router_id, networks in [
        ("192.168.99.11", "1.1.1.1", [
            {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
            {"ip": "172.16.0.0", "wildcard": "0.0.255.255", "area": 0},
        ]),  # ISP
        ("192.168.99.12", "2.2.2.2", [
            {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
            {"ip": "172.17.0.0", "wildcard": "0.0.255.255", "area": 0},
        ]),  # STO
        ("192.168.99.13", "3.3.3.3", [
            {"ip": "192.168.12.0", "wildcard": "0.0.0.255", "area": 0},
            {"ip": "172.18.0.0", "wildcard": "0.0.255.255", "area": 0},
            {"ip": "12.12.12.12", "wildcard": "0.0.0.3", "area": 0},
        ]),  # GBG
    ]:
    
        set_ospf(host, router_id, networks, password)

    set_default("192.168.99.11", password)  # ISP