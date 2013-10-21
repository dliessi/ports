Come installare Frescobaldi in Mac OS X
=====

[[English](INSTALL-Frescobaldi.md), [italiano](INSTALL-Frescobaldi.it.md)]

*****
**NOTA IMPORTANTE**  
Se in precedenza hai installato Frescobaldi seguendo la guida [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide) di Philippe Massart o usando il [repository di Portfile](https://github.com/dliessi/ports) di Davide Liessi, leggi le [Istruzioni per la migrazione](#istruzioni-per-la-migrazione).
*****


Indice
-----

* [Prepara la tua macchina per l’installazione](#prepara-la-tua-macchina-per-linstallazione)
* [Installa Frescobaldi](#installa-frescobaldi)
* [Aggiorna Frescobaldi](#aggiorna-frescobaldi)
* [Istruzioni per la migrazione](#istruzioni-per-la-migrazione)


Prepara la tua macchina per l’installazione
-----

1. Installa [MacPorts](http://www.macports.org/install.php).

2. Apri il Terminale e inserisci le righe seguenti.
   
   ```
   sudo port selfupdate
   sudo port upgrade outdated
   sudo port install poppler +quartz +qt4
   ```
   
   La prima riga aggiorna la tua installazione di MacPorts, la seconda aggiorna i port installati, la terza installa poppler (una dipendenza di Frescobaldi) con le varianti corrette.

3. Se vuoi il supporto MIDI in Frescobaldi
   1. inserisci `sudo port install fluidsynth` nel Terminale per installare FluidSynth (un sintetizzatore basato su SoundFont)
   2. scarica e installa [Qsynth](http://sourceforge.net/projects/qsynth) (un’interfaccia grafica per FluidSynth)
   3. apri Qsynth, clicca su “Setup...” e imposta le opzioni seguenti:
      * scheda “MIDI”: imposta “MIDI Driver” a “coremidi”
      * scheda “Audio”: imposta “Audio Driver” a “coreaudio”, “Buffer Size” a “256” e “Audio Device” a “default”
      * scheda “Soundfonts”: clicca su “Open...” e seleziona un SoundFont a tua scelta (es. puoi scaricare uno di quelli elencati in [questa pagina del manuale di MuseScore](http://musescore.org/it/manuale/librerie-di-suoni))


Installa Frescobaldi
-----

Scegli uno dei casi seguenti.

* **“Voglio l’ultima versione stabile rilasciata”**: inserisci `sudo port install frescobaldi` nel Terminale.  
  Per avviare Frescobaldi clicca due volte sull’applicazione `/Applications/MacPorts/Frescobaldi.app` o inserisci `/opt/local/bin/frescobaldi` nel Terminale.

* **“Voglio le nuove funzionalità e le correzioni degli errori”**: inserisci `sudo port install frescobaldi-devel` nel Terminale.  
  Per avviare Frescobaldi clicca due volte sull’applicazione `/Applications/MacPorts/Frescobaldi.app` o inserisci `/opt/local/bin/frescobaldi` nel Terminale.

* **“Voglio contribuire allo sviluppo di Frescobaldi”**: inserisci `sudo port install depof:frescobaldi git-core` nel Terminale.  
  Ora Git e le dipendenze di Frescobaldi sono installati nel tuo sistema, perciò ti basta solo clonare il [repository Git di Frescobaldi](https://github.com/wbsoft/frescobaldi) e iniziare a lavorarci!
  **N.B.** Le dipendenze di Frescobaldi sono state installate attraverso MacPorts, quindi per eseguire Frescobaldi devi usare la versione di Python installata da MacPorts (`/opt/local/bin/python2.7`) e non quella di Mac OS X (`/usr/bin/python`).

L’ultimo tipo di installazione può coesistere con ciascuna delle prime due.

frescobaldi e frescobaldi-devel possono essere installati nello stesso sistema, ma non possono essere attivi nello stesso momento.
Se vuoi installarli entrambi, inizia con uno dei due, poi disattivalo con `sudo port deactivate frescobaldi(-devel)` e quindi installa l’altro.
Quando vuoi passare da uno all'altro, ti basta disattivare la versione attualmente attiva (puoi sapere qual è con `port installed name:frescobaldi`) e attivare l’altra (`sudo port activate frescobaldi(-devel)`).

Se vuoi che la riproduzione MIDI in Frescobaldi funzioni, Qsynth deve essere avviato e devi scegliere la porta MIDI corretta nelle preferenze di Frescobaldi.
La porta corretta è scelta automaticamente se avvii Qsynth prima di avviare Frescobaldi.


Aggiorna Frescobaldi
-----

Quando vuoi aggiornare Frescobaldi (o, in generale le tue installazioni di MacPorts), inserisci nel Terminale

```
sudo port selfupdate
sudo port upgrade outdated
```

La prima riga aggiorna MacPorts stesso e il repository dei Portfile, la seconda aggiorna i port per cui è disponibile un aggiornamento.
Prima di inserire la seconda riga, puoi vedere quali aggiornamenti sono disponibili con il comando `port outdated`.


Istruzioni per la migrazione
-----

Hai già installato Frescobaldi seguendo la guida [Frescobaldi Mac OS X install guide](https://github.com/wbsoft/frescobaldi/wiki/Frescobaldi-Mac-OS-X-install-guide) di Philippe Massart o usando il [repository di Portfile](https://github.com/dliessi/ports) di Davide Liessi?
Allora puoi ignorare il capitolo [Prepara la tua macchina per l’installazione](#prepara-la-tua-macchina-per-linstallazione) e continuare con uno dei paragrafi seguenti.

Le preferenze di Frescobaldi saranno preservate nel processo di migrazione.
Potrebbero comunque diventare inaccessibili *alla vecchia installazione*, se non avevi aggiornato Frescobaldi recentemente, a causa di un cambiamento nella gestione delle preferenze.

### Migrazione da un’installazione basata sulla guida “Frescobaldi Mac OS X install guide” di Philippe Massart

Segui le istruzioni in [Installa Frescobaldi](#installa-frescobaldi) con un’unica differenza: devi inserire `-f` tra `sudo port` e `install` nel comando prescelto (es. `sudo port install frescobaldi` diventa `sudo port -f install frescobaldi`).

La cartella `/Applications/frescobaldi` e l’applicazione generata con Platypus non dovrebbero interferire con la nuova installazione, ma puoi cancellarle per evitare di confonderti.

### Migrazione da un’installazione basata sul repository di Portfile di Davide Liessi

A causa di un paio di cambiamenti nei Portfile inviati a MacPorts, è necessario disinstallare e reinstallare py-python-poppler-qt4 e frescobaldi(-devel).

1. Inserisci `sudo port uninstall name:frescobaldi name:python-poppler-qt4` nel Terminale.

2. Apri il file `sources.conf` nel tuo editor di testo preferito; userò nano come esempio.
   1. Inserisci `sudo nano /opt/local/etc/macports/sources.conf` nel Terminale.
   2. Cancella la riga che inizia con `file://` che avevi inserito in precedenza (in un’installazione tipica di MacPorts sarà l’unica riga iniziante pre `file://` in quel file).
   3. Salva il file e esci dall’editor (se usi nano: ctrl-O per salvare, invio per confermare il nome del file, ctrl-X per uscire).

3. Puoi cancellare la cartella del repository dei Portfile, anche se non interferisce con l’installazione.

4. Segui le istruzioni in [Installa Frescobaldi](#installa-frescobaldi).
