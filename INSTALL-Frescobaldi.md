How to install Frescobaldi on Mac OS X
=====

*****
**IMPORTANT NOTE**  
If you had a previous installation of Frescobaldi that you installed either following Philippe Massart’s [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide) or using Davide Liessi’s [Portfile repository](https://github.com/dliessi/ports), please read the [Migration instructions](#migration-instructions).
*****


Table of contents
-----

* [Prepare your machine for the installation](#prepare-your-machine-for-the-installation)
* [Install Frescobaldi](#install-frescobaldi)
* [Upgrade Frescobaldi](#upgrade-frescobaldi)
* [Migration instructions](#migration-instructions)


Prepare your machine for the installation
-----

1. Install [MacPorts](http://www.macports.org/install.php).

2. Open the Terminal and enter the following lines.
   
   ```
   sudo port selfupdate
   sudo port upgrade outdated
   sudo port install poppler +quartz +qt4
   ```
   
   The first line updates your MacPorts installation, the second upgrades your ports, the third installs poppler (a dependency of Frescobaldi) with the correct variants.

3. If you want MIDI support in Frescobaldi
   1. enter `sudo port install fluidsynth` in the Terminal to install FluidSynth (a SoundFont-based synthesizer)
   2. download and install [Qsynth](http://sourceforge.net/projects/qsynth) (a GUI for FluidSynth)
   3. open Qsynth, click on “Setup...” and set the following options:
      * “MIDI” tab: set “MIDI Driver” to “coremidi”
      * “Audio” tab: set “Audio Driver” to “coreaudio”, “Buffer Size” to “256” and “Audio Device” to “default”
      * “Soundfonts” tab: “Open...” a SoundFont at your choice (e.g. you can download one of those listed in [this page from MuseScore’s manual](http://musescore.org/en/handbook/soundfont))


Install Frescobaldi
-----

Choose one of the following cases.

* **“I want the latest stable released version”**: enter `sudo port install frescobaldi` in the Terminal.  
  To launch Frescobaldi double click the application bundle `/Applications/MacPorts/Frescobaldi.app` or enter `/opt/local/bin/frescobaldi` in the Terminal.

* **“I want the new features and bug fixes”**: enter `sudo port install frescobaldi-devel` in the Terminal.  
  To launch Frescobaldi double click the application bundle `/Applications/MacPorts/Frescobaldi.app` or enter `/opt/local/bin/frescobaldi` in the Terminal.

* **“I want to contribute to Frescobaldi”**: enter `sudo port install depof:frescobaldi git-core` in the Terminal.  
  Now you have Git and the dependencies of Frescobaldi installed in your system, so you just need to clone the [Git repository of Frescobaldi](https://github.com/wbsoft/frescobaldi) and start working on it!  
  **N.B.** The dependencies of Frescobaldi were installed through MacPorts, so you must run Frescobaldi using the Python installation provided by MacPorts (`/opt/local/bin/python2.7`) and not the one provided by Mac OS X (`/usr/bin/python`).

The last kind of installation can coexist with either of the first two.

frescobaldi and frescobaldi-devel can be installed on the same system, but they cannot be active at the same time.
If you want to install both of them, start with one, then deactivate it with `sudo port deactivate frescobaldi(-devel)` and then install the other.
When you want to switch between the two versions, you just need to deactivate the currently active version (you can see which one is active with `port installed name:frescobaldi`) and activate the other (`sudo port activate frescobaldi(-devel)`).

If you want a working MIDI playback in Frescobaldi, you must have Qsynth running and you must select the correct MIDI port in Frescobaldi’s settings.
The correct port is automatically selected if you launch Qsynth before Frescobaldi.


Upgrade Frescobaldi
-----

When you want to upgrade Frescobaldi (or, in general, your MacPorts installations), enter in the Terminal

```
sudo port selfupdate
sudo port upgrade outdated
```

The first line updates MacPorts itself and the Portfile repository, the second upgrades the outdated ports.
Before entering the second line, you can inspect the list of the outdated ports with `port outdated`.


Migration instructions
-----

Have you already installed Frescobaldi following Philippe Massart’s [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide) or using Davide Liessi’s [Portfile repository](https://github.com/dliessi/ports)?
Then you can ignore the section [Prepare your machine for the installation](#prepare-your-machine-for-the-installation) and continue with one of next sections.

Frescobaldi’s settings will be preserved in the migration process.
However they may become inaccessible *to the old setup*, if you hadn’t updated recently, due to a change in Frescobaldi’s settings management.

### Migrate from an installation based on Philippe Massart’s “Frescobaldi Mac OS X install guide”

Follow the instructions in [Install Frescobaldi](#install-frescobaldi) with only one difference: you must insert `-f` between `sudo port` and `install` in the chosen command (e.g. `sudo port install frescobaldi` becomes `sudo port -f install frescobaldi`).

The directory `/Applications/frescobaldi` and the Platypus-generated application bundle shouldn’t interfere with the new setup, but you may delete them to avoid confusion.

### Migrate from an installation based on Davide Liessi’s Portfile repository

Due to a couple of changes in the Portfiles submitted to MacPorts, you will need to uninstall and reinstall py-python-poppler-qt4 and frescobaldi(-devel).

1. Enter `sudo port uninstall name:frescobaldi name:python-poppler-qt4` in the Terminal.

2. Open the `sources.conf` file in your favorite text editor; I'll use nano as an example.
   1. Enter `sudo nano /opt/local/etc/macports/sources.conf` in the Terminal.
   2. Delete the line beginning with `file://` that you previously inserted (in a typical installation of MacPorts, it will be the only line beginning with `file://` in that file).
   3. Save the file and exit the editor (if you use nano: ctrl-O to save, enter to confirm the file name, ctrl-X to exit).

3. You may delete the Portfile repository directory, even though it doesn't interfere with the installation.

4. Follow the instructions in [Install Frescobaldi](#install-frescobaldi).
