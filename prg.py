import subprocess
import time
import smbus
from Adafruit_ADS1x15 import ADS1x15
from time import sleep
adc = ADS1x15()

while True:
        t_reg = 0x05
        address = 0x18
        bus = smbus.SMBus(1)
        reading = bus.read_i2c_block_data(address, t_reg)
        t = (reading[0] << 8) + reading[1]

        temp = t & 0x0FFF
        temp /=  16.0
        if (t & 0x1000):
            temp -= 256

        fichier = open("/var/www/temp.txt","w")
        fichier.write(str(float(temp)))
        fichier.close()
        output=str(float(temp))
        print output

        result = (adc.readADCSingleEnded(0)-500)/10
        print result
	fichier2 = open("/var/www/temp2.txt","w")
	fichier2.write(str(result))
	fichier2.close()
	time.sleep(1)



