# main.py

import time
import usb_hid
from adafruit_hid.mouse import Mouse
"""
lib/adafruit_hid
"""
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
    print("Clicking the left mouse button...")
    click_mouse(Mouse.LEFT_BUTTON)

    # Example 3: Scroll the mouse wheel up and down
    print("Scrolling the mouse wheel up and down...")
    scroll_mouse(scroll_delta=5)
    time.sleep(1)
    scroll_mouse(scroll_delta=-5)
    time.sleep(1)

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
for _ in range(8):
    # Blink LED on
    led.value = True
    # Move mouse right
    mouse.move(x=20, y=0)
    time.sleep(0.5)

    # Blink LED off
    led.value = False
    # Move mouse left
    mouse.move(x=-20, y=0)
    time.sleep(0.5)


