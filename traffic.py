from machine import Pin
import time


DS = Pin(20, Pin.OUT)    # data
SHCP = Pin(18, Pin.OUT)  # shift clock
STCP = Pin(19, Pin.OUT)  # storage clock
OE = Pin(21, Pin.OUT)    # output enable

# Function to turn on lights one by one in 5 second increments
def lights_on():
    for i in range(16): 
        for bit in range(16):  # Shift 16 bits to control all lights
            if bit == i:
                DS.value(1)  # Turn on one light
            else:
                DS.value(0)  # Turn off all other lights
            
            # Shift 
            SHCP.value(1)
            SHCP.value(0)
        
        # latch to storage
        STCP.value(1)
        STCP.value(0)
        
        # enable output
        OE.off()
        
        # 5 seconds
        time.sleep(5)

#call the function
lights_on()


