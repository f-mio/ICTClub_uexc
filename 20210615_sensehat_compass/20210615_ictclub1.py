from sense_hat import SenseHat
from datetime import datetime
from time import sleep
import csv

record_color = [160,0, 0]
finish_color = [0, 160, 0]

sense = SenseHat()


sampling_time  = 1
measuring_time = 1
output_size    = int(measuring_time * 60 / sampling_time)

data = [ ["date", "t", "h", "p"] ]

while True:
    sense.clear(record_color)
    t = sense.get_temperature()
    h = sense.get_humidity()
    p = sense.get_pressure()
    date = datetime.now()
    data.append([date,t,h,p])

    if len(data) > output_size:
        with open("data.csv", "w") as f:
            writer = csv.writer(f)
            for record in data:
                writer.writerow(record)
        break
    sleep(sampling_time)

sense.clear(finish_color)
sleep(2)
sense.clear()