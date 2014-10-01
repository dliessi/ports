Come usare questo repository
=====

[[English](USAGE.md), [italiano](USAGE.it.md)]

Se vuoi usare questo repository, devi clonarlo, inserire il suo percorso nel file `sources.conf` della tua installazione di MacPorts e cortruire lìindice dei port nella cartella di base del repository.

Di seguito trovi le istruzioni che raccomando di seguire.

Le istruzioni presumono che tu abbia un’[installazione di MacPorts](http://www.macports.org/install.php) funzionante e che tu abbia installato Git (lo puoi installare attraverso MacPorts inserendo `sudo port install git` nel Terminale).

1. Nel Terminale inserisci
   
   ```
   sudo mkdir /opt/dliessi
   my_user=`id -un`; my_group=`id -gn`; sudo chown ${my_user}:${my_group} /opt/dliessi
   cd /opt/dliessi
   git clone https://github.com/dliessi/ports.git
   ```

2. Apri il file `sources.conf` nel tuo editor di testo preferito; userò nano come esempio.
   
   1. Inserisci `sudo nano /opt/local/etc/macports/sources.conf` nel Terminale.
   2. Spostati dopo le righe di commento (quelle che iniziano con `#`) e prima delle righe che iniziano con `rsync://` e inserisci la riga `file:///opt/dliessi/ports/`.
   3. Salva il file ed esci dall’editor (se usi nano: ctrl-O per salvare, invio per confermare il nome del file, ctrl-X per uscire).

3. Nel Terminale inserisci
   
   ```
   cd /opt/dliessi/ports
   portindex
   ```

Ora la tua installazione di MacPorts dovrebbe essere in grado di vedere i miei Portfile.


Aggiornamento
-----

Per aggiornare le tue installazioni di MacPorts:
* per prima cosa aggiorna il repository dei Portfile; nel Terminale inserisci
  ```
  cd /opt/dliessi/ports
  git pull
  portindex
  ```

* quindi aggiorna MacPorts normalmente, con `sudo port selfupdate` seguito da `sudo port upgrade outdated`.
