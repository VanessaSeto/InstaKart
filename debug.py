import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
camera = PiCamera()

notPressed = True
while notPressed:
    if GPIO.input(24) == GPIO.HIGH:
        camera.start_preview()
        sleep(3)
        camera.capture('/home/pi/Desktop/InstaKart/QR code/image.jpg')
        camera.stop_preview()
        notPressed = False
GPIO.cleanup()
