from sense_hat import SenseHat

20210615_sense = SenseHat()

temp = 20210615_sense.get_temperature()

20210615_sense.show_message("{:.1f} celsius".format(temp))
