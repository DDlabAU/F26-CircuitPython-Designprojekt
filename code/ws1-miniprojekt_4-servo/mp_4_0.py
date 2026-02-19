import board
import time
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=50)
my_servo = servo.Servo(pwm)