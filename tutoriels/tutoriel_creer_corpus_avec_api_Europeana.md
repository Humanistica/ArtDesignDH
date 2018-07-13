# Créer un corpus avec l'API d'Europeana

*Réalisé dans le cadre du workshop “fabriquer des jeux de données en art” du 28 au 30 mai 2018 à l'INHA.*


## Table des matières

* [Introduction](#introduction)
* [Demandez votre clé publique](#demandez-votre-clé-publique)
* [Les APIs REST](#les-apis-rest)
  * [Explications](#explications)
  * [Exemple de décomposition d'une requête](#exemple-de-décomposition-d-une-requête)
  * [Construire une requête](#construire-une-requête)
  * [Les curseurs](#les-curseurs)
* [Europeana Search](#europeana-search)
  * [Pourquoi une application web?](#pourquoi-une-application-web)
  * [Guide d'utilisation](#guide-d-utilisation)
  * [Nous aider](#nous-aider)


## Introduction

Europeana est un agrégateur de données muséales et permet ainsi à de nombreux musées de partager leurs collections.

Europeana propose [plusieurs API](https://pro.europeana.eu/resources/apis) (Application Programing Interface) afin de requêter sa base. Ici, il est montré comment utiliser l'[API de recherche](https://pro.europeana.eu/resources/apis/search) d'Europeana dans le but de constituer des corpus destinés à l'enseignement.

Les APIs sont des interfaces permettant à deux systèmes différents de communiquer entre eux. Au cours de ce tutoriel, l'API d'Europeana se trouve être l'interface entre l'utilisateur demandeur de données et la base de données  d'Europeana. En envoyant une requête correctement formulée à l'API, cette dernière va transmettre la demande de l'utilisateur à la base d'Europena qui prendra soin de renvoyer les résultats correspondant aux critères de recherche.

La première partie du tutoriel permet de présenter, dans les grandes lignes, le fonctionnement des APIs REST et comment elles peuvent être utilisées, notamment dans le cas d'Europeana. La seconde partie du tutoriel présente l'application web [Europeana Search](https://europeana-search.herokuapp.com/) permettant d'utiliser l'API d'Europeana grâce à une interface simple développée dans le cadre du workshop “fabriquer des jeux de données en art”.



## Demandez votre clé publique

Si ce n'est pas encore fait, demandez votre clé d'authentification à l'addresse suivante : https://pro.europeana.eu/get-api . Cette clé permet d'utiliser les API d'Europeana.

**Il est nécessaire d'avoir une clé publique pour suivre ce tutoriel jusqu'au bout.**


## Les APIs REST

### Explications

Les APIs sont des interfaces permettant à deux systèmes différents de communiquer entre eux. Dans le cas étudié au cours de ce tutoriel, l'API d'Europeana se trouve être l'interface entre l'utilisateur demandeur de données et la base de données  d'Europeana. En envoyant une requête correctement formulée à l'API, cette dernière va transmettre la demande de l'utilisateur à la base d'Europena qui prendra soin de renvoyer les résultats correspondant aux critères de recherche.

Plus particulièrement, les APIs REST (*REpresentational State Transfer*) permettent de formuler des demandes sous formes de requêtes HTTP. Généralement, ces requêtes sont composées de deux membres distincts : 1. l'addresse de l'API  et 2. des champs comportant les paramètres de recherche de la requête.

*Note :* les APIs disponibles sur le web fonctionnent globalement de la même manière. Il cependant nécessaire de se référer à la documentation proposée par l'institution pour y trouver toutes les informations concernant l'utilisation de son API

*Note* : l'utilisation des APIs ne permet en aucun cas d'accéder à la totalité des données présentes sur une base de données. Autrement dit, certaines données présentes sur la base d'une institution, comme par exemple la provenance d'un objet ou le nom d'un donateur, ne seront pas rendues accessibles via une API si la dite institution décide de garder ces données privées.

### Exemple de décomposition d'une requête

Par exemple dans la requête suivante :
> https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query="Mona+Lisa"

Le premier membre "*https://www.europeana.eu/api/v2/search.json*" indique que nous souhaitons utiliser l'API search d'europeana.

Le second membre " *?wskey=xxxx&query="Mona+Lisa"* " correspond aux paramètres de la recherche. En décomposant ce membre de la requête, on trouve les paramètres suivants :

* " *wskey=xxxx* " - Ici, le nom du paramètre est *wskey* est la valeur attribuée est "*xxxx*". Dans le cas d'Europeana, il correspond à une clé d'authentification,
* " *query="Mona+Lisa"* " - Ici, le nom du paramètre est "*query*" et la valeur attribuée est "*Mona+Lisa*". Ce paramètre correspond aux filtres de la recherche.

*Note :* les paramètres de la recherche sont séparés par des "&".

### Construire une requête

Cette partie du tutoriel s'appuie sur la [documentation de l'API](https://pro.europeana.eu/resources/apis/search) de recherche fournie par Europeana.

Comme vu dans le paragraphe [Exemple de décomposition d'une requête](#exemple-de-décomposition-d-une-requête), une requête est composée de deux membre distincts. Le premier est invariant et correspond à l'adresse de l'API à utiliser. Le second membre contient deux paramètres : la clé d'authentification (contenu dans le champs *wskey*) et le paramètre de recherche (contenu dans le champs *query*).

Voici donc la base de la requête :
> https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=

Il est nécessaire de remplacer "*xxxx*" par votre clé publique. Le champs *query* est pour le moment vide : c'est ce paramètre qui nous permettra d'énoncer des critères de recherche.


Plusieurs critères de recherche sont applicables :
* par mots-clés,
* par date,
* par zone géographique.

Le principe de construction de requête étant globalement le même pour tous les critères, seuls les critères par mot-clés et par date seront traités en guise d'exemple.


##### Recherches par mots-clés

Lors d'une recherche par mots-clés, il est nécessaire de "traduire" au format HTTP la liste des mots-clés : par exemple, pour effectuer une recherche portant sur les mots *Mona* et *Lisa*, nous écrirons : query="Mona+Lisa". Ici, la liste des mots est mise entre guillemets et les espaces sont remplacés par des signes "*+*".

Pour d'affiner la recherche, il est possible d'ajouter des opérateurs logiques : "*AND*", "*OR*" ou "*NOT*" :

* *query=mona+AND+lisa* - indique que l'on recherche les objets qui ont dans leurs mots-clés "*mona*" **et** "*lisa*",
* *query=mona+OR+lisa* - indique que l'on cherche les objets qui ont dans leurs mots-clés soit "*mona*", soit "*lisa*", soit les deux,
* *query=mona+NOT+lisa* - indique que l'on cherche les objets qui le mot "*mona*" dans leurs mot-clés mais pas "*lisa*".

Notons qu'il est aussi possible d'effectuer des recherches par auteur en ajoutant le préfixe "*who*" au contenu de la requête :
> https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=who:"Leonardo+da+Vinci"

Autres exemples de requête :
> https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=mona+NOT+lisa

> https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=jacques+dutronc

##### Recherches par dates

Les recherches par dates s'effectuent grâce au préfixe *timestamp_created*. Les dates doivent être mises au format aaaa-mm-jj. Pour utiliser les deux exemples suivants, il faudra veiller à remplacer les dates par vos propres valeurs.

Pour effectuer une recherche sur une date précise :
>https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=timestamp_created:"2013-03-16T20:26:27.168Z"

Pour effectuer une recherche sur une période :
>https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=timestamp_created:[2013-11-01T00:00:0.000Z+TO+2013-12-01T00:00:00.000Z]



##### Combiner les deux critères de recherche

Il est possible de combiner des recherches grâce au nouveau paramètre "*qf*".

Par exemple, pour faire une recherche avec les mots clés "*jacques*" et "*dutronc*" en affinant avec une période de création des objets allant du 01/11/1970 au 01/12/2013:
> https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=jacques+dutronc&qf=timestamp_created:[1970-11-01T00:00:0.000Z+TO+2013-12-01T00:00:00.000Z]

##### Deux manières d'exécuter la recherche

Une fois la requête construite (en veillant à correctement insérer sa clé publique et les critères de recherche), elle peut être exécutée soit dans un navigateur internet, soit dans un terminal (OSX ou Linux) à l'aide de la commande *curl*.

Pour exécuter la requête dans une navigateur, il suffit de la copier dans une barre de recherche qui pour accéder à une page web. Là, le résultat de la requête est affiché. Il est alors possible de télécharger les fichiers au format *json*.

Pour exécuter la commande dans un terminal, il est possible en utilisant la commande *curl* de directement enregistrer le résultatd de la commande dans un fichier json en entrant la commande suivante :
> curl https://www.europeana.eu/api/v2/search.json?wskey=MA_CLÉ&query=MA_REQUETE > mon_fichier.json


### Les curseurs

Le nombre de résultats d'une recherche est limité à 100. Pour récupérer tous les résultats d'une recherche dont le nombre d'items serait > à 100, il est nécessaire d'utiliser le système de pagination de l'API.

Il faut alors ajouter le paramètre *rows* à nos requêtes. Puisque le nombre de résultats retourné est limité à 100 il faudra effectuer plusieurs de requêtes en prenant soin de mettre à jour le paramètre rows qui indique à l'API quelle "page" nous voulons récupérer. (On considère qu'une "page" contient au plus 100 résultats : si une réponse comporte 1200 objets, on peut dire qu'elle a 12 pages).

La première requête a effectuée comporte donc le paramètre *rows* qui contient la valeur "\*". Par exemple :
> https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=mona+lisa&rows=*

Le résultat de cette requête contient un champs "Next cursor". La valeur de ce champs doit remplacer l'actuelle valeur du champs "*rows*" dans notre requête. Si la valeur du nouveau curseur est AewfjdpJlljdfkg, la prochaine requête à effectuer sera la suivante :

> https://www.europeana.eu/api/v2/search.json?wskey=xxxx&query=mona+lisa&rows=AewfjdpJlljdfkg


Et ainsi de suite, jusqu'à ce que l'API n'est plus de résultats à retourner.



## Europeana search

Ce paragraphe présente l'API Europeana Search développée par [William Diakité](https://twitter.com/WilliamDiakite) dans le cadre du workshop “fabriquer des jeux de données en art” du 28 au 30 mai 2018 à l'INHA.


Le répertoire de l'application est disponible à cette adresse : https://github.com/WilliamDiakite/EuropeanaAPIHelpers .


### Pourquoi une application web ?

Cette application a été réalisée afin de faciliter la création de corpus via l'API de recherche d'Europeana. En effet, la taille de ce tutoriel et le besoin de produire des interfaces simples d'utilisation témoigne d'un problème rencontré par de nombreux.euses chercheur.e.s : celui des collections disponibles sous réserve de savoir utiliser une API...


### Guide d'utilisation

Cette application nécessite d'avoir une clé publique.

Le champs "Mots-Clés" doit impérativement être complété. Les autres champs peuvent être laissé vide ou être complété.

### Nous aider

L'application est encore sous sa version Alpha, de nombreux bugs sont encore présents.

Aidez-nous à déveloper cette application en demandant un accès au [répertoire de l'appication](https://github.com/WilliamDiakite/EuropeanaAPIHelpers) !
