import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def set_ospf(host, router_id, networks, password):
    headers = {"Content-Type": "application/yang-data+json"}
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


def set_default_route(host, interface, password):
    headers = {"Content-Type": "application/yang-data+json"}
    url = (f"https://{host}/restconf/data/ietf-routing:routing/routing-instance=default/"
           "routing-protocols/routing-protocol=static,1/static-routes/ietf-ipv4-unicast-routing:ipv4")
    payload = {
        "ietf-ipv4-unicast-routing:route": [{
            "destination-prefix": "0.0.0.0/0",
            "next-hop": {"outgoing-interface": interface}
        }]
    }

    svar = requests.post(url,
                            json=payload,
                            headers=headers,
                            auth=("admin", password),
                            verify=False)
    print(svar.status_code, svar.text)


def set_if_ospf(host, port, settings, password):
    headers = {"Content-Type": "application/yang-data+json"}
    url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=0%2F0%2F{port}"
    payload = {
        "Cisco-IOS-XE-native:GigabitEthernet": {
            "name": f"0/0/{port}",
            "ip": {
                "Cisco-IOS-XE-ospf:router-ospf": {
                    "ospf": settings
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
