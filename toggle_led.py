import RPi.GPIO as GPIO
import time

#Specifying the numbering system
GPIO.setmode(GPIO.BOARD)

#Setting the gpio's modes
#Input is pin 15, the push button
#GPIO.setup(15, GPIO.IN)

#Enabling PullUp/PullDown for default state of the input (avoiding floating input)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Output is pin 14, the led with initial value
GPIO.setup(16, GPIO.OUT, initial=1)

#Main function for toggling the led
#def main():
#    for i in range(10):
#        time.sleep(1) # 1 second time delay
#        GPIO.output(16, GPIO.LOW)
#        time.sleep(1) # 1 second time delay
#        GPIO.output(16, GPIO.HIGH)

LED_NEXT_STATE = [True]

#Main function for using the switch
def main():
    while True:    
        channel = GPIO.wait_for_edge(18, GPIO.FALLING, timeout=1000)
        if channel is 0:
            print('Press detected')
            LED_NEXT_STATE[0] = not LED_NEXT_STATE[0]
            GPIO.output(16, LED_NEXT_STATE[0])
        
        GPIO.remove_event_detect(18)

#TRIAL & EXCEPTION
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        GPIO.cleanup()
    except e:
        print("Some other error occurred: {}".format(e.message))
        GPIO.cleanup()
GPIO.cleanup()
