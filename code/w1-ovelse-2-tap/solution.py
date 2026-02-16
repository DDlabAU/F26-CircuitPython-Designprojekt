import time
from adafruit_circuitplayground import cp

cp.detect_taps = 1
lights_on = False

while True:
    if cp.tapped:
        lights_on = not lights_on
        print("Tapped! lights_on =", lights_on)

        if lights_on:
            cp.red_led = True
            cp.pixels.fill((0, 40, 140))
        else:
            cp.red_led = False
            cp.pixels.fill((0, 0, 0))

        # Enkel debounce så ét tap ikke registreres flere gange.
        time.sleep(0.25)
