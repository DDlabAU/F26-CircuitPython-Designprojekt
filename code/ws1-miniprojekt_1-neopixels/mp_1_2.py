from adafruit_circuitplayground import cp
import time # giver adgang til time.sleep(secs)

cp.pixels.brightness = 0.3

while True:
    # cp.pixels.fill gør det samme, men det er nemmere for os at arbejde videre fra et foor-loop
    # cp.pixels.fill((255, 0, 0))
    for i in range(10):
        cp.pixels[i] = (255, 0, 0)
