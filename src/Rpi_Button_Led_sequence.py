import RPi.GPIO as GPIO
import time

LED_PIN_LIST = [17, 27, 22]
BUTTON_PIN = 26

#function for light the LED base on index
def power_on_selected_led(selected_pin):
    #make sure only turn on or off the pin of the LED
    if selected_pin not in LED_PIN_LIST:
        return
    for pin in LED_PIN_LIST:
        if pin == selected_pin:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

GPIO.setmode(GPIO.BCM)

#setup led pins
for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
#setup button
GPIO.setup(BUTTON_PIN, GPIO.IN)

#initial previous button state, led_index
previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0
for pin in LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)

while True:
    #Take current button state
    button_state = GPIO.input(BUTTON_PIN)
    #If button state not change (keep pressed, or not pressed), then nothing happen, else:
    if button_state != previous_button_state:
        #assign new state for previous_button_state
        previous_button_state = button_state
        #if the button is press
        if button_state == GPIO.HIGH:
            #turn on the selected led only
            power_on_selected_led(LED_PIN_LIST[led_index])
            led_index +=1
            #check index of the led not outside the number of LEDs
            if led_index>=len(LED_PIN_LIST):
                led_index = 0

GPIO.cleanup()