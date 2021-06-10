from sense_hat inport SenseHat

sense = SenseHat()

temp = sense.get_temperature()

sense.show_message("{:.1f} celsius".format(temp))


