from adafruit_circuitplayground import cp
import time # giver adgang til time.sleep(secs)

cp.pixels.brightness = 0.3

while True:
    for i in range(10):
        cp.pixels[i] = (255, 0, 0)
        time.sleep(0.1)


    for i in range(10):
        cp.pixels[i] = (0, 0, 0)
        time.sleep(0.1)

    # Alternativt kan man slukke fra den anden "retning"
    # for i in range(9, -1, -1):
    #     cp.pixels[i] = (0, 0, 0)
    #     time.sleep(0.25)
