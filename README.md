dliessi/ports
=====

Personal MacPorts Portfile repository


Contents
-----

* [frescobaldi](http://www.frescobaldi.org/) @2.0.10
* frescobaldi-devel @20130823
* [py-python-poppler-qt4](https://code.google.com/p/python-poppler-qt4/) @0.16.3


Usage
-----

If you want to use this repository, you may clone it, insert its path in your MacPorts installation's `sources.conf` file and construct the port index in the repository's root directory.

Let's see an example of how to do this.

Let's suppose that
* your username is `yourname`,
* your home directory (`~`) is `/Users/yourname`, and
* you have already created the directory `~/github` and you want my repository to be in the subdirectory `~/github/ports`.

1. In the Terminal
```
cd ~/github
git clone https://github.com/dliessi/ports.git
```
As an alternative, if you don't have git installed, [download the ZIP file](https://github.com/dliessi/ports/archive/master.zip), expand it, rename the expanded directory to `ports` and move it in `~/github`.  

2. Open the `sources.conf` file in your favorite text editor; I'll use nano as an example.  
In the Terminal
```
sudo nano /opt/local/etc/macports/sources.conf
```
Go after the comment lines (those that begin with `#`) and before the line(s) that begin with `rsync://` and insert the line
```
file:///Users/yourname/github/ports/
```
Then save the file and exit the editor (if you use nano: ctrl-O to save, enter to confirm the file name, ctrl-X to exit).

3. In the Terminal
```
cd ~/github/ports
portindex
```

Now your MacPorts installation should be able to see my Portfiles.

**N.B.** py-python-poppler-qt4, a dependency of frescobaldi(-devel) depends on poppler with variants qt4 and quartz.
MacPorts cannot automatically install dependencies with variants other than the default ones, so you should `port install poppler +qt4 +quartz` before installing frescobaldi(-devel) or py-python-poppler-qt4.


About [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide)
-----

Here is what changes with respect to [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide) by Philippe Massart if you enable this repository in your MacPorts installation.

### [Installing Frescobaldi and dependencies](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide#installing-frescobaldi-and-dependencies)

This part reduces to just what follows.

* Update MacPorts with `sudo port selfupdate` or update just the Portfiles with `sudo port sync`.
* Upgrade your ports with `sudo port upgrade outdated`.
* `sudo port install poppler +quartz +qt4`.
* `sudo port install frescobaldi` or `sudo port install frescobaldi-devel`.

frescobaldi(-devel) is installed as `/opt/local/bin/frescobaldi-2.7`.

### [Creating a launcher](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide#creating-a-launcher)

I never used Platypus so I cannot advise on this, but I think that it should work the same if you substitute the script with the following one.
```
#!/bin/sh
/opt/local/bin/python2.7 /opt/local/bin/frescobaldi-2.7
```

### [MIDI output](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide#midi-output)

The only difference here is that you do not need to install portmidi, since it is automatically installed as a dependency of frescobaldi(-devel).

### [Upgrading to a new version of Frescobaldi](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide#upgrading-to-a-new-version-of-frescobaldi)

I should keep these Portfiles reasonably up to date, so when there is something new you should just need to pull/fetch the repository or download the ZIP file, perform [step 3](https://github.com/dliessi/ports#usage) and `sudo port upgrade outdated`.
If time passes and I do not upgrade the Portfiles, please open a new issue [here on GitHub](https://github.com/dliessi/ports/issues).
