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
