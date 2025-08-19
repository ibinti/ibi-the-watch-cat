# magsafe power

With the help of buck converters, I think the MagSafe power adapters that outlived their respective MacBooks can become excellent power sources for the 5V robotics projects.

why magsafe has 5 pins?

The classic Apple MagSafe connector for MacBooks has five pins. 🔌 The pins serve specific functions to ensure a safe and efficient charge. The design also allows for the connector to be reversible, meaning it can be plugged in facing either direction.

MagSafe Pin Functions

Outer Pins: The two outer pins are for ground. They are slightly longer than the others, which ensures they make contact first when you plug in the connector.

Inner Pins: The two inner pins provide the V+ (positive voltage) to the laptop. They deliver the power needed to charge the battery and run the computer.

Center Pin: The tiny center pin is the "adapter sense" or "charge control" pin. It's a data line that allows the MacBook to communicate with the power adapter. This is what enables the laptop to:

Identify the wattage of the power adapter.

Change the color of the LED light on the connector (orange for charging, green for full).

Access the adapter's serial number.

The symmetrical arrangement of the power and ground pins allows the connector to be plugged in either way. This is a key part of the MagSafe design, which eliminates the need to fumble with the connector and reduces wear and tear on the port.

This video explains what MagSafe is, how it works, and shows a teardown of the MagSafe connector to reveal its inner workings.

can i use geound and v+ pins for my other devices that has buck converter for 5v use

Yes, it's possible to use the ground and V+ pins from a MagSafe adapter for other devices, but you can't just plug them in and expect a stable voltage. The MagSafe power brick is not a simple power supply. The adapter's output voltage is not constant and will only switch to its full, higher voltage (like 14.5V to 20V depending on the model) after it detects a specific resistive load on its data pin.

How to Get the Full Voltage

To use the MagSafe adapter as a power source, you must "trick" it into providing its full voltage. This is typically done by connecting a resistor between the ground and data pins.

Resistor Value: The required resistance is around 39 kΩ (kilohms) for most MagSafe adapters.

Safety Precaution: The adapter initially outputs a low voltage (around 3V to 6V) to prevent shorts. Once it detects the proper load from the resistor, it will switch to the full, higher voltage. This is a built-in safety feature.

Once you've successfully triggered the full voltage, you can connect the output to a buck converter to step the voltage down to 5V for your devices. A buck converter is a DC-to-DC power converter that efficiently lowers voltage while stepping up the current.


https://www.righto.com/2015/11/macbook-charger-teardown-surprising.html

https://github.com/jonathonlui/magsafe-trigger
