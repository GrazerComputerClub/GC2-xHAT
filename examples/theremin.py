pi@raspberrypi:~ $ cat theremin.py 
from gpiozero import TonalBuzzer, DistanceSensor
from time import sleep

buzzer = TonalBuzzer(18)
ds= DistanceSensor(echo=27, trigger=17)

buzzer.source = ds

while True:  
    print("Distance= %3.2f" % (ds.distance *100), 'cm')
    sleep(0.5)

