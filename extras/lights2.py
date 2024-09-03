from gpiozero import LED
from time import sleep

def setup():
    PIN_MAPPING = {
        1: {'red': 3, 'yellow': 5, 'green': 1},
        #2: {'red': 17, 'yellow': 27, 'green': 22},
        #3: {'red': 14, 'yellow': 15, 'green': 18},
        #4: {'red': 23, 'yellow': 24, 'green': 25}
    }
    global pins 
    pins = {}
    
    for k, v in PIN_MAPPING.items():
        pins[k] = {color: LED(pin) for color, pin in v.items()}
        for color, led in pins[k].items():
            if color == 'red':
                led.on()  # Turn on red lights
            else:
                led.off()  # Turn off yellow and green lights
    
    print("Setup complete")
    return PIN_MAPPING

def light_on(index):
    colors = pins[index]
    colors['red'].off()
    colors['yellow'].on()
    sleep(1)
    colors['yellow'].off()
    colors['green'].on()

def wait(duration):
    sleep(duration)

def light_off(index):
    colors = pins[index]
    colors['green'].off()
    colors['yellow'].on()
    sleep(2)
    colors['yellow'].off()
    colors['red'].on()

def cleanup():
    for group in pins.values():
        for led in group.values():
            led.close()
    print("GPIO cleanup complete")

def run():
    try:
        setup()
        while True:
            for i in range(1, 5):
                light_on(i)
                wait(5)  # Example duration
                light_off(i)
    except KeyboardInterrupt:
        cleanup()

if __name__ == "__main__":
    run()
