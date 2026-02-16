import time
import board

print("QT Py første testkode starter...")

required_libs = (
    "adafruit_bus_device",
    "adafruit_register",
)
missing_libs = []

for lib in required_libs:
    try:
        __import__(lib)
    except ImportError:
        missing_libs.append(lib)

if missing_libs:
    print("Mangler libraries:", ", ".join(missing_libs))
    print("Kopier dem til CIRCUITPY/lib hvis I bruger STEMMA-sensorer.")
else:
    print("Library check OK")

pixel = None
led = None

try:
    import neopixel

    pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2, auto_write=True)
    print("NeoPixel fundet.")
except Exception as exc:
    print("NeoPixel ikke tilgængelig:", exc)

try:
    import digitalio

    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    print("Board LED fundet.")
except Exception as exc:
    print("Board LED ikke tilgængelig:", exc)

if pixel is None and led is None:
    print("Ingen lys-output tilgængelig. Tjek board definition.")

for color in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
    if pixel is not None:
        pixel[0] = color
    if led is not None:
        led.value = not led.value
    print("Viser farve/status:", color)
    time.sleep(0.35)

if pixel is not None:
    pixel[0] = (0, 0, 0)
if led is not None:
    led.value = False

print("QT Py første testkode gennemført.")

while True:
    if led is not None:
        led.value = not led.value
    if pixel is not None:
        pixel[0] = (12, 12, 12) if led is not None and led.value else (0, 0, 0)
    time.sleep(0.5)
