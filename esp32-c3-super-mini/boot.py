import uasyncio as asyncio
from machine import Pin

# Define the LED pin
led = Pin(8, Pin.OUT)

# Coroutine to blink the LED every second
async def blink_led():
    while True:
        led.value(not led.value())  # Toggle LED state
            
        if led.value():
            await asyncio.sleep(.9)      # Pause the coroutine for .9 second
        else:
            await asyncio.sleep(.1)      # Pause the coroutine for .1 second
# Coroutine for a background task (e.g., checking a sensor)
async def background_task():
    while True:
        print("Checking for background events...")
        # Simulate a task that takes some time
        await asyncio.sleep(5)
        
# Main function to run the event loop
async def main():
    # Create and schedule the coroutines to run
    task1 = asyncio.create_task(blink_led())
    task2 = asyncio.create_task(background_task())
    
    # Wait for the tasks to finish (which they won't in this case)
    await asyncio.gather(task1, task2)

# Start the event loop
asyncio.run(main())