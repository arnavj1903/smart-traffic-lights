from gpiozero import AngularServo
from time import sleep

signalPIN = 14  # Change the GPIO pin later
servo = AngularServo(signalPIN, min_angle=0, max_angle=360, min_pulse_width=0.0005, max_pulse_width=0.0024)

def smooth_move(start_angle, end_angle, steps=10, delay=0.1):
    angle_diff = end_angle - start_angle
    step_size = angle_diff / steps

    for step in range(steps + 1):
        servo.angle = start_angle + step * step_size
        sleep(delay)

def motor():
    smooth_move(90, 270)  # Move from 90 to 270 degrees
    sleep(3)
    smooth_move(270, 90)  # Move back from 270 to 90 degrees
    sleep(3)

while True:
    motor()
