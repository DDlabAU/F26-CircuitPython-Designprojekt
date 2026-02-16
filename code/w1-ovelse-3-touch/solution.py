import time
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touched pad A1")
        cp.red_led = True
        cp.pixels.fill((120, 80, 0))
        cp.start_tone(440)
    else:
        cp.red_led = False
        cp.pixels.fill((0, 0, 0))
        cp.stop_tone()

    time.sleep(0.05)
