def FahrenToCelcius(f):
    c = 5/9*(f - 32)
    return c
f = int(input("Enter temperature in Fahrenheit"))
print(FahrenToCelcius(f))
print("Got It")