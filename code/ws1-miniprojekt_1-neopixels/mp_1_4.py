import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

RED = (255, 0, 0)
BLUE = (0, 0, 255)

delay = 0.1

while True:
    # "Politi-blink": hver anden pixel skifter mellem rød og blå.
    for i in range(10):
        cp.pixels[i] = RED if i % 2 == 0 else BLUE
    time.sleep(delay)

    for i in range(10):
        cp.pixels[i] = BLUE if i % 2 == 0 else RED
    time.sleep(delay)
