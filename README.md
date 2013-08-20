dliessi/ports
=====

Personal MacPorts Portfile repository


Contents
-----

* [frescobaldi](http://www.frescobaldi.org/) @2.0.10
* frescobaldi-devel @20130818
* [py-python-poppler-qt4](https://code.google.com/p/python-poppler-qt4/) @0.16.3


Usage
-----

If you want to use this repository, you may

1. clone this repository (`git clone https://github.com/dliessi/ports.git`) or [download the ZIP file](https://github.com/dliessi/ports/archive/master.zip) and expand it;
2. insert the line `file:///path/to/repository` (where `/path/to/repository` is the full path to the repository) in `/opt/local/etc/macports/sources.conf`;  
(MacPorts finds Portfiles in the order specified in `sources.conf`, so you may want to insert the line before other repositories.)
3. in Terminal, `cd` to the repository and execute `portindex`.

Now you should be able to use the Portfiles provided in this repository.

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
