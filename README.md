## Entretien Technique Affluences

Pour lancer l'application avec Docker (en dév):
docker compose -f docker-compose-dev.yml up -d --build

------------------------------

Format de la requête : http://127.0.0.1:5000/api/occupancy [GET]

```json
{
    "site_id": 1,
    "start_datetime": "2024-04-21 16:00:00",
    "end_datetime" : "2024-04-21 18:00:00",
    "granularity" : 1800
}
```

Format des dates : %Y-%m-%d %H:%M:%S
Granularity : en seconde

-------------------------------