# Récupérer un jeu de données et le mettre à jour grâce à git et Github

---

* [Pré-requis](#Pré-requis)
* [Introduction](#Introduction)
* [Git et Github, comment ça marche ?](#Git-et-Github-comment-ça-marche)
* [Récupérer des données grâce à Github Desktop (recommandé)](#récupérer-des-données-grâce-à-github-desktop-recommandé)
  * [Installer *Github Desktop*](#installer-Github-desktop)
  * [Cloner et mettre à jour](#cloner-et-mettre-à-jour)
* [Récupérer des données via le terminal](#récupérer-des-données-via-le-terminal)
  * [Installer *Git*](#installer-git)
  * [Cloner et mettre à jour](#cloner-et-mettre-à-jour)


## Pré-requis

Pour suivre ce tutoriel, il est nécessaire de posseder un compte Github. [Créer un compte](https://github.com/join).


## Introduction

De plus en plus d'institutions mettent leurs collections en ligne grâce au servcie d'hébergement *Github.com*.


La mise à disposition des données sur cette plateforme permet aux utilisateurs de créer une copie dite *locale* des collections (ie. sur le disque dur d'un ordinateur) et de les mettre à jour rapidement afin de prendre en compte les dernières modifications effectuées par l'institution qui les fournies.


Ce tutoriel a pour but de présenter la démarche de récupération de données disponibles sur Github à travers deux approches : la première utilisant l'application Github Desktop et la seconde nécessitant d'utiliser le terminal.


## Git et Github, comment ça marche ?

#### Fonctionnement global

Git est un outil de versionning permettant à des individus de travailler sur les mêmes documents tout en conservant les traces des modifications.

L'outil fonctionne de la manière suivante : un répertoire distant (en anglais, *repository*) est d'abord créé sur un serveur (ici, Github) et est signalé à Git comme nouveau projet. Chaque utilisateur va alors pouvoir *cloner* le répertoire du projet sur sa propre machine. Cette copie du répertoire distant est appelé *repertoire locale*.

Une fois le répertoire copié localement, des documents peuvent être ajoutés, modifiés ou supprimés. Jusque là, seul l'auteur de ces modifications peut les constater puisque ces dernières sont effectuées sur son ordinateur.

Pour partager les modifications au reste des utilisateurs, l'auteur doit dans un premier temps signaler à Git que des modifications ont été effectuées puis, dans un second temps, envoyer le contenu de son repertoire local vers le repertoire distant afin que ce dernier soit mis à jour.

Les modifications sont alors visibles sur le serveur distant, les utilisateurs peuvent demander à Git de mettre à jour localement leur répertoire.

Ce processus, même s'il peut sembler contraignant, permet aux différents participants du projet de modifier des documents sans être gêné par les modifications des autres (contrairement à une solution comme FramaPad ou Google Docs).


#### La synchronisation de répertoires

Pour synchroniser des données disponibles sur Github, nous utiliserons seulement quelques unes des étapes décrites dans le fonctionnement global. La démarche est composée de deux étapes :
1. Copie du répertoire distant vers un repertoire local,
2. Demande de mise à jour du répertoire local.


## Récupérer des données grâce à Github Desktop (recommandé)

### Installer Github Desktop
**Systèmes d'exploitation compatibles** : macOSX, Windows

À venir...


## Récupérer des données via le terminal


### Installer Git
*Note* : dans le cas où Github Desktop est déjà installé, cette étape d'installation n'est pas nécessaire.

*Systèmes d'exploitation compatibles* : macOSX, Linux, Windows

#### Linux
Ouvrez votre terminal en utilisant le raccourci *Ctrl + Alt + t* puis entrez les commandes suivantes :

> sudo apt-get update

> sudo apt-get install git-all


#### Mac
Une version de git est surement déjà installée sur votre ordinateur. Pour vérifier la présence de Git ouvrez un votre terminal en utilisant le raccourci Cmd + Space et en entrant "terminal" dans la barre de recherche. Entrez la commande suivante dans le terminal :

> git --version

Si le résultat retourné indique que Git n'est pas installé, utilisez [l'installeur](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).


#### Windows

Sous Windows, vous pouvez télécharger cet [installeur](http://git-scm.com/download/win).


### Récupérer des données disponibles sur Github

*Note : la démarche décrite ci-dessous nécessite de connaître les connaissances basique de l'utilisation d'un terminal.*

Dans ce paragraphe, nous allons récupérer la [collection du MoMA](https://github.com/MuseumofModernArt/collection) et voir comment la mettre à jour. Vous pouvez cependant appliquer ce tutoriel à un autre répertoire Github.

![alt text](https://github.com/Humanistica/ArtDesignDH/tutoriels/img/tuto_synchro_donnes_1.png)

Une fois sur la page principale du repertoire à acquérir, appuyez sur "Clone or download" et copiez le lien présent dans le pop-up.

Ensuite, ouvrez un terminal :
* Sous Linux, utilisez le raccourci *Ctrl + Alt + t*
* Sous MacOSX, utilisez le raccourci *Cmd + Space*, entrez "terminal" dans la barre de recherche puis appuyez sur la touche Entrer.
* Sous Windows, utilisez le raccourci *Win + r*, entrez "cmd" dans la zone de recherche puis appuyez sur la touche Entrer.


Grâce à la commande *cd* (*dir*, sous Windows), accédez au répertoire dans lequel vous souhaitez enregistrer les données provenant de Github.


Entrez la commande suivante pour copier localement le contenu du répertoire distant :

> git clone https://github.com/MuseumofModernArt/collection.git


Le contenu du répertoire distant est alors présent sur votre ordinateur.


### Mettre à jour localement un répertoire

Grâce à la commande *cd* (*dir*, sous Windows), accédez au repertoire précédement clôné.
Pour mettre à jour le répertoire, entrez la commande suivante :
> git pull


Le message "Already up-to-date" est affiché lorsque votre répertoire est déjà à jour. Dans le cas contraire, les modifications sont téléchargées automatiquement.
