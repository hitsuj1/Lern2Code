#Kalkulator Trygonometryczny ver1.
import math #math library

function=str(input("Podaj funkcję: "))
angle=float(input("Podaj kąt(w stopniach): "))
lenght=float(input("Podaj długość boku a(b dla cos): "))

#input and variables

if function=="tg":  
        angle_rad=math.radians(angle)
        print("tg=", round(math.tan(angle_rad)/lenght)) #tg result
elif function=="ctg":
        angle_rad=math.radians(angle)
        print("ctg=", round(math.tan(angle_rad)*lenght)) #ctg result
elif function=="sin":
        angle_rad=math.radians(angle)
        print("sin=", lenght/math.sin(angle_rad)) #sin result
elif function=="cos":
        angle_rad=math.radians(angle)
        print("cos=", lenght/math.cos(angle_rad)) #cos result
else:
        print("Niewłaściwa funkcja") #bad function input

    #działa...ale nie działa xD