## Tutoriel "pas-pas" pour utiliser (et comprendre) Palladio en utilisant les données de Wikidata
réalisé dans le cadre du workshop “fabriquer des jeux de données en art” du 28 au 30 mai 2018 à l'INHA

### Objectifs :
> * réaliser une reqûete wikidata pour créer un corpus comportant différentes variables et types de données (libellé, date, lieux géolocalisés).
> * jouer cette requête dans Palladio et utiliser les différences facettes de l'application

![Exemple de visualisation réalisé sur Palladio](/img/tuto_wikidata_palladion_1.png)
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

### Dans Palladio
1. Aller dans Palladio http://hdlab.stanford.edu/palladio-app/#/upload
2. cliquer sur Load data from a SPARQL endpoint (beta)
3. Dans le champs ````SPARQL endpoint````, mettre ````https://query.wikidata.org/bigdata/namespace/wdq/sparql````
4. Dans la fenêtre, il faut écrire la requête wikidata

### Arrêtons-nous sur la requête wikidata

Voici à quoi resemblera la requête finale :

````sparql
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
SELECT distinct ?Objet ?ObjetLabel ?LieuDecouverteLabel ?coord (CONCAT(STR(?lat),", ",STR(?long)) as ?lat_long) ?LieuConservationLabel ?coord2 (CONCAT(STR(?lat2),", ",STR(?long2)) as ?lat_long2)
WHERE {
?Objet wdt:P31/wdt:P279* wd:Q15792060.
?Objet wdt:P189 ?LieuDecouverte.
?LieuDecouverte wdt:P625 ?coord.
?LieuDecouverte p:P625 ?declaration.
?declaration psv:P625 ?coord_geo.
?coord_geo wikibase:geoLatitude ?lat.
?coord_geo wikibase:geoLongitude ?long.
?Objet wdt:P195 ?LieuConservation.
?LieuConservation wdt:P625 ?coord2.
?LieuConservation p:P625 ?declaration2.
?declaration2 psv:P625 ?coord_geo2.
?coord_geo2 wikibase:geoLatitude ?lat2.
?coord_geo2 wikibase:geoLongitude ?long2.
SERVICE wikibase:label {
bd:serviceParam wikibase:language "fr,en"}
}
````
#### Découpons la requête pour la détailler :

* Les préfixes précisent les namespaces qui seront utiliser dans la requête, ce qui permet ensuite d'utiliser wdt: sans répéter l'url du modèle à chaque.
````sparql
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
````

* Le ````Select```` permet de lister les éléments que l'on souhaite afficher :
````sparql
SELECT distinct ?Objet ?ObjetLabel ?LieuDecouverteLabel ?coord (CONCAT(STR(?lat),", ",STR(?long)) as ?lat_long) ?LieuConservationLabel ?coord2 (CONCAT(STR(?lat2),", ",STR(?long2)) as ?lat_long2)
````
   * 2 points d'attention à regarder
      * Les variables ````?.....Label```` permet d'afficher les labels grâce au service qui sera appelé dans la requête via
  ````bd:serviceParam wikibase:language "fr,en"}````
      * Palladio **exigent que les informations de géolocalisation soit dans une même et unique cellule (lattitude, longitude)**. Pour cela, il faut donc créer dans la requête ce champs de manière dynamique grâce à ````sparql
      (CONCAT(STR(?lat),", ",STR(?long)) as ?lat_long)````

* Le ````WHERE```` permet de rédiger la requête en tant que tel

````sparql
{
?Objet wdt:P31/wdt:P279* wd:Q15792060. #Prendre tous les items de type objets archéologiques. L'étoile est utilisée pour prendre toutes les sous-classes
?Objet wdt:P189 ?LieuDecouverte.
?LieuDecouverte wdt:P625 ?coord.
?LieuDecouverte p:P625 ?declaration.
?declaration psv:P625 ?coord_geo.
?coord_geo wikibase:geoLatitude ?lat.
?coord_geo wikibase:geoLongitude ?long.
?Objet wdt:P195 ?LieuConservation.
?LieuConservation wdt:P625 ?coord2.
?LieuConservation p:P625 ?declaration2.
?declaration2 psv:P625 ?coord_geo2.
?coord_geo2 wikibase:geoLatitude ?lat2.
?coord_geo2 wikibase:geoLongitude ?long2.
}
````
