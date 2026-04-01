# Nom: Maksym Bicz
# Ce programme convertit une température Celsius en Fahrenheit et Kelvin.

c = float(input("Température en Celsius: "))

f = (c * 9 / 5) + 32
k = c + 273.15

print("Fahrenheit:", f)
print("Kelvin:", k)