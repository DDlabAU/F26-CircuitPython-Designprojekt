import time
from adafruit_circuitplayground import cp


while True:
    if cp.touch_A1:
        print("Touched pad A1")
        cp.red_led = True
        cp.pixels.fill((0, 120, 255))
        cp.start_tone(262)
    elif cp.touch_A2:
        print("Touched pad A2")
        cp.red_led = True
        cp.pixels.fill((255, 0, 120))
        cp.start_tone(294)
    else:
        cp.red_led = False
        cp.pixels.fill((0, 0, 0))
        cp.stop_tone()

    time.sleep(0.05)
