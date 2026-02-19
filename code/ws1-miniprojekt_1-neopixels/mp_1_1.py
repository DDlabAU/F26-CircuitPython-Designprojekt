from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3

while True:
    cp.pixels[0] = (0, 255, 0)
    cp.pixels[1] = (255, 255, 0)
