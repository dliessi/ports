dliessi/ports
=====

Personal MacPorts Portfile repository

**N.B.** Branches other than `master` can be subject to **history rewriting**, so use them at your own risk.


Table of contents
-----

* [Available Portfiles](#available-portfiles)
* [How to use this repository](#how-to-use-this-repository)
* [How to install Frescobaldi](#how-to-install-frescobaldi)


Available Portfiles
-----

* [frescobaldi](http://www.frescobaldi.org/) @2.0.11
* frescobaldi-devel @20131016 (identical to frescobaldi 2.0.11)
* [py-python-poppler-qt4](https://code.google.com/p/python-poppler-qt4/) @0.16.3


How to use this repository
-----

If you want to use this repository, you may clone it, insert its path in your MacPorts installation's `sources.conf` file and construct the port index in the repository's root directory.

Here is what I recommend.

Let's assume that you have a working [MacPorts installation](http://www.macports.org/install.php) and that you have git installed (you can install it through MacPorts entering `sudo port install git-core` in the Terminal).

1. In the Terminal
```
sudo mkdir /opt/dliessi
cd /opt/dliessi
sudo git clone https://github.com/dliessi/ports.git
```

2. Open the `sources.conf` file in your favorite text editor; I'll use nano as an example.  
In the Terminal
```
sudo nano /opt/local/etc/macports/sources.conf
```
Go after the comment lines (those that begin with `#`) and before the line(s) that begin with `rsync://` and insert the line
```
file:///opt/dliessi/ports/
```
Then save the file and exit the editor (if you use nano: ctrl-O to save, enter to confirm the file name, ctrl-X to exit).

3. In the Terminal
```
cd /opt/dliessi/ports
sudo portindex
```

Now your MacPorts installation should be able to see my Portfiles.

**N.B.** py-python-poppler-qt4, a dependency of frescobaldi(-devel) depends on poppler with variants qt4 and quartz.
MacPorts cannot automatically install dependencies with variants other than the default ones, so you should `port install poppler +qt4 +quartz` before installing frescobaldi(-devel) or py-python-poppler-qt4.

### Upgrade

I should keep these Portfiles reasonably up to date, so when there is something new you should just need to
* `sudo git pull` in the repository directory,
* perform step 3 (`sudo portindex`), and
* `sudo port upgrade outdated`.

If time passes and I do not upgrade the Portfiles, please open a new issue [here on GitHub](https://github.com/dliessi/ports/issues).


How to install Frescobaldi
-----

### Install Frescobaldi

* Install [MacPorts](http://www.macports.org/install.php).
* Prepare MacPorts to use this repository as described [above](#how-to-use-this-repository).
* If you already had MacPorts installed, in the Terminal
 + `sudo port selfupdate` to update MacPorts or `sudo port sync` to just update the Portfiles;
 + `sudo port upgrade outdated` to upgrade your ports.
* In the Terminal, `sudo port install poppler +quartz +qt4` to install poppler (dependency of py-python-poppler-qt4) with the correct variants.
* In the Terminal,
 + if you want latest stable version: `sudo port install frescobaldi`;
 + if you want latest development version: `sudo port install frescobaldi-devel`
* frescobaldi(-devel) is installed as `/opt/local/bin/frescobaldi-2.7`; both frescobaldi and frescobaldi-devel include an application bundle that is installed as `/Applications/MacPorts/Frescobaldi.app`.

**N.B.** If you had previously installed Frescobaldi following Philippe Massart's [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide), you may get an error about existing files not belonging to registered ports when MacPorts tries to activate py27-python-poppler-qt4 or frescobaldi(-devel).
In order to solve this problem, launch the installation command again with the `-f` (force) option, i.e. `sudo port -f install frescobaldi(-devel)`.

### MIDI output

Follow the [relevant section](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide#midi-output) of Philippe Massart's [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide), with the only difference that you do not need to install portmidi, since it is automatically installed as a dependency of frescobaldi(-devel).
