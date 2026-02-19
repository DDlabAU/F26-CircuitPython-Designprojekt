from adafruit_circuitplayground import cp
import time

cp.detect_taps = 1

while True:
    if cp.tapped:
        print("Tapped!")
        
        cp.pixels.fill((255, 0, 0))
        # Alternativt brug et for-loop som tidligere:
        # for i in range(10):
        #     cp.pixels[i] = (255, 0, 0)

        time.sleep(1)
    else:
        cp.pixels.fill((255, 0, 0))
        # Alternativt brug et for-loop som tidligere:
        # for i in range(10):
        #     cp.pixels[i] = (0, 0, 0)
