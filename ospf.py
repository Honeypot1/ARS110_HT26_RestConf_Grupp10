import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def set_ospf(host, router_id, password):
    headers = {"Content-Type": "application/yang-data+json"}
    #url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:router-ospf"
    url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/router"
    payload = {
        "Cisco-IOS-XE-native:router": {
            "Cisco-IOS-XE-ospf:router-ospf": {
                "ospf": {
                    "process-id": [{
                        "id": 1,
                        "router-id": router_id
                    }]
                }
            }
        }
    }

    svar = requests.patch(  url, 
                            json=payload, 
                            headers=headers,
                            auth=("admin", password), 
                            verify=False)
    print(svar.status_code, svar.text)


if __name__ == "__main__":
    password = "123"
    for host, router_id in [
        ("192.168.99.12", "2.2.2.2"),  # STO
        ("192.168.99.13", "3.3.3.3"),  # GBG
    ]:
        set_ospf(host, router_id, password)