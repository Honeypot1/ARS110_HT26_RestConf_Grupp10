import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_this(host, port, password):
    url = f"https://{host}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F{port}"
    svar = requests.get(url, auth=("admin", password), verify=False)
    print(svar.text)
    
def put_this(host, port, ip, netmask, description, password):
    headers = {"Content-Type": "application/yang-data+json"}
    url = f"https://{host}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F{port}"
    payload = {
        "ietf-interfaces:interface": {
            "name": f"GigabitEthernet0/0/{port}",
            "description": description,
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": ip, "netmask": netmask}]
            },
            "ietf-ip:ipv6": {}
        }
    }
    svar = requests.put(url, json=payload, headers=headers,
                        auth=("admin", password), verify=False)
    print(svar.status_code, svar.text)