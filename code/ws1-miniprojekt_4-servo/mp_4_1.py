import time
import board
import pwmio
import analogio
import simpleio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=50)
my_servo = servo.Servo(pwm)

light = analogio.AnalogIn(board.LIGHT)

while True:
    # Ret i værdierne 1000 og 40000 her, hvis det ikke opfører sig som forventet
    # light.value giver potentielt en værdi mellem 0-65535,
    # men de faktiske værdier kan komme i et langt mindre spænd alt efter forholdene 
    angle = simpleio.map_range(light.value, 1000, 40000, 0, 180)
    my_servo.angle = angle
    print(light.value, angle)
    time.sleep(0.05)
