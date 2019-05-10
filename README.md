# GC2-xHAT
Raspberry Pi Zero Extended HAT for Raspjamming and other Events

## Features

- **7-Segment Display** - 4-Digits TM1637 (Proprietary 2-Wire Bus)  
  CLK  ... GPIO23  
  DIO  ... GPIO24   
- **Sensors**
	 - DHT11/DHT22/AM2302 (Proprietary 1-Wire Bus) - Humidity & Temperature (GPIO22, External Pull-up)
	 - AMD2320/AMD2322 (I2C Bus) - Humidity & Temperature
	 - DS18B20 (1-Wire Bus) - Temperature (GPIO04, External Pull-up)
	 - HC-SR04 (Proprietary Interface) - Distance  
             TRIGGER ... GPIO17  
             ECHO ... GPIO27 (External 5V to 3V divider for input)  
- **Traffic Light** 
	 - LED red (GPIO16, Active High, Default off)
	 - LED yellow/orange (GPIO20, Active High, Default off)
	 - LED green (GPIO21, Active High, Default off)
- **Switches** 
 	 - S1 (GPIO13, Active High, Default Low)
	 - S2 (GPIO19, Active High, Default Low)
	 - S3 (GPIO26, Active High, Default Low)
- **Buzzer** (GPIO18, Active High, Default off) 
- **ATmega 328P Sockel** Programming/Testing  
  RESET ... GPIO25 (Active Low, Default Low with no Power, Default High with Power)  
  MOSI  ... GPIO10  
  MISO  ... GPIO09  
  SCK   ... GPIO11  
- **ESP-01 Sockel** (ESP8266) Programming/Testing  
  RST   ... GPIO06 (Active Low, Default High)  
  GPIO0 ... GPIO12 (High ... Programming, Low ... Flash-Boot, Default Low)  
  TXD   ... GPIO14  
  RXD   ... GPIO15  
- Power Switch for ATmega and ESP-01 (GPIO05, Active Low, Default off)
- HAT EEPROM (I2C Bus)  
	 I2C0, A0-A2 Low

![PCB Top](https://github.com/GrazerComputerClub/GC2-xHAT/raw/master/GC2-xHATv1.0.png)

![Circuit diagram](https://github.com/GrazerComputerClub/GC2-xHAT/raw/master/circuit_diagram.png)

![GC2-xHAT](https://github.com/GrazerComputerClub/GC2-xHAT/raw/master/GC2-xHAT.jpg)


## Components list
	
10 x Resistor 470 o. 1K  (LED*: R3, R4, R13, R14 ; Protect: R8, R9, R10, R15, R16, R17)  
 4 x Resistor 4K7 (5V->3V: R1 ; Pull-up: R6, R7 ; Transistor base: R11)  
 1 x Resistor 6K8 (5V->3V: R2)  
 1 x Resistor 47K (Green LED: R5*)  
 3 x Tactile switch 6x6mm (S1, S2, S3)  
 1 x LED red 3mm (LR)  
 1 x LED yellow/orange 3mm (LY)  
 1 x LED green 3mm (YG)  
 1 x LED blue 3mm (LB)  
 1 x LED pink 3mm (LP)  
 1 x Transistor BC547B (T1)  
 1 x Female pin header socket 2x4 (SV2)  
 1 x Female pin header socket 1x4 (U$3)  
 1 x Female pin header socket 2x20 (SV1)  
 1 x 28-Pin DIP-Socket o. 28-Pin ZIF-Socket (0.3''/7.62mm Narrow)  
 1 x DHT11 o. DHT22 o. AM2302 (U$2)  
 1 x AM2322 o. AM2320  (U$4 / U$1)  
 1 x DS18B20 (IC1) 
 1 x TM1637 4 Digi LED display modul (GND, VCC, DIO, CLK)  
 1 x Buzzer (O 12mm, 7.2mm holes) (SG3)  
 1 x FET IRLML6401 (Q1)  
 1 x EEPROM STM M24C64-WMN6 (24C64)  
 2 x SMD 1206 resistor 3K9 (R18, R19)  
 1 x Capacity 100nF (C1)  
 2 x Spacer M2.5  
 2 x Bolt M2.5

\* Please choose LED resistor corresponding to LED type and 3.3 V, usually 1 KOhm is ok, but our green LED is a low current type, so even 47K makes a satisfying light  


### DE-Bezugsquellen Spezialkomponenten:

DHT11: 
* [Reichelt](https://www.reichelt.com/de/en/developer-boards-temperature-humidity-sensor-debo-dht-11-p224221.html) 
* [AZ-Delivery](https://www.az-delivery.de/collections/temperatursensoren/products/5-x-dht11-temperatursensor)  
* [Amazon](https://www.amazon.de/s?k=DHT11)

DHT22: 
* [Reichelt](https://www.reichelt.com/de/en/development-boards-temperature-humidity-sensor-debo-dht-22-p224218.html) 
* [AZ-Delivery](https://www.az-delivery.de/collections/temperatursensoren/products/dht22)   
* [Amazon](https://www.amazon.de/s?k=DHT22)

AM2320: 
* [Amazon](https://www.amazon.de/s?k=AM2320) 

DS18B20: 
* [Reichelt](https://www.reichelt.com/de/en/digital-thermometer-1-wire-0-5-c-to-92-ds-18b20-p58169.html) 
* [AZ-Delivery](https://www.az-delivery.de/collections/temperatursensoren/products/5ersetds18b20)  
* [Amazon](https://www.amazon.de/s?k=18B20)

TM1637: 
* [AZ-Delivery](https://www.az-delivery.de/products/4-digit-display)
* [Amazon](https://www.amazon.de/s?k=TM1637)

Buzzer:
* [Amazon](https://www.amazon.de/s?k=Beeper+5V)
