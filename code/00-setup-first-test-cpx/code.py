import time
import board
import neopixel

print("CPX første testkode starter...")

missing_libs = []
try:
    from adafruit_circuitplayground import cp
except ImportError:
    cp = None
    missing_libs.append("adafruit_circuitplayground")

if missing_libs:
    print("Mangler libraries:", ", ".join(missing_libs))
    print("Kopier manglende library til CIRCUITPY/lib")
else:
    print("Library check OK")

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.15, auto_write=True)
colors = (
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
)

for color in colors:
    pixels.fill(color)
    if cp is not None:
        cp.red_led = not cp.red_led
    print("Viser farve:", color)
    time.sleep(0.35)

pixels.fill((0, 0, 0))
if cp is not None:
    cp.red_led = False
print("CPX første testkode gennemført.")

while True:
    # Heartbeat så board tydeligt er aktivt.
    if cp is not None:
        cp.red_led = not cp.red_led
    time.sleep(0.5)
