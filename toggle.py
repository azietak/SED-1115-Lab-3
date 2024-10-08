from machine import Pin
import time


#Set up LED 2 on pin 20 as output
led_2 = Pin(20, Pin.OUT)
#Set switch on pin 13 as input with pull down
switch_4 = Pin(13, Pin.IN, Pin.PULL_DOWN)

#Variables for button states
prev_state = False
curr_state = False


while True:
    prev_state = curr_state #Update the previous button state
    curr_state = switch_4.value() # Read current button state

    #Checking if button is just pressed
    if curr_state == 1 and prev_state == 0:
        led_2.toggle() #Toggle LED 2 
        
        #Add delay for multiple toggle bc button bounce
        time.sleep_ms(100)