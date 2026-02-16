import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=50)
my_servo = servo.Servo(pwm)


def sweep(start, stop, step):
    for angle in range(start, stop, step):
        my_servo.angle = angle
        time.sleep(0.03)
        if not cp.button_a:
            return


while True:
    # Hold knap A nede for at aktivere sweep.
    if cp.button_a:
        cp.red_led = True
        sweep(0, 181, 5)
        sweep(180, -1, -5)
    else:
        cp.red_led = False
        my_servo.angle = 90
        time.sleep(0.05)
