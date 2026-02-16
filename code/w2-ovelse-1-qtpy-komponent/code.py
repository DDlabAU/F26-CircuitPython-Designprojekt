import time
import board
import busio

print("I2C scan starter...")
i2c = busio.I2C(board.SCL, board.SDA)

while not i2c.try_lock():
    pass

try:
    devices = i2c.scan()
    if devices:
        print("Fundne I2C adresser:", [hex(address) for address in devices])
    else:
        print("Ingen I2C enheder fundet. Tjek sensor + kabel.")
finally:
    i2c.unlock()

while True:
    time.sleep(1)
