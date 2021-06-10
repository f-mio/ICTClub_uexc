from SenseHat import sense_hat

sense = SenseHat()

temp = sense.get_temperature()

sense.show_message("{:.1f} celsius".format(temp))