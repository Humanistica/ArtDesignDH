# Corpus MoMa
## Méthode pour créer des sous-corpus - niveau débutant

Le MoMA met à disposition sur github 2 fichiers CSV  : la liste des artistes (nom, nationalité, date de naissance, date de mort, genre) et la liste des oeuvres acquises par le musée (une trentaine de variables).

Vous pouvez les télécharger depuis ce lien : https://github.com/MuseumofModernArt/collection

> Ces deux fichiers sont trop importants (plusieurs dizaines de millier d’objets) pour être manipulés tels quels par les étudiants. Il peut néanmoins être intéressant de fabriquer des sous-corpus en fonction des critères évoqués dans l’introduction. Ces sous-corpus peuvent être réalisés par département, par nationalité, par genre, par période, etc… Nous en donnons ici un exemple, utilisable pour le cours de 9h.


En utilisant open refine, nous avons extrait le 18 juin 2018 du corpus “oeuvres” les oeuvres correspondant aux critères suivants : département Media & Performance, Vidéo (sound, colour), oeuvres réalisées par un seul auteur, artistes de nationalité américaine. Puis nous n’avons retenu que 7 variables : titre, nom de l’artiste, genre, date de création, date d’acquisition, Url de l’oeuvre, url de la photographie de l’oeuvre.

Ce fichier peut être utilisé dans Palladio pour visionner une galerie d’oeuvre, réaliser des graphes et des histogrammes.

Le même principe peut être utilisé à partir des fichiers des collections :
* de la Tate Modern : https://github.com/tategallery/collection 
* Du Carnegie Museum of Art : https://github.com/cmoa/collection

Si vous réalisez des extractions de corpus à partir de ces jeux de données, n’hésitez pas à les partager dans ce dossier en documentant la date à laquelle le jeu de données a été réalisé, ainsi que les manipulations effectuées à partir du jeu initial.
