import os
import time

required = (
    "WIFI_SSID",
    "WIFI_PASSWORD",
    "AIO_USERNAME",
    "AIO_KEY",
)

missing = [key for key in required if not os.getenv(key)]

if missing:
    print("Mangler i settings.toml:", ", ".join(missing))
else:
    print("settings.toml ser OK ud.")
    print("Tilføj nu jeres Adafruit IO input/output logik i denne fil.")

while True:
    time.sleep(1)
