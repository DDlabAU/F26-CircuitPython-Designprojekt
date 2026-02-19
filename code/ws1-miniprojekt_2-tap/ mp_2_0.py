from adafruit_circuitplayground import cp
import time

cp.detect_taps = 1

while True:
    if cp.tapped:
        print("Tapped!")
        cp.red_led = True
        time.sleep(1)
    else:
        cp.red_led = False