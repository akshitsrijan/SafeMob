'''
Connections:
VCC ----> 3.3V(Pin 1) or 5V (Pin 2)
GND ----> GND (Pin 6)
out ----> GPIO14 (Pin 8 I guess gomma wait lemme check)

:)

'''


import RPi.GPIO as GPIO
import time

#using BCM GPIO nnumbering
GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 14

#Set pin as input
GPIO.setup(SENSOR_PIN, GPIO.IN)

print("Starting IR sensor Test.Press CTRL +C to exit.")

try:
  while true:
    sensor_value=GPIO.input(SENSOR_PIN)
    if sensor_value == GPIO.LOW:
      print("Obstacle detected")
    else:
      print("No obstacle detected")
    time.sleep(0.5)

except KeyboardInterrupt:
  GPIO.cleanup()
  print("Exiting script.")
