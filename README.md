# ms_lockout

<p align="center">
  <img align="center" src="https://raw.githubusercontent.com/pitt-makerspace/ms_lockout/master/docs/ms_lockout_logo.png" height="220" />
  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
  <img align="center" src="https://raw.githubusercontent.com/pitt-makerspace/ms_lockout/master/docs/makerspace_logo.png" width="280" />
</p>

### University of Pittsburgh makerspace lockout System.<br>
The lockout system is designed to ensure safe usage of equipment and analyze space usage to improve user experience in the makerspace.<br>

The current version of the lockout system uses Raspberry PIs to give user access to equipment in the
space by reading user IDs. This makes sure users have proper training on the equipment. When the ID is read, the Raspberry PI asks the web server if the user has access to the equipment.<br>

In this repository, required software for the lockout devices and the web server can be found with installation instructions as well as hardware setup instructions.

# Setup
- [Software](#software)
- [Hardware](#hardware)

## Software

### Enable SPI

```
sudo raspi-config
```

Select `Interfacing Options` then select `SPI` and activate.

### Install dependencies

**spidev**

```
sudo apt-get install python-spidev python3-spidev
```

**SPI-Py**

```
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
sudo python setup.py install
sudo python3 setup.py install
```

### RFC522 Package

**MFRC522-python**

```
git clone https://github.com/mxgxw/MFRC522-python.git
cd MFRC522-python
python Read.py
```

## Hardware

The lockout device consists of:
- Raspberry PI 3
- Relay
- RFID Reader
- RGB LED
- Plastic case with lock
- Outlet splitter

## Raspberry PI

### RFID Connections

|No|RF24|GPIO|Pin|
|-:|---:|---:|--:|
| 1| VCC|3.3V|  1|
| 2| RST|  25| 22|
| 3| GND| GND|  6|
| 4| IRQ|   -|  -|
| 5|MISO|   9| 21|
| 6|MOSI|  10| 19|
| 7| SCK|  11| 23|
| 8| SDK|   8| 24|

<p align="center"><img src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2018/02/rc522_rfid_raspberry_pi_wiring.png"></p>

### Relay Connections

|No|Name|GPIO|Pin|
|-:|---:|---:|--:|
| 1| GND| GND|  9|
| 2| SIG|  23| 16|

### RGB LED Connections

|No|  Name|GPIO|Pin|
|-:|-----:|---:|--:|
| 1|   Red|  17| 11|
| 2| Green|  27| 13|
| 3|  Blue|  22| 15|
| 4|   GND| GND| 14|

### Buzzer

|No|Name|GPIO|Pin|
|-:|---:|---:|--:|
| 1| GND| GND| 20|
| 2| SIG|  25| 22|
