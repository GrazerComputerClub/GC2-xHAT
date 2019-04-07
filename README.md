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
	 - S3 (GPIO21, Active High, Default Low)
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

![GC2-xHAT](https://github.com/GrazerComputerClub/GC2-xHAT/raw/master/GC2-xHAT.jpg)


## Components list
	
10 x Resistor 1K  (LED, protection)  
 4 x Resistor 4K7 (R1, R6, R7, R11 transistor base)  
 1 x Resistor 6K8 (R2)  
 1 x Resistor 47K (R5 green LED)  
 3 x Tactile switch 6x6mm  
 1 x LED red 3mm  
 1 x LED orange 3mm  
 1 x LED green 3mm  
 1 x LED blue 3mm  
 1 x LED pink 3mm  
 1 x Transistor BC547B  
 1 x Female pin header socket 2x4  
 1 x Female pin header socket 1x4  
 1 x Female pin header socket 2x20  
 1 x DHT11 o. DHT22 o. AM2302  
 1 x AM2322 o. AM2320  
 1 x DS18B20  
 1 x TM1637 4 Digi LED display modul (GND, VCC, DIO, CLK)  
 1 x Buzzer (O 12mm, 7.2mm holes)  
 1 x FET IRLML6401  
 1 x EEPROM STM M24C64-WMN6  
 2 x SMD 1206 resistor 3K9  
