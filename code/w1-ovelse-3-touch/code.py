import time
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touched pad A1")
        cp.red_led = True
    else:
        cp.red_led = False
    time.sleep(0.05)
