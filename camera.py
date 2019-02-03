from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/InstaKart/QR code/image.jpg')
camera.stop_preview()
