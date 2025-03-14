import math  # math library #math library

function = input("Podaj funkcję: ")
angle = float(input("Podaj kąt(w stopniach): "))
length = float(input("Podaj długość boku a(b dla cos): "))

# input and variables

angle_rad = math.radians(angle) #radian conversion

if function == "tg":
    print("tg =", round(math.tan(angle_rad) * length, 4))  # tg result
elif function == "ctg":
    print("ctg =", round(length / math.tan(angle_rad), 4))  # ctg result
elif function == "sin":
    print("sin =", round(length / math.sin(angle_rad), 4))  # sin result
elif function == "cos":
    print("cos =", round(length / math.cos(angle_rad), 4))  # cos result
else:
    print("Niewłaściwa funkcja")  # bad function input

#works like a charm now :) need to add some restrictions about angle and loop it
