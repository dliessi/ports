Comment installer Frescobaldi sous Mac OS X
=====

[[English](INSTALL-Frescobaldi.md), [italiano](INSTALL-Frescobaldi.it.md), [Français]{INSTALL-Frescobaldi.fr.md}]

*****
**REMARQUE IMPORTANTE**  
Si vous aviez précédemment installé Frescobaldi en suivant le [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide) de Philippe Massart ou le [Portfile repository](https://github.com/dliessi/ports) de Davide Liessi, veuillez suivre les [Instructions de migration](#migration-instructions).
*****


Table des matières
-----

* [Préparer votre système pour l'installation](#prepare-your-machine-for-the-installation)
* [Installer Frescobaldi](#install-frescobaldi)
* [Mettre à jour Frescobaldi](#upgrade-frescobaldi)
* [Instructions de migration](#migration-instructions)


Preparer votre système pour l'installation
-----

1. Installez [MacPorts](http://www.macports.org/install.php).

2. Ouvrir le Terminal et entrer les lignes suivantes.
   
   ```
   sudo port selfupdate
   sudo port upgrade outdated
   sudo port install poppler +quartz +qt4
   ```
   
   La première ligne met à jour votre installation MacPorts, la seconde met à jour vos ports, la troisième installe poppler (une dépendance de Frescobaldi) avec les variantes correctes.

3. Si vous désirez le support MIDI dans Frescobaldi
   1. entrez `sudo port install fluidsynth` dans le Terminal pour installer FluidSynth (un synthétiseur utilisant les SoundFonts)
   2. téléchargez et installez [Qsynth](http://sourceforge.net/projects/qsynth) (une interface pour FluidSynth)
   3. ouvrez Qsynth, cliquez sur “Setup...” et réglez les options suivantes:
      * onglet “MIDI”: réglez “MIDI Driver” sur “coremidi”
      * onglet “Audio”: réglez “Audio Driver” sur “coreaudio”, “Buffer Size” sur “256” et “Audio Device” sur “default”
      * onglet “Soundfonts”: “Open...” un SoundFont de votre choix (vous pouvez par exemple télécharger un SoundFont proposé sur [cette page du manuel de MuseScore manual (en anglais)](http://musescore.org/en/handbook/soundfont))


Installer Frescobaldi
-----

Choisissez un des profils suivants.

* **“Je voudrais la dernière version stable”**: entrez `sudo port install frescobaldi` dans le Terminal.  
  Pour démarrer Frescobaldi, double-cliquez sur l'application `/Applications/MacPorts/Frescobaldi.app` ou entrez `/opt/local/bin/frescobaldi` dans le Terminal.

* **“Je voudrais profiter des nouvelles fonctions et corrections de bogues”**: entrez `sudo port install frescobaldi-devel` dans le Terminal.  
  Pour démarrer Frescobaldi, double-cliquez sur l'application `/Applications/MacPorts/Frescobaldi.app` ou entrez `/opt/local/bin/frescobaldi` dans le Terminal.

* **“Je voudrais contribuer à Frescobaldi”**: entrez `sudo port install depof:frescobaldi git-core` dans le Terminal.  
  Maintenant, Git et les dépendances de Frescobaldi sont installées sur votre système; il ne vous reste qu'à cloner le [dépôt Git de Frescobaldi](https://github.com/wbsoft/frescobaldi) and commencer à y travailler!  
  **N.B.** Les dépendances de Frescobaldi ont été installées via MacPorts; vous devez donc lancer Frescobaldi en utilisant la version de Python installée par MacPorts (`/opt/local/bin/python2.7`) et non celle qui est fournie avec Mac OS X (`/usr/bin/python`).

Ce dernier type d'installation peu coexister avec l'une des deux précédentes.

frescobaldi et frescobaldi-devel peuvent être installés sur le même système, mais ne peuvent être actifs en même temps.
Si vous voulez les installer tous les deux, installez un des deux, désactivez le avec `sudo port deactivate frescobaldi(-devel)` puis installez l'autre.
Quand vous désirez passer de l'un à l'autre, il vous suffit de désactiver la version active (vous pouvez vérifier de laquelle il s'agit avec la commande `port installed name:frescobaldi`) et activer l'autre (`sudo port activate frescobaldi(-devel)`).

Si vous voulez que Frescobaldi puisse jouer du MIDI, vous devez démarrer Qsynth et sélectionner le port MIDI correspondant dans les réglages de Frescobaldi.
Le port correct est automatiquement sélectionné si vous lancez Qsynth avant Frescobaldi.


Mettre à jour Frescobaldi
-----

Quand vous désirez mettre à jour Frescobaldi(ou, de façon générale, votre installation MacPorts), entrez dans le Terminal

```
sudo port selfupdate
sudo port upgrade outdated
```

La première ligne met à jour Macports lui-même ainsi que le dépôt de Portfile, la seconde met à jour les ports "périmés".
Avant d'entrer la seconde ligne, vous pouvez obtenir la liste des ports "périmés"" avec `port outdated`.


Instructions de migration
-----

Vous avez déjà installé Frescobaldi en suivant le [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide) de Philippe Massart ou le [Portfile repository](https://github.com/dliessi/ports) de Davide Liessi?
Dans ce cas, vous pouvez ignorer la section [Préparer votre système pour l'installation](#prepare-your-machine-for-the-installation) et continuer avec l'une des sections suivantes.

Les réglages de Frescobaldi seront conservés malgré le processus de migration.
Cependant, ils peuvent devenir inaccessible à *l'anciennent installation* si vous ne l'avez pas mise à jour dernièrement, suite à une modification dans la gestion des réglages de Frescobaldi.

### Migrer depuis une installation basée sur le “Frescobaldi Mac OS X install guide” de Philippe Massart

Suivez les instructions de la section [Installer Frescobaldi](#install-frescobaldi) à une différence près: vous devez insérer `-f` entre `sudo port` et `install` dans la commande choisie (ex.:  `sudo port install frescobaldi` devient `sudo port -f install frescobaldi`).

Le dossier `/Applications/frescobaldi` et le lanceur généré par Platypus ne devraient pas interférer avec la nouvelle configuration, mais vous pouvez les effacer pour éviter toute confusion.

### Migrer depuis une installation basée sur le dépôt Portfile de Davide Liessi

Suite à plusieurs modifications dans les Portfiles soumis à MacPorts, vous devrez désinstaller et ré-installer py-python-poppler-qt4 et frescobaldi(-devel).

1. Entrez `sudo port uninstall installed and \( name:frescobaldi name:python-poppler-qt4 \)` dans le Terminal.

2. Ouvrez le ficheir `sources.conf` dans votre éditeur de texte favori; j'utilise nano dans l'exemple suivant.
   1. Entrez `sudo nano /opt/local/etc/macports/sources.conf` dans le Terminal.
   2. Effacez la ligne commençant par `file://` que vous aviez précédemment insérée (dans une installation MacPorts classique, c'est la seule ligne commençant par `file://` dans ce fichier).
   3. Enregistrez le fichier et quitter l'éditeur (si vous utilisez nano: ctrl-O pour enregistrer, enter pour confirmer le nom de fichier, ctrl-X pour quitter).

3. Vous pouvez supprimer le dossier du dépôt Portfile, bien qu'il n'interfère pas avec l'installation.

4. Suivez les instructions dans la section [Installer Frescobaldi](#install-frescobaldi).
