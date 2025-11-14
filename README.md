================================================================================
README.txt - Infrastructure Docker : Flask + MariaDB + Nginx Reverse Proxy
================================================================================

DESCRIPTION
===========
3 conteneurs Docker :
- db    : MariaDB
- app   : Flask (Python) qui lit la base
- proxy : Nginx (reverse proxy)

2 réseaux :
- backend_net  : app + db + proxy
- frontend_net : proxy seul

SECURITE
========
- MariaDB : pas de port ouvert → impossible depuis l'hôte
- Flask    : pas de port ouvert → inaccessible directement
- Accès    : uniquement via http://localhost:8080 (Nginx)

DOSSIERS
========
docker-infra/
├── docker-compose.yml
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── proxy/
    ├── nginx.conf
    └── Dockerfile

LANCEMENT
=========
cd docker-infra
docker-compose up -d

Accès : http://localhost:8080

TEST
====
curl http://localhost:8080
→ Affiche : "App fonctionne !" + version MariaDB

VERIF SÉCURITÉ
==============
# DB inaccessible
mysql -h localhost -u appuser -p
→ Connection refused

# App inaccessible
curl http://localhost:5000
→ Connection refused

FONCTIONNEMENT
==============
proxy (port 8080) → app (port 5000) → db (port 3306 interne)

NETTOYAGE
=========
docker-compose down        # arrête
docker-compose down -v     # supprime les données

================================================================================
