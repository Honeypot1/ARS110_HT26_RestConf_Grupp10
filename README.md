Projekt för CCNP 1. 

Automation av en skill med RESTconf från CCNA.

- main.py – konfigurerar nätverket (använder interfaces.py, ospf.py, grund.py)
- robert.py – rättar konfigurationen med GET och skriver ut OK/FEL per kontroll

Kör: python main.py, sedan python robert.py

En sidnot
Certifikatbaserad autentisering fick vi inte att fungera under labbtiden. Skripten använder därför användarnamn och lösenord över HTTPS med verify=False. Det uppfyller inte kravet på hög säkerhet och tas även upp i rapportens diskussion.
