from sense_hat import SenseHat

sense = SenseHat()


sense.set_imu_config(
    compass_enabled=True,
    gyro_enabled=False,
    accel_enabled=False)


mag = sense.get_compass()

print(mag)

#while 1:
#    mag = sense.get_