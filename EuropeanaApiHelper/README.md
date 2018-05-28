# EuropeanaApiHelpers
Contains tools to retrieve collections from Europeana API


### Dépendances
Il est nécessaire d'avoir installé Python3 pour éxécuter ces scipts. (https://www.python.org/downloads/)


### Simple search
Pour stocker le résultat d'une requête simple dans un fichier JSON, entrez la commande suivante dans un terminal : 

```
curl "https://www.europeana.eu/api/v2/search.json?wskey=CLE_PUBLIQUE&query=REQUETE" > nom_fichier.json
```

### Cursor search
L'API Europeana utilise le cursor search pour récupérer plusieurs pages de données. Le script europeana_cursor_search.py gère automatiquement le cursor search et enregistre les données directement de un fichier csv.

Pour récolter toutes les pages d'une collection, entrez la commande suivante dans un terminal :

```
python3 europeana_cursor_search.py "https://www.europeana.eu/api/v2/search.json?wskey=CLE_PUBLIQUE&query=REQUETE" nom_fichier.csv
```

Pour garder uniquement certaine colonne du fichier .csv, il est nécessaire de créer un fichier .txt contenant les noms des colonnes à garder. Par exemple :
> *mes_colonnes.txt*
```
items_title
items_type
items_ugc
items_year
items_guid
items_id
```

Enuite, entrez la commande suivante dans votre terminal : 
```
python3 europeana_cursor_search.py "https://www.europeana.eu/api/v2/search.json?wskey=CLE_PUBLIQUE&query=REQUETE" nom_fichier.csv --col mes_colonnes.txt
```







# Python JSON to CSV converter
Convertion de fichier json vers csv depuis la ligne de commande 


Pour convertir un fichier json en fichier csv, entrez la commande suivante dans un terminal:

```
python3 JtoC.py your_file.json
```
