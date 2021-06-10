from sense_hat import SenseHat

sense = SenseHat()

temp = sense.get_temperature()

sense.show_messages("{:.1f} celsius".format(temp))
