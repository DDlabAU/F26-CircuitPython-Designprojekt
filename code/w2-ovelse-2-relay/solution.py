import time
import board
import digitalio

relay = digitalio.DigitalInOut(board.A1)
relay.direction = digitalio.Direction.OUTPUT

# Forventet wiring:
# - Knap mellem A2 og GND
# - Intern pull-up gør at knappen er True når ikke trykket.
button = digitalio.DigitalInOut(board.A2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    # Knap trykket -> relay ON
    relay.value = not button.value
    time.sleep(0.02)
