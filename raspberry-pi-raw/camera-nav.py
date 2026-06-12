import cv2
from gpiozero import (
     PWMOutputDevice, DigitalOutputDevice, DistanceSensor
)

#motor 3 = drive wheel left, motor 4 = drive wheel right
motor3pwmpin = 12
motor1dirpin = 5
motor2pwmpin = 19
motor2dirpin = 6

motor3pwm = PWMOutputDevice(motor3pwmpin, frequency=1000, initial_value=0)
motor3dir = DigitalOutputDevice(motor1dirpin, initial_value=0)
motor4pwm = PWMOutputDevice(motor2pwmpin, frequency=1000, initial_value=0)
motor4dir = DigitalOutputDevice(motor2dirpin, initial_value=0)

