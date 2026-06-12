from gpizero import (
     PWMOutputDevice, DigitalOutputDevice, DistanceSensor
)
from time import sleep
import board, busio, adafruit_tcs34725

#motor 1 = intake, motor 2 = conveyor
motor1pwmpin = 18
motor1dirpin = 23
motor2pwmpin = 13
motor2dirpin = 24

#distance sensor hc-sro4
triggerpin = 17
echopin = 27

#color sensor tcs34725
colori2c = busio.I2C(board.SCL, board.SDA)
colorsensor = adafruit_tcs34725.TCS34725(colori2c)
colorsensor.integration_time = 200
colorsensor.gain = 4

motor1pwm = PWMOutputDevice(motor1pwmpin, frequency=1000, initial_value=0)
motor1dir = DigitalOutputDevice(motor1dirpin, initial_value=0)
motor2pwm = PWMOutputDevice(motor2pwmpin, frequency=1000, initial_value=0)
motor2dir = DigitalOutputDevice(motor2dirpin, initial_value=0)
distsensor = DistanceSensor(echo=echopin, trigger=triggerpin, max_distance=4.0)

#thresholds 
distthreshold = 0.1
luxthresholdsort = 110
luxthresholdblank = 30

def setIntake(dir, speed):
     motor1dir.value = dir
     motor1pwm.value = speed

def setConveyor(dir, speed):
     motor2dir.value = dir
     motor2pwm.value = speed

#right for bright clothing, left for dark, keep conveyor going until clothing is gone
def checkColor():
     if colorsensor.lux > luxthresholdsort:
          setConveyor(1, 1.0)
          while colorsensor.lux > luxthresholdblank:
               sleep(1)
          setConveyor(0, 0)
     else:
          setConveyor(0, 1.0)
          while colorsensor.lux > luxthresholdblank:
               sleep(1)
          setConveyor(0, 0)

def checkForClothing():
     if distsensor.distance < distthreshold:
          setIntake(1, 1.0)
          while distsensor.distance < distthreshold:
               sleep(1)
          setIntake(0, 0)

while True:
     checkForClothing()
     if colorsensor.lux > luxthresholdblank:
          checkColor()
     sleep(0.2)