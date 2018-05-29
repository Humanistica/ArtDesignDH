# Quelques trucs utiles pour les cours du CNAM de 2018

## Wikidata

### A garder
* Adresse d'un élément wikidata (Q??) : https://www.wikidata.org/wiki/Q354396
* Adresse d'une propriété wikidata (P??) :https://www.wikidata.org/wiki/Property:P571
* Adresse pour réaliser des requêtes SPARQL : https://query.wikidata.org/
* SPARQLEndpoint pour wikidata https://query.wikidata.org/bigdata/namespace/wdq/sparql

### Quelques exemples de requêtes SPARQL

#### Lister uniquement l'id de éléments des oeuvres de Klimt
````sparql
SELECT *
WHERE
{
  ?item wdt:P31 wd:Q3305213 .
  ?item wdt:P170 wd:Q34661 .
}
````
#### Afficher sous forme de grille d'images toutes les oeuvres attribuées au Caravage
````sparql
#defaultView:ImageGrid
SELECT DISTINCT ?item ?itemLabel (YEAR(?date) AS ?year) ?dimensions ?locationLabel ?countryLabel ?image WHERE {
  { ?item wdt:P170 wd:Q42207 . } UNION { ?item wdt:P1773 wd:Q42207 }
  OPTIONAL { ?item p:P276 ?statement . ?statement ps:P276 ?location . FILTER NOT EXISTS { ?statement pq:P582 ?x } OPTIONAL { ?location wdt:P17 ?country } }
  OPTIONAL { ?item wdt:P18 ?image }
  OPTIONAL { ?item wdt:P2048 ?length }
  OPTIONAL { ?item wdt:P2049 ?width }
  OPTIONAL { ?item wdt:P571 ?date }
  BIND (CONCAT(STR(?length),"×",STR(?width)) AS ?dimensions)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
} ORDER BY ?itemLabel
````

#### Afficher sous forme de liste toutes les céramiques grecques du Metropolitan Museum pour lesquelles la base AGORHA possède des informations de provenance.

````sparql
	select DISTINCT ?item ?itemLabel ?img ?idAgorha
	where {
		?item wdt:P31/wdt:P279* wd:Q738680 . # pottery of ancient Greece
		?item wdt:P18 ?img.    
	    ?item wdt:P276 wd:Q160236.
	  ?item wdt:P2344 ?idAgorha.

	  SERVICE wikibase:label {
	bd:serviceParam wikibase:language "fr,en"}
	}
````

#### Afficher sous la forme d'une timeline, les propriétaires des céramiques grecques du MET 

````sparql
	#defaultView:Timeline
	select DISTINCT ?item ?itemLabel ?eventLabel ?img ?proprietairesLabel ?datedebut ?datefin
	where {
		?item wdt:P31/wdt:P279* wd:Q738680 . # pottery of ancient Greece
		?item wdt:P18 ?img.    
	    ?item wdt:P276 wd:Q160236.
	    ?item p:P127 ?declaration_proprietaires.
	    ?declaration_proprietaires ps:P127 ?proprietaires.
	    OPTIONAL 
		{?declaration_proprietaires pq:P580 ?datedebut.
		FILTER(!(STRSTARTS(?datedebut, 't')))}
	    OPTIONAL 
		{?declaration_proprietaires pq:P582 ?datefin.
		FILTER(!(STRSTARTS(?datefin, 't')))}

	  SERVICE wikibase:label {
	bd:serviceParam wikibase:language "fr,en"}
	}
````
#### Afficher sous forme de carte toutes les sculptures publiques dans Paris

````sparql
#defaultView:Map
SELECT DISTINCT ?item  ?Titre ?createur (year(?date) as ?AnneeCreation) ?image ?coord 
WHERE {
   ?item wdt:P31/wdt:P279* wd:Q860861.                    # sculpture
   ?item wdt:P136 wd:Q557141 .                            # genre : art public
   {?item wdt:P131 wd:Q90.}                               # ... située dans Paris
   UNION
   {?item wdt:P131 ?arr.                                  # ... ou dans un arrondissement de Paris  
   ?arr wdt:P131 wd:Q90. } 
   ?item rdfs:label ?Titre filter (lang(?Titre) = "fr").  # Titre
  
   OPTIONAL {?item wdt:P170 ?Qcreateur.                   # créateur/créatrice (option)
   ?Qcreateur rdfs:label ?createur filter (lang(?createur) = "fr") .}
   OPTIONAL {?item wdt:P571 ?date.}                       # date de création (option)
   OPTIONAL {?item wdt:P18  ?image.}                      # image (option)
   OPTIONAL {?item wdt:P625 ?coord.}                      # coordonnées géographiques (option)
}
````

#### Qui fête son anniversaire aujourd'hui
````sparql
#Qui fête son anniversaire aujourd'hui ?
#Whose birthday is today?
SELECT ?entityLabel (YEAR(?date) as ?year)
WHERE
{
    BIND(MONTH(NOW()) AS ?nowMonth)
    BIND(DAY(NOW()) AS ?nowDay)

    ?entity wdt:P569 ?date .
    FILTER (MONTH(?date) = ?nowMonth && DAY(?date) = ?nowDay)
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "en" .
    }
}
LIMIT 10
````
#### Classement général des causes de décès sous forme de BubbleChart

````sparql
#Classement général des causes de décès
#defaultView:BubbleChart
#TEMPLATE={"template":"Overall causes of death ranking of ?thing ","variables":{"?thing": {"query":"SELECT ?id  (COUNT(?id) AS ?count) WHERE {  ?sub wdt:P509 ?y.  ?sub wdt:P31 ?id. } GROUP BY ?id "} } }
SELECT ?cid ?cause (COUNT(*) AS ?count) WHERE {
  BIND(wd:Q5 AS ?thing)
  ?pid wdt:P31 ?thing;
      wdt:P509 ?cid.
SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". ?cid rdfs:label ?cause}
}
GROUP BY ?cid ?cause
ORDER BY DESC(?count) ?cause
````
#### Nombre de films par an et par genre sous forme d'un scatterplot avec animation

````sparql
#Nombre de films par an et par genre
#defaultView:ScatterChart
SELECT   ?year  (COUNT(?_genre) AS ?count ) (SAMPLE(?_genreLabel) AS ?label )  (?year as ?year_shown) WHERE {
  ?item wdt:P31 wd:Q11424.
  ?item wdt:P577 ?_publication_date.
  ?item wdt:P136 ?_genre.
  ?_genre rdfs:label ?_genreLabel.
  BIND(str(YEAR(?_publication_date)) AS ?year)
  FILTER((LANG(?_genreLabel)) = "en")
 
 FILTER (?_publication_date >= "2000-00-00T00:00:00Z"^^xsd:dateTime)
}
GROUP BY ?_genreLabel ?year
HAVING (?count > 30)
````


#### Évolution du nombre d'œuvres par "Genre" entre 1500-1600. 
````sparql
#defaultView:BarChart 
SELECT   ?year  (COUNT(?_genre) AS ?count ) (SAMPLE(?_genreLabel) AS ?label )  (?year as ?year_shown) WHERE {
  ?item wdt:P31 wd:Q3305213.
  ?item wdt:P170 ?creator.
  ?item wdt:P571 ?_creation_date.
  ?item wdt:P136 ?_genre.
  ?_genre rdfs:label ?_genreLabel.
  BIND(str(YEAR(?_creation_date)) AS ?year)
  FILTER((LANG(?_genreLabel)) = "fr")
  
 FILTER (?_creation_date >= "1500-00-00T00:00:00Z"^^xsd:dateTime)
 FILTER (?_creation_date <= "1600-00-00T00:00:00Z"^^xsd:dateTime)
}
GROUP BY ?_genreLabel ?year
HAVING (?count > 1)
````

#### Récupérer la géoloc des villes de naissance et de décès des peintres actifs au XVIe 
````
http://tinyurl.com/ybrcyhb8
````

#### Afficher les lieux de découverte et les lieux de conservation des objets trouvés lors de fouilles archéologiques
````sparql
#defaultView:Map
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
#### Afficher sur une carte, les villes en France dont le nom se termine par "ette"

````sparql
#defaultView:Map
SELECT ?item ?itemLabel ?coord WHERE {
  ?item (wdt:P31/wdt:P279*) wd:Q486972.
  ?item wdt:P17 wd:Q142.
  ?item rdfs:label ?itemLabel.
  ?item wdt:P625 ?coord.
  FILTER((LANG(?itemLabel)) = "fr")
  FILTER(REGEX(?itemLabel, "(ette)$"))
}
````

