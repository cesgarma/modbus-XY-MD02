# modbus-XY-MD02
Modbus connection with python using a Raspberry PI -> USB -> Serial -> RS485 -> "XY-MD02" - ModBus Temperature and Humidity sensor. 

# Description
The objective is to connect a Temperature / Humidity sensor, in this case the "XY-MD02" ModBus sensor to a Raspberry PI or any other device (PC, Mac, Linux) using Python.

To keep things simple, this project is using the python library [minimalmodbus](https://minimalmodbus.readthedocs.io/en/master/index.html).

If you are using that specific sensor, then follow the installation instructions and run the main script which will simply loop to gather the temperature value and print it on the terminal every 2 seconds.

If you are using a different sensor, then reference the datasheet to figure out the ModBus Device Address and Command that you should use.

# Hardware
We are using the following hardware

* Raspberry PI 3
* USB-to-Serial
* Serial-to-RS485
* 5V DC power supply.
* "XY-MD02" ModBus Temperature sensor.

# Installation
I like to develop using python virtual environments to avoid misconfiguring your host.

## Clone this repository
```
git clone https://github.com/cesgarma/modbus-XY-MD02.git
```

## Install pyenv

### Install Dependencies
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

### Install pyenv
```
curl https://pyenv.run | bash
```

### Add pyenv to path

```
$ touch ~/.bash_aliases
$ nano ~/.bash_aliases
```

Add the following lines to the file .bash_aliases

```
export PATH="/home/pi/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Update your bash (you don’t have to reboot the terminal)

```
$ source ~/.bashrc
```

## Install python 3.7.6 with pyenv (or any other Python 3.7 version)

This will take a while. Grab some coffee.
```
$ pyenv install 3.7.6
```

## Setup python 3.7.6
To setup python 3.7.6 as global so any python command from any shell will use it just run:
```
$ pyenv global 3.7.6
```

## Install minimalmodbus
The [minimalmodbus](https://minimalmodbus.readthedocs.io/en/master/index.html) provides simple connectiviy to devices connected using ModBus. Find full documentation on their website.

```
pip install minimalmodbus
```

You are ready to go!

# Run the script
```
python tempReaderModbus.py
```