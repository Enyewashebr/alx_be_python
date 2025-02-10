def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# User interaction
try:
    temperature_input = input("Enter the temperature: ")
    temperature = float(temperature_input)
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

unit_input = input("Is this in Celsius or Fahrenheit (C/F)? ").strip().upper()
if unit_input not in ['C', 'F']:
    print("Invalid unit. Please enter 'C' or 'F'.")
    exit()

if unit_input == 'C':
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is equivalent to {converted:.2f}°F")
elif unit_input == 'F':
    converted = convert_to_celsius(temperature)
    print(f"{temperature}°F is equivalent to {converted:.2f}°C")
