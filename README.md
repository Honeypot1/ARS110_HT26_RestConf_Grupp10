Projekt för CCNP 1. 

Automation av en skill med RESTconf från CCNA.

- main.py – konfigurerar nätverket (använder interfaces.py, ospf.py, grund.py)
- robert.py – rättar konfigurationen med GET och skriver ut OK/FEL per kontroll

Kör: python main.py, sedan python robert.py

Uppgiften kräver säker autentisering och inte användarnamn/lösenord. Vi lade flera timmar på att få certifikatbaserad autentisering mot RESTconf att fungera, men lyckades inte. Skripten använder därför användarnamn och lösenord över HTTPS med verify=False. Vi är medvetna om att det inte uppfyller kravet.
