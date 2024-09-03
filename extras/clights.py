from gpiozero import TrafficLights
from time import sleep

# Define GPIO pins for each traffic light
TRAFFIC_LIGHTS = {
    1: TrafficLights(2, 3, 4),
    2: TrafficLights(17, 27, 22),
    3: TrafficLights(0, 5, 6),
    4: TrafficLights(16, 20, 21)
}

def setup():
    # No setup needed for gpiozero
    return TRAFFIC_LIGHTS

def light_on(light_number):
    if light_number in TRAFFIC_LIGHTS:
        TRAFFIC_LIGHTS[light_number].green.on()
        TRAFFIC_LIGHTS[light_number].amber.off()
        TRAFFIC_LIGHTS[light_number].red.off()

def light_off(light_number):
    if light_number in TRAFFIC_LIGHTS:
        TRAFFIC_LIGHTS[light_number].green.off()
        TRAFFIC_LIGHTS[light_number].amber.off()
        TRAFFIC_LIGHTS[light_number].red.on()

def yellow_on(light_number):
    if light_number in TRAFFIC_LIGHTS:
        TRAFFIC_LIGHTS[light_number].green.off()
        TRAFFIC_LIGHTS[light_number].amber.on()
        TRAFFIC_LIGHTS[light_number].red.off()

def wait(duration):
    sleep(duration)

def cleanup():
    # gpiozero handles cleanup automatically
    pass

def all_red():
    for light in TRAFFIC_LIGHTS.values():
        light.red.on()
        light.amber.off()
        light.green.off()

def transition_to_green(light_number):
    if light_number in TRAFFIC_LIGHTS:
        yellow_on(light_number)
        wait(2)  # Yellow light duration
        light_on(light_number)

def transition_to_red(light_number):
    if light_number in TRAFFIC_LIGHTS:
        yellow_on(light_number)
        wait(2)  # Yellow light duration
        light_off(light_number)

for i in range (1, 5):
    light_on(i)
    wait(2)
    light_off(i)