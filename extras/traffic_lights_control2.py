from machine import Pin
import time
import main

def setup():
    PIN_MAPPING = {
    1: {'red': 1, 'yellow': 3, 'green': 2},
    2: {'red': 4, 'yellow': 5, 'green': 6},
    3: {'red': 16, 'yellow': 17, 'green': 18},
    4: {'red': 22, 'yellow': 26, 'green': 27}
}
    global pins 
    pins = {}
    for k, v in PIN_MAPPING.items():
        pins[k] = {color: Pin(pin, Pin.OUT) for color, pin in v.items()}
    for pin_set in pins.values():
        for pin in pin_set.values():
            pin.on()
    print("Setup complete")
    return PIN_MAPPING


def light_on(index):
    colors = pins[index]
    colors['red'].off()
    colors['yellow'].on()
    time.sleep(1)
    colors['yellow'].off()
    colors['green'].on()   

def wait():
    duration=main.traffic_lights_control()
    time.sleep(duration)

def light_off(index):
    colors = pins[index]
    colors['green'].off()
    colors['yellow'].on()
    time.sleep(2)
    colors['yellow'].off()
    colors['red'].on()

'''def run():
    setup()
    while True():
        lights_on(1)
        wait()
        lights_off(1)
        lights_on(2)
        wait()
        lights_off(2)
        lights_on(3)
        wait()
        lights_off(3)
        lights_on(4)
        wait()
        lights_off(4)'''
