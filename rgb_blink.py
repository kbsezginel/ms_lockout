"""
Blink RGB LEDs using Raspberry PI GPIO
"""
import RPi.GPIO as GPIO
import time


COLORS = {'red':    [True, False, False],
          'green':  [False, True, False],
          'blue':   [False, False, True],
          'yellow': [True, True, False],
          'purple': [True, False, True],
          'cyan':   [False, True, False],
          'white':  [True, True, True]}


def rgb_blink(pins, color, sleep=1):
    """Blink LED using given GPIO pin, number of times and speed.

    Args:
        - pins (list): GPIO pins in order of RGB
        - color (str): LED color
        - sleep (int): sleep in seconds (default: 1)

    Returns:
        - None (blinks led)
    """
    color_pins = COLORS[color]
    for pidx, pin in enumerate(pins):
        if color_pins[pidx]:
            GPIO.output(pin, GPIO.HIGH)
    time.sleep(sleep)
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
