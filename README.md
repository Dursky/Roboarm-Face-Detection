# Roboarm-Face-Detection

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

### [PL]
Wykrywanie twarzy odbywa się dzięki oprogramowaniu OpenCV![2]()
Pozostałe użyte technologie:
  - I2C
  - Serwomechanizmy
  - Czujniki na podczerwień
  

### Instalacja

```sh
$ git clone https://github.com/Dursky/Roboarm-Face-Detection.git
$ cd Roboarm-Face-Detection
$ python3 main.py
```
### Podłączenie

By podłaczyć poprawnie silniki serwo do Raspberry Pi, używamy pinów GPIO.
```sh
[17]GPIO -- Serwo osi X
[2]GPIO -- Serwo osi Y
```



### EN

Face detection is done with OpenCV![2]() software.
Other technologies used:
  - I2C
  - Servomechanisms
  - infrared sensors

### Installation

```sh
$ git clone https://github.com/Dursky/Roboarm-Face-Detection.git
$ cd Roboarm-Face-Detection
$ python3 main.py
```

### Podłączenie

To properly connect the servo motors to the Raspberry Pi, we use the GPIO pins.
```sh
[17]GPIO -- Servo X-Axis
[2]GPIO -- Servo Y-Axis
```