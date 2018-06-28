# Corpus Peintre décédés à Paris
## Corpus prêt à l’emploi pour le cours d’introduction de 9h.

Ce corpus comprend **1274 résultats de peintres décédés à Paris** avec les variables suivantes :
* Nom du peintre
* Lieu de naissance
* Coordonnées géographiques du lieu de naissance
* Image ou portrait du peintre
* Image de signature du peintre
* Lieu de sépulture
* Cause de décès du peintre
* Lieu de sépulture
* Date de décès

Ce corpus est issu de Wikidata avec la requête suivante effectuée le 18 juin 2018 :

````sparql
SELECT
  ?artist ?artistLabel
  ?birthPlaceLabel ?coordsBP
  ?pic
  ?causeLabel
  ?signat
  ?plBurialLabel ?plBurialCoords
  ?deathDate

WHERE {
  ?artist wdt:P106 wd:Q1028181 ;
          wdt:P20 wd:Q90 .
  #?artist wdt:P21 wd:Q6581097 .
  ?artist wdt:P570 ?deathDate .
  ?artist wdt:P19 ?birthPlace .
  ?birthPlace wdt:P625 ?coordsBP .
  ?artist wdt:P18 ?pic .
  OPTIONAL { ?artist wdt:P509 ?cause }
  OPTIONAL { ?artist wdt:P109 ?signat }
  OPTIONAL { ?artist wdt:P119 ?plBurial .
             ?plBurial wdt:P625 ?plBurialCoords .

           }

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}

````
Dû à la gestion d’accents, le fichier CSV a été généré depuis Google Sheets à partir du CSV téléchargé de Wikidata.

Les colonnes correspondant à des coordonnées géographiques ont été traités et renommées pour que le CSV soit directement utilisable dans Palladio. Il permet notamment de représenter une carte des peintres, par exemple.

L'utilisateur pourra repérer des cellules vides dans le corpus. Ceci est dû à des manques d'information sur Wikidata. En contexte pédagogique, cette situation peut s'utiliser pour inviter les étudiants à compléter les informations directement sur Wikidata ou pour qu’ils s’entraînent à filtrer des cellules vides sur Open Refine.
