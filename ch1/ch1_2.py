print(" *** Wind classification ***")
v = float(input("Enter wind speed (km/h) : "))
if v >= 209:
    print("Wind classification is Super Typhoon.")
elif v > 102:
    print("Wind classification is Typhoon.")
elif v > 56:
    print("Wind classification is Tropical Storm.")
elif v > 52:
    print("Wind classification is Depression.")
elif v > 0:
    print("Wind classification is Breeze.")