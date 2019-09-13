import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
n = 1
GPIO.setup(4,GPIO.IN) #Gpio4 (pin16)


while 1:
  if GPIO.input(4) == False:
  
    now = time.strftime("Date%m-%d-%yTime%H-%M-%S")
	
    command = "bash oscmds.sh " +  str(now)		#str(now) argumentot
    os.system(command)
    
	emailcommand = 'python2 IOTNOTIFY2.py ' + now + '.jpg"'
    os.system(emailcommand)