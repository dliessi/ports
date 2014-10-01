How to use this repository
=====

[[English](USAGE.md), [italiano](USAGE.it.md)]

If you want to use this repository, you may clone it, insert its path in your MacPorts installation's `sources.conf` file and construct the port index in the repository's root directory.

Here is what I recommend.

Let's assume that you have a working [MacPorts installation](http://www.macports.org/install.php) and that you have Git installed (you can install it through MacPorts entering `sudo port install git` in the Terminal).

1. In the Terminal enter
   
   ```
   sudo mkdir /opt/dliessi
   my_user=`id -un`; my_group=`id -gn`; sudo chown ${my_user}:${my_group} /opt/dliessi
   cd /opt/dliessi
   git clone https://github.com/dliessi/ports.git
   ```

2. Open the `sources.conf` file in your favorite text editor; I'll use nano as an example.
   
   1. Enter `sudo nano /opt/local/etc/macports/sources.conf` in the Terminal.
   2. Go after the comment lines (those that begin with `#`) and before the line(s) that begin with `rsync://` and insert the line `file:///opt/dliessi/ports/`.
   3. Save the file and exit the editor (if you use nano: ctrl-O to save, enter to confirm the file name, ctrl-X to exit).

3. In the Terminal enter
   
   ```
   cd /opt/dliessi/ports
   portindex
   ```

Now your MacPorts installation should be able to see my Portfiles.


Upgrade
-----

To upgrade your MacPorts installations:
* first upgrade the Portfile repository; in the Terminal enter
  ```
  cd /opt/dliessi/ports
  git pull
  portindex
  ```

* then upgrade MacPorts as usual, with `sudo port selfupdate`, and then `sudo port upgrade outdated`.
