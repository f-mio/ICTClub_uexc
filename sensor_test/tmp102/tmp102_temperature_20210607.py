import smbus
import time

bus = smbus.SMBus(1)


while True:
    data = bus.read_i2c_block_data(0x48, 0)
    msb = data[0]
    lsb = data[1]

    temp =  ( ( (msb<<8) | lsb ) >> 4) * 0.0625
    print("environment temperature  :  {:.1f} celsius".format(temp))
    time.sleep(1)
