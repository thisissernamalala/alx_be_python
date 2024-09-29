FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32.0) *FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32.0

temp = int(input("Enter the temperature to convert: "))
val = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if val == "C":
 faren = convert_to_fahrenheit(temp)
 print(f"{temp}°C is {faren}°F")

elif val == "F":
 faren = convert_to_celsius(temp)
 print(f"{temp}°F is {faren}°C")