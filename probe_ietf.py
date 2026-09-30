import requests
import urllib3
def get_this(port):
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {"Content-Type": "application/yang-data+json"}
    url = f"https://192.168.99.11/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F{port}"
    svar = requests.get(url, auth=("admin","123"), verify=False)
    #print(svar.status_code)
    print(svar.text)


    payload = {
    "ietf-interfaces:interface": {
        "name": f"GigabitEthernet0/0/{port}",
        "description": "RESTCONF-test",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address":[
                {
                "ip":"192.168.1.1",
                "netmask": "255.255.255.0"
                }
            ]

        },
        "ietf-ip:ipv6": {
        }
    }
    }



    #svaret = requests.put(url,json=payload, headers=headers,auth=("admin", "123"), verify=False)
    wegetthis = requests.get(url,json=payload, headers=headers,auth=("admin", "123"), verify=False)
    #print(svaret)

    if "netmask" in wegetthis.text:
        print('ip finns')
    else:
        print("DAVID E CUNT")

if __name__=="__main__":
    print(wegetthis)