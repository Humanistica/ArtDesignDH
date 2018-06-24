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

### Formaliser sa question pour la transformer en requête :

**Quelles informations/champs est-ce que je veux récupérer (zone “afficher”) ?**

La démarche de SPARQL consiste à poser des filtres successifs qui permettent de trier les éléments dans WD. Il faut donc formaliser ce que l’on cherche à obtenir.

> Exemple 1 : je veux obtenir un corpus composés des vases grecs qui sont conservés au Metropolitan Museum de New York pour lesquels une image est disponible

Pour formalisation de la question : on peut se dire que :

> Je veux afficher :
* le nom
* l’image

> pour tous les éléments de WD
* qui sont des vases grecs antiques
* et
  * qui sont conservés au MET
  * qui ont une image

Avec l’assistant :

* Créer un filtre. Un filtre est composé de **deux champs** : **une propriété** et **la valeur de cette propriété**. Pour remplir ces deux champs, WD propose un moteur de remplissage automatique.

En passant la souris sur le champ, une fenêtre pop-up donne une définition pour aider à bien choisir la propriété.

![Alt Text](./img/tuto_wikidata_assistant_requete.gif)
