import adafruit_dht
from adafruit_motor import servo
import board
import pwmio
import time

# Choose the pin connected to the DHT sensor data line.
# For example, to use GP15:
dht_pin = board.GP15

# Initialize the DHT22 device (use DHT22 for the AM2302 sensor)
dht_device = adafruit_dht.DHT22(dht_pin)


# Raspberry Pi Pico uses GP pins (GP0, GP1, GP2, etc.)
# Common PWM pins on Pico: GP0, GP1, GP2, GP3, GP4, GP5, etc.
SERVO_PIN = board.GP0  # Change this to your connected pin

# Create PWM object
pwm = pwmio.PWMOut(SERVO_PIN, frequency=50)

# Create servo object
servo_motor = servo.Servo(pwm, min_pulse=500, max_pulse=2500)

def set_servo_angle(angle):
    """Set servo to a specific angle (0-180 degrees)"""
    if 0 <= angle <= 180:
        servo_motor.angle = angle
        print(f"Servo set to {angle} degrees")
    else:
        print("Angle must be between 0 and 180 degrees")

# Test the servo
print("Servo test starting...")
while not True:
    set_servo_angle(0)      # 0 degrees
    time.sleep(1)
    set_servo_angle(90)     # 90 degrees (center)
    time.sleep(1)
    set_servo_angle(180)    # 180 degrees
    time.sleep(1)
    set_servo_angle(90)     # Back to center
    time.sleep(1)
print("Done servo sweep.")

import time
import board
import analogio
import microcontroller

# The RP2040 ADC is a 12-bit ADC, which means it reads values from 0 to 65535.
# The `read_u16()` method in CircuitPython handles this.
# The reference voltage is typically 3.3V on the Pico.
ADC_VREF = 3.3  # Reference voltage of the RP2040 ADC

# Voltage divider resistor values
# R1 is the resistor connected to the voltage source (the larger one)
# R2 is the resistor connected to the ADC pin and ground (the smaller one)
# Your setup: 22kΩ (R1) and 2.2kΩ (R2)
R1 = 22000.0  # 22kΩ
R2 = 2200.0   # 2.2kΩ

# The voltage divider ratio, used to calculate the actual input voltage.
# V_in = V_out * (R1 + R2) / R2
divider_ratio = (R1 + R2) / R2

# Initialize the Analog-to-Digital Converter on GPIO28 (ADC2).
# ADC pins on the Pico are GPIO26 (ADC0), GPIO27 (ADC1), and GPIO28 (ADC2).
adc_pin = board.GP28
adc_input = analogio.AnalogIn(adc_pin)

print("Starting RP2040 ADC voltage reader on GPIO28...")
print("Reading from a voltage divider with R1=22kΩ and R2=2.2kΩ.")

# Function to read and convert the ADC value
def read_and_calculate_voltage():
    """
    Reads the raw ADC value, converts it to a voltage at the ADC pin,
    and then calculates the actual input voltage from the voltage divider.
    """
    # Read the raw 16-bit ADC value. It ranges from 0 to 65535.
    raw_value = adc_input.value

    # Convert the raw ADC value to a voltage at the ADC pin.
    # The Pico's ADC is 12-bit, but `read_u16()` returns a 16-bit value.
    # The formula is (raw_value / 65535) * Vref.
    voltage_at_adc_pin = (raw_value / 65535) * ADC_VREF
    
    # Calculate the actual input voltage to the voltage divider
    # by multiplying the ADC pin voltage by the voltage divider ratio.
    input_voltage = voltage_at_adc_pin * divider_ratio
    
    return raw_value, voltage_at_adc_pin, input_voltage

try:
    while True:
        raw_val, adc_volts, input_volts = read_and_calculate_voltage()
        print(f"Raw ADC: {raw_val:<5} | Voltage at pin: {adc_volts:.3f} V | Input Voltage: {input_volts:.3f} V")
        
        
        # Read the sensor values
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        # Optional: convert temperature to Fahrenheit
        if temperature_c is not None and humidity is not None:
            # Print the results
            print(f"Temp: {temperature_c:.1f} °C")
            print(f"Humidity: {humidity:.1f} %")

        time.sleep(1) # Wait for 1 second before the next reading
        set_servo_angle(0)      # 0 degrees
        time.sleep(1)
        set_servo_angle(90)     # 90 degrees (center)
        time.sleep(1)
        set_servo_angle(180)    # 180 degrees
        time.sleep(1)
        set_servo_angle(90)     # Back to center
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped.")
    

import time
import usb_hid
from adafruit_hid.mouse import Mouse

# Initialize the Mouse object
# The USB HID device must be a mouse
try:
    mouse = Mouse(usb_hid.devices)
except OSError:
    print("USB HID Mouse device not found. Ensure your firmware has HID support.")

# --- Mouse Functions ---

def move_mouse(x_delta, y_delta):
    """
    Moves the mouse cursor by a specified delta.
    
    Args:
        x_delta (int): The change in the x-coordinate.
        y_delta (int): The change in the y-coordinate.
    """
    if mouse:
        mouse.move(x=x_delta, y=y_delta)
        time.sleep(0.01) # Small delay to prevent issues with fast updates

def click_mouse(button):
    """
    Clicks a specified mouse button.
    
    Args:
        button (int): The button to click (e.g., Mouse.LEFT_BUTTON).
    """
    if mouse:
        mouse.click(button)
        time.sleep(0.1) # Delay to simulate a proper click action

def scroll_mouse(scroll_delta):
    """
    Scrolls the mouse wheel.
    
    Args:
        scroll_delta (int): The amount to scroll. Positive is up, negative is down.
    """
    if mouse:
        mouse.move(wheel=scroll_delta)
        time.sleep(0.01)

# --- Main Program Logic ---

def main():
    print("Starting Raspberry Pi Pico HID Mouse demonstration...")

    # Example 1: Move the mouse in a square pattern
    print("Moving mouse in a square pattern...")
    for _ in range(4):
        move_mouse(x_delta=20, y_delta=0)
        time.sleep(0.5)
    
        move_mouse(x_delta=0, y_delta=20)
        time.sleep(0.5)
    
        move_mouse(x_delta=-20, y_delta=0)
        time.sleep(0.5)
    
        move_mouse(x_delta=0, y_delta=-20)
        time.sleep(0.5)

    # Example 2: Click the left mouse button
    # print("Clicking the left mouse button...")
    # click_mouse(Mouse.LEFT_BUTTON)

    # Example 3: Scroll the mouse wheel up and down
    # print("Scrolling the mouse wheel up and down...")
    # scroll_mouse(scroll_delta=5)
    # time.sleep(1)
    # scroll_mouse(scroll_delta=-5)
    # time.sleep(1)

    print("Demonstration complete.")

# Run the main program
main()
import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

# Setup LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Setup HID mouse
mouse = Mouse(usb_hid.devices)

#while True:
#for _ in range(64):
while True:
    # Blink LED on
    led.value = True
    # Move mouse right
    # mouse.move(x=20, y=0)
    time.sleep(0.1)

    # Blink LED off
    led.value = False
    # Move mouse left
    # mouse.move(x=-20, y=0)
    time.sleep(1.9)


