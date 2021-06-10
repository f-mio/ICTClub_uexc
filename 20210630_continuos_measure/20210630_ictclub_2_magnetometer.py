from sense_hat import SenseHat
import numpy as np
from time import sleep

sense = SenseHat()

none_color     = [0, 150, 0]
detect_1_color = [100, 100, 0]
detect_2_color = [100, 0, 0]

sense.set_imu_config(
    compass_enabled=True,
    gyro_enabled=False,
    accel_enabled=False)

while 1:
    mag_raw = sense.get_compass_raw()
    mag = np.sqrt(mag_raw["x"]**2 + mag_raw["y"]**2 + mag_raw["z"]**2)
    print("{:.1f}μT".format(mag))
    if mag > 300:
        sense.clear(detect_2_color)
    elif mag > 200:
        sense.clear(detect_1_color)
    else:
        sense.clear(none_color)
    sleep(0.5)

    # ループ継続判断
    event = sense.stick.get_events()
    if len(event) > 0 and event[0].direction == "middle":
        break

sense.clear()