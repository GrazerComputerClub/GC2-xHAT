# GC2-xHAT
Raspberry Pi Zero Extended HAT PCB

## Features

 - 7-Segment Display - 4-Digits TM1637 (Proprietary 2-Wire Bus)
 - Sensors
	 - DHT11/DHT22/AM2302 (Proprietary 1-Wire Bus) - Humidity & Temperature
	 - AMD2320/AMD2322 (I2C Bus) - Humidity & Temperature
	 - DS18B20 (1-Wire Bus) - Temperature
	 - HC-SR04 (Proprietary Interface) - Distance
 - Traffic Light 
	 - LED red (GPIO16, Active High, Default off)
	 - LED yellow/orange (GPIO20, Active High, Default off)
	 - LED green (GPIO21, Active High, Default off)
 - Switches 
 	 - S1 (GPIO13, Active High, Default Low)
	 - S2 (GPIO19, Active High, Default Low)
	 - S3 (GPIO21, Active High, Default Low)
 - Buzzer 
 - ATmega 328P Programming/Testing
 - ESP-01 (ESP8266) Programming/Testing
 - Power Switch for ATmega and ESP-01
 	GPIO5, Active Low, Default off 
 - HAT EEPROM (I2C Bus)
 	I2C0, A0-A2 Low

![PCB Top](https://github.com/GrazerComputerClub/GC2-xHAT/raw/master/GC2-xHATv1.0.png)

