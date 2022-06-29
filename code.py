from time import sleep
from gpiozero import Buzzer, InputDevice
 
buzz    = Buzzer(13)
no_rain = InputDevice(18)
waterlevel = InputDevice(17)

def buzz_now(iterations):
    for x in range(iterations):
        buzz.on()
        sleep(0.1)
        buzz.off()
        sleep(0.1)

def long_beep():
    buzz.on()
    sleep(10)
    buzz.off()
    sleep(0.1)

while True:
    if no_rain.is_active:
        print("It's raining - take measures.")
        buzz_now(2)
        if(waterlevel.value == 1):
            print("Therainfall has exceeded its limits!! Please start necessary precautions.")
            long_beep()

        sleep(1)