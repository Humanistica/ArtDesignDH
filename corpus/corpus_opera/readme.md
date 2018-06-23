# Corpus Opera
## Corpus prêt à l’emploi pour le cours d’introduction de 9h.

Ce corpus comprend **446 opéras** avec les variables suivantes :
* Titre de l’opéra
* nom du compositeur
* date de la première
* lieu de la première
* coordonnées géographiques du lieu de la première
* langue de l’opéra
* image.

Ce corpus est issu de wikidata avec la requête suivante effectuée le 18 juin 2018 :

````sparql
SELECT ?opera ?composerLabel ?operaLabel ?worldpremiere ?lieu_de_la_premi_re_repr_sentationLabel ?image ?barLabel ?langueLabel WHERE {
  ?opera (wdt:P31/wdt:P279*) wd:Q1344.
  ?opera wdt:P1191 ?worldpremiere.
  ?opera wdt:P4647 ?lieu_de_la_premi_re_repr_sentation.
  ?lieu_de_la_premi_re_repr_sentation wdt:P625 ?bar.
  ?opera wdt:P86 ?composer.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,de,fr,it,es,ru". }
  OPTIONAL { ?opera wdt:P18 ?image. }
  OPTIONAL { ?opera wdt:P407 ?langue. }
}
ORDER BY ?worldpremiere
````

Le corpus a ensuite été nettoyé avec Open Refine pour être directement utilisable dans Palladio. Il permet notamment de :
* Représenter une timeline des opéras
* Représenter géographiquement les lieux de création
* Effectuer des graphes
* Effectuer une galerie d’images (même si toutes les pièces n’ont pas d’illustration. C’est une façon de sensibiliser à l’incomplétude des données).

Les données disponibles sur le théâtre sont encore très pauvres dans wikidata. Néanmoins, un projet de versement des données est en cours. On pourra consulter utilement la page suivante pour suivre le projet : https://www.wikidata.org/wiki/Wikidata:WikiProject_Performing_arts
Dans l’onglet “tools & queries” figurent de nombreux exemples de requêtes qui peuvent servir de point de départ pour construire un corpus.
