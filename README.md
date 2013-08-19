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

**N.B.** py-python-poppler-qt4 depends on poppler with variants qt4 and quartz.
You should `port install poppler +qt4 +quartz` before installing frescobaldi or frescobaldi-devel.
