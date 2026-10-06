import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_this(host, name, password):
    url = f"https://{host}/restconf/data/ietf-interfaces:interfaces/interface={name.replace('/', '%2F')}"
    svar = requests.get(url, 
                    auth=("admin", password), 
                    verify=False)
    print(svar.text)

def put_this(host, name, ip, netmask, description, password):
    headers = {"Content-Type": "application/yang-data+json"}
    url = f"https://{host}/restconf/data/ietf-interfaces:interfaces/interface={name.replace('/', '%2F')}"
    typ = "iana-if-type:softwareLoopback" if name.startswith("Loopback") else "iana-if-type:ethernetCsmacd"
    payload = {
        "ietf-interfaces:interface": {
            "name": name,
            "description": description,
            "type": typ,
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": ip, "netmask": netmask}]
            },
            "ietf-ip:ipv6": {}
        }
    }
    svar = requests.put(url,
                    json=payload,
                    headers=headers,
                    auth=("admin", password),
                    verify=False)
    print(svar.status_code, svar.text)
