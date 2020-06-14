# Flask MVC sample project

> **This project is not ideal for any production projects whatsoever.**


> This project is simply to illustrate how MVC works under the hood. In no way
> what-so-ever that this project implies a good MVC. This project is simply made
> as a tool of teaching, nothing more, nothing less.

## Lancer le serveur web du projet

```shell
$ flask run
```

Si `flask` n'existe pas, assurer que `~/.local/bin` est dans votre `$PATH`.

## Télécharger / clone le projet

Il y a deux méthodes pour télecharger ou cloner le projet.

### Méthode 1: Télécharger l'archive

1. Taper le bouton avec l'icône télécharger qui est situé à gauche du bouton bleu
   avec le texte "Clone".
2. Choisir votre format préféré.
3. Extraire l'archive à un dossier.

### Méthode 2: Avec Git

Pour utiliser cette méthode, c'est nécessaire d'avoir Git sur votre système.

Pour cloner le projet, taper cette commande:
```shell
$ git clone https://gitlab.com/yuki_is_bored/flask_project
```

## Installation

Voir la documentation d'installation pour votre système d'éxploitation :

* [Linux](./INSTALL.linux.md)
* [Windows](./INSTALL.win.md)
* [macOS](./INSTALL.macos.md)

## Configuration

### Configuration du BDD

Ouvrir le fichier `config.py` et modifier les variables `MYSQL_HOSTNAME`,
`MYSQL_DATABASE`, `MYSQL_USERNAME` et `MYSQL_PASSWORD`.

Par exemple :

```python
MYSQL_HOSTNAME = 'balthasar.magi.nerv.gov.jp`
MYSQL_DATABASE = 'detabesu'
MYSQL_USERNAME = 'soryuu'
MYSQL_PASSWORD = 'passwort'
```
