# Enviro+ Web-Server

# Enviro+

Designed for environmental monitoring, Enviro+ lets you measure air quality (pollutant gases and particulates), temperature, pressure, humidity, light, and noise level. Learn more - https://shop.pimoroni.com/products/enviro-plus


[![Build Status](https://travis-ci.com/pimoroni/enviroplus-python.svg?branch=master)](https://travis-ci.com/pimoroni/enviroplus-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/enviroplus-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/enviroplus-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/enviroplus.svg)](https://pypi.python.org/pypi/enviroplus)
[![Python Versions](https://img.shields.io/pypi/pyversions/enviroplus.svg)](https://pypi.python.org/pypi/enviroplus)

# Installing

You're best using the "One-line" install method if you want all of the UART serial configuration for the PMS5003 particulate matter sensor to run automatically.

**Note** The code in this repository supports both the Enviro+ and Enviro Mini boards. _The Enviro Mini board does not have the Gas sensor or the breakout for the PM sensor._

:warning: This library now supports Python 3 only, Python 2 is EOL - https://www.python.org/doc/sunset-python-2/

## One-line (Installs from GitHub)

```
curl -sSL https://get.pimoroni.com/enviroplus | bash
```

**Note** report issues with one-line installer here: https://github.com/pimoroni/get

## Or... Install and configure dependencies from GitHub:

* `git clone https://github.com/pimoroni/enviroplus-python`
* `cd enviroplus-python`
* `sudo ./install.sh`

**Note** Raspbian Lite users may first need to install git: `sudo apt install git`

# Web-Server

1. Install Flask
```pip3 install Flask``` 
2. Clone this repo to your computer. 
``` git clone https://github.com/dpasut/enviroplus_webserver.git```
3. Determine where flask is installed.
```which flask```
4. Using the output from the previous step, run the web server with the flask path replaced with your own.
 ```FLASK_APP=webserver.py /usr/bin/flask run --host=0.0.0.0``` 

