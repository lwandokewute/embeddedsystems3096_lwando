import RPi.GPIO as GPIO

#Specifying the numbering system
GPIO.setmode(GPIO.BOARD)

#Setting the gpio's modes
#Input is pin 15, the push button
GPIO.setup(15, GPIO.IN)

#Output is pin 14, the led
GPIO.setup(14, GPIO.OUT, initial=GPIO.HIGH)

#Main function
def main():
   
