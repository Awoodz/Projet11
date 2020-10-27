# Qu'est ce que c'est ?
Cette application vous permets de rechercher des aliments et de leur trouver des substituts plus sain. Vous pourrez sauvegarder des substituts afin de les retrouver plus facilement !
Cette version dispose d'une nouvelle fonctionnalité : il est désormais possible de filtrer les résultats d'une recherche ou les produits sauvegardés par nutriscore.

# Le contexte
Ce programme est une amélioration d'un projet précédent dans le cadre d'une formation d'OpenClassrooms. Le but étant de corriger des bugs, d'ajouter une fonctionnalité, de créer des tests adéquats et de s'entretenir avec le client.

# Comment l'utiliser ?

### Sur votre ordinateur :
  * Téléchargez le repository et décompressez le au chemin de votre choix
  * Assurez vous d'avoir une version récente de Python ( https://www.python.org/downloads/release )(programme developpé sous Python 3.8)
  * Installez les modules contenus dans le requirements.txt
  * Créez une variable d'environnement qui contiendra votre clé secrète. Nommez la "PUR_BEURRE_KEY".
  * Téléchargez et installez Postgresql
  * Créez une base de donnée nommée "pur_beurre" encodé en utf8 ( ```createdb -E utf8 pur_beurre``` ) ou bien changez le paramètre NAME de la base de donnée dans le fichier settings.py
  * Créez un utilisateur "root" ( ```createuser --superuser root``` ) ou bien changez le paramètre USER de la base de donnée dans le fichier settings.py
  * Assurez vous que le port utilisé par postgresql soit le port 5432, autrement, changez le paramètre PORT de la base de donnée dans le fichier settings.py
  * Une fois votre serveur de base de donnée lancé, effectuez les migrations ( ```./manage.py migrate``` )
  * Afin de remplir la base de donnée, lancez la commande suivante : ```./manage.py dtb_builder```
  * Enfin, executez la commande ```./manage.py runserver``` puis ouvrez votre navigateur web à l'adresse indiquée dans le terminal