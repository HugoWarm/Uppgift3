import random

height= float(input("Hur lång är du i meter?"))
if height < 1.40 or height > 1.95:
    print("Du kan inte åka på gröna lund")
else:
    print("Du kan åka på gröna lund")

förnamn= input("Vad är ditt förnamn?")
efternamn= input("Vad är ditt efternamn?")

try:
    age= int(input("Hur gammal är du?"))
   
    print("Du heter "+ förnamn +" "+ efternamn + " och du är ")
    print("Du är", age, "år gammal")
except:
    print("Fel format, skriv bara nummer")


print("Skriv in din vikt i kg och längd i meter så kan vi räkna ut ditt bmi.")
try:
    längd= float(input("Din längd i meter"))
    vikt= int(input("Din vikt i kg"))
    print("Din bmi är",vikt/längd**2)
except:
    print("Skriv längd i meter och vikt i kg.")


try:
    radius = float(input("Skriv radien på din cirkel i cm."))
    print("Din cirkel har arean",3.14*radius**2,"cm^2")
except:
    print("Skiv inte bokstäver.")


dice = random.randint(1,6)

print(dice)

try:
    numb = int(input("Hur många tärningar vill du slå?"))
    for i in range(1,numb+1):
        print("Tärning",str(i) + ":",random.randint(1,6))
except:
    print("Skriv bara siffra")
