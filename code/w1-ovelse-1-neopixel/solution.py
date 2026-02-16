import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

while True:
    # "Politi-blink": hver anden pixel skifter mellem rød og blå.
    for i in range(10):
        cp.pixels[i] = (255, 0, 0) if i % 2 == 0 else (0, 0, 255)
    time.sleep(0.12)

    for i in range(10):
        cp.pixels[i] = (0, 0, 255) if i % 2 == 0 else (255, 0, 0)
    time.sleep(0.12)
