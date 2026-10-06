# Varför native

Kravet var att inte göra en enda PATCH mot `native:native`. Vi använde IETF-modellerna där det gick: `ietf-interfaces` för IP och description, `ietf-routing` för default-routen.

För OSPF fanns inget fungerande standardalternativ. `ietf-ospf` tog emot vår POST (201) men skapade ingen `router ospf`. `openconfig-ospfv2` saknas på IOS-XE 16.12. Därför använde vi Cisco-native, men bara de delar som rör OSPF: `native/router` för processen och `native/interface/.../ip/router-ospf` för prio och cost. Hostname finns bara i native-modellen.

| Konfig | Modell |
|--|--|
| IP, description, loopbacks | `ietf-interfaces` |
| Default-route | `ietf-routing` |
| OSPF-process, network, router-ID, originate | `Cisco-IOS-XE-native` (`router`) |
| Prio, cost | `Cisco-IOS-XE-native` (`interface/.../ip`) |
| Hostname | `Cisco-IOS-XE-native` (`hostname`) |
| Spara | `cisco-ia` |

## Läsa och skriva OSPF

| | Utan native | Med native |
|--|--|--|
| Läsa OSPF-status (grannar, RID, areor) | `Cisco-IOS-XE-ospf-oper:ospf-oper-data` | – |
| Läsa OSPF-konfig | – | `Cisco-IOS-XE-native:native/router` |
| Skriva OSPF | `ietf-ospf` ger 201 men skapar ingenting | `Cisco-IOS-XE-native:native/router` |

## Payload från GET

Vi läste först konfigen med GET i Postman. Svaret har samma format som RESTCONF förväntar sig vid skrivning, så vi kopierade det som body och bytte ut värdena. När anropet fungerade i Postman flyttade vi payloaden till Python och ersatte värdena med variabler.

- Interface: GET `ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0` → `put_this` i `interfaces.py` (bild 09)
- OSPF: GET `Cisco-IOS-XE-native:native/router` → `set_ospf` i `ospf.py` (bild 10)

URL och payload måste börja på samma nivå. URL som slutar på `native/router` tar en payload som börjar med `Cisco-IOS-XE-native:router`. Annars svarar routern `400 missing element`.
