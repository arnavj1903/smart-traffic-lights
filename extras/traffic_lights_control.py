import RPi.GPIO as GPIO
import time

def setup():
    PIN_MAPPING = {
        1: {'red': 3, 'yellow': 5, 'green': 1},
        #2: {'red': 17, 'yellow': 27, 'green': 22},
        #3: {'red': 14, 'yellow': 15, 'green': 18},
        #4: {'red': 23, 'yellow': 24, 'green': 25}
    }
    global pins 
    pins = {}
    
    GPIO.setmode(GPIO.BCM)  #Use BCM GPIO numbering
    
    for k, v in PIN_MAPPING.items():
        pins[k] = {color: pin for color, pin in v.items()}
        for color, pin in v.items():
            GPIO.setup(pin, GPIO.OUT)
            if color == 'red':
                GPIO.output(pin, GPIO.HIGH) #Turn on red lights
            else:
                GPIO.output(pin, GPIO.LOW) #Turn off yellow and green lights
    
    print("Setup complete")
    return PIN_MAPPING

def light_on(index):
    colors = pins[index]
    GPIO.output(colors['red'], GPIO.LOW)
    GPIO.output(colors['yellow'], GPIO.HIGH)
    time.sleep(1)
    GPIO.output(colors['yellow'], GPIO.LOW)
    GPIO.output(colors['green'], GPIO.HIGH)   

def wait(duration):
    time.sleep(duration)

def light_off(index):
    colors = pins[index]
    GPIO.output(colors['green'], GPIO.LOW)
    GPIO.output(colors['yellow'], GPIO.HIGH)
    time.sleep(2)
    GPIO.output(colors['yellow'], GPIO.LOW)
    GPIO.output(colors['red'], GPIO.HIGH)

def cleanup():
    GPIO.cleanup()
    print("GPIO cleanup complete")


def run():
    setup()
    while True:
        light_on(1)
        wait(5)  # Example duration
        light_off(1)
        light_on(2)
        wait(5)  # Example duration
        light_off(2)
        light_on(3)
        wait(5)  # Example duration
        light_off(3)
        light_on(4)
        wait(5)  # Example duration
        light_off(4)

run()