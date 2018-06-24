## Tutoriel "pas-pas" pour créer un corpus avec wikidata
réalisé dans le cadre du workshop “fabriquer des jeux de données en art” du 28 au 30 mai 2018 à l'INHA

> **Important avant toute chose** : si on ne trouve pas dans WD tous les éléments dont on a besoin pour sa recherche, alors il convient d’enrichir les données directement dans WD !

### introduction
**Wikidata** est une base de données libre, collaborative, multilingue, et secondaire qui collecte des données structurées pour alimenter Wikipédia, Wikimedia Commons, les autres projets du mouvement Wikimédia et pour n'importe qui sur la planète.

Pour en savoir + sur wikidata, lecture hautement recommendée de https://www.wikidata.org/wiki/Wikidata:Introduction/fr

### Démarche

Se rendre sur le sparqlendpoint de Wikidata : https://query.wikidata.org/

Voici à quoi ressemble l'interface :
![Exemple de visualisation réalisé sur Palladio](./img/tuto_wikidata_1.png)

**Wikidata** propose deux modes pour rédiger des requêtes :
* via un assistant (bloc de gauche de l’écran) : formulaire, avec le libellé des concepts
* via la fenêtre de saisie classique (bloc de droite de l’écran) : requête littérale à rédiger en langage sparql

Dans tous les cas, un conseil : partir d’un exemple de requête préenregistrée *(bouton “Exemples”)*.
> NB : Il est recommandé de n’utiliser le mode assistant sur la partie gauche de la page uniquement pour des requêtes très simples, car toutes les fonctionnalités du langage SPARQL ne sont pas accessibles via les champs de l’assistant.

Deux sources pour "appréhender" les requêtes SPARQL :
* [Page web contenant des exemples de requêtes SQARQL  pour Wikidata](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples)
* [La page web tutoriel SQARQL pour un usage sur Wikidata est aussi utile](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial)
