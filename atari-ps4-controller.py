import RPi.GPIO as GPIO
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BCM)

pins=[22,23,24,25,26]

GPIO.setup(pins, GPIO.IN)

class MyController(Controller):
        def __init__(self, **kwargs):
                Controller.__init__(self, **kwargs)

        def on_x_press(self):
                GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

        def on_x_release(self):
                GPIO.setup(26, GPIO.IN)

        def on_up_arrow_press(self):
                GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

        def on_up_down_arrow_release(self):
                GPIO.setup(22, GPIO.IN)
                GPIO.setup(23, GPIO.IN)

        def on_down_arrow_press(self):
                GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

        def on_left_arrow_press(self):
                GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

        def on_left_right_arrow_release(self):
                GPIO.setup(24, GPIO.IN)
                GPIO.setup(25, GPIO.IN)

        def on_right_arrow_press(self):
                GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
