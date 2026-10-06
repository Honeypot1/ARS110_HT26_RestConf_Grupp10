import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def set_hostname(host, hostname, password):
    headers = {"Content-Type": "application/yang-data+json"}
    url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native/hostname"
    payload = {"Cisco-IOS-XE-native:hostname": hostname}

    svar = requests.patch(url,
                            json=payload,
                            headers=headers,
                            auth=("admin", password),
                            verify=False)
    print(svar.status_code, svar.text)


def save_config(host, password):
    url = f"https://{host}/restconf/operations/cisco-ia:save-config"
    svar = requests.post(url, auth=("admin", password), verify=False)
    print(svar.status_code, svar.text)
