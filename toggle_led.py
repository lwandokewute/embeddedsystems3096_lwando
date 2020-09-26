import RPi.GPIO as GPIO

#Specifying the numbering system
GPIO.setmode(GPIO.BOARD)

#Setting the gpio's modes
#Input is pin 15, the push button
#GPIO.setup(15, GPIO.IN)

#Enabling PullUp/PullDown for default state of the input (avoiding floating input)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Output is pin 14, the led with initial value
GPIO.setup(14, GPIO.OUT, initial=GPIO.HIGH)

#Main function
def main():
    for i in range(10):
         time.sleep(1000) # 1 second time delay
         GPIO.output(14, GPIO.LOW)
         time.sleep(1000) # 1 second time delay
         GPIO.output(14, GPIO.HIGH)

#TRIAL & EXCEPTION
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        GPIO.cleanup()
    except e:
        print("Some other error occurred: {}".format(e.message))
        GPIO.cleanup()
GPIO.cleanup()
