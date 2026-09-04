# height= float(input("Hur lång är du i meter?"))
# if height < 1.40 or height > 1.95:
#     print("Du kan inte åka på gröna lund")
# else:
#     print("Du kan åka på gröna lund")

try:
    förnamn= input("Vad är ditt förnamn?")
    efternamn= input("Vad är ditt efternamn?")
   
    print("Du heter "+ förnamn +" "+ efternamn + " och du är ")#+ int(age) + " år gammal")
except:
    print("Fel format, skriv bara bokstäver på den första och andra och nummer på den tredje")

     #age= input("Hur gammal är du?")