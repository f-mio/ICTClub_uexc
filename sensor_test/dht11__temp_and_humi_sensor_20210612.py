import RPi.GPIO as GPIO
import time

dhtPin = 17

GPIO.setmode(GPIO.BCM)

max_unchange_count = 100

state_init_pull_down = 1
state_init_pull_up = 2
state_data_first_pull_down = 3
state_data_pull_up = 4
state_data_pull_down = 5


def readDht11():
    GPIO.setup(dhtPin, GPIO.OUT)
    GPIO.output(dhtPin, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(dhtPin, GPIO.LOW)
    time.sleep(0.02)
    GPIO.setup(dhtPin, GPIO.IN, GPIO.PUD_UP)

    unchanged_count = 0
    last = -1
    data = []
    
    while True:
        current = GPIO.input(dhtPin)
        data.append(current)
        if last != current:
            unchanged_count = 0
            last = current
        else:
            unchanged_count += 1
            if unchanged_count > max_unchange_count:
                break

    state = state_init_pull_down

    lengths = []
    current_length = 0

    for current in data:
        current_length += 1
        
        if state == state_init_pull_down:
            if current == GPIO.LOW:
                state = state_init_pull_up
            else:
                continue

        if state == state_init_pull_up:
            if current == GPIO.HIGH:
                state = state_data_first_pull_down
            else:
                continue

        if state == state_data_first_pull_down:
            if current == GPIO.LOW:
                state = state_data_pull_up
            else:
                continue

        if state == state_data_pull_up:
            if current == GPIO.HIGH:
                current_length = 0
                state = state_data_pull_down
            else:
                continue


        if state == state_data_pull_down:
            if current == GPIO.LOW:
                lengths.append(current_length)
                state = state_data_pull_up
            else:
                continue
    if len(lengths) != 40:
        return False

    shortest_pull_up = min(lengths)
    longest_pull_up  = max(lengths)
    halfway = (longest_pull_up + shortest_pull_up) / 2
    bits = []
    the_bytes = []
    byte = 0
    
    for length in lengths:
        bit = 0
        if length > halfway:
            bit = 1
        bits.append(bit)

    for i in range(0, len(bits)):
        byte = byte << 1
        if bits[i]:
            byte = byte | 1
        else:
            byte = byte | 0
        if (i+1)%8 == 0:
            the_bytes.append(byte)
            byte = 0
            
    checksum = (the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3]) & 0xFF
    if the_bytes[4] != checksum:
        return False

    return the_bytes[0], the_bytes[2]

def main():
    
    while True:
        result = readDht11()
        if result:
            humidity, temperature = result
            print("humidity: %s %%, temperture: %s C`" % (humidity, temperature))
        time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()

