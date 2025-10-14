print("Welcome to the temp app!")
Temp = int(input("What is the temperature of CPU? "))

if(Temp > 80):
    print("Warning, temperature too high!")
else:
    print("ALL cool, keep on going!")

#Tee ohjelma joka kertoo onko numero parillinen vai pariton.   

num = int(input("insert number: "))
Answer = num % 2
if Answer == 0:
    print(f"parillinen: {Answer}")
else:
    print(f"pariton: {Answer}")



if(Temp > 80):
    if(Temp > 90):
        print("You are toast")
    else:
        print("Warning")
else:
    print("You are ok")

if(Temp > 90):
    print("You are toast")
elif(Temp > 80):
    print("You are toast")
else:
    print("You are ok")

#Tee ohjelma, joka kysyy kahta nimeä. Testaa kumpi nimistä on pidempi, vai onko ne saman mittaisia. Vinkki: len()

name1 = input("Anna nimi 1: ")
name2 = input("Anna nimi 2: ")
if len(name1) > len(name2):
    print("nimi1 on pidempi kuin nimi2")
elif len(name1) < len(name2):
    print("nimi2 on pidempi kuin nimi1")
else:
    print("nimet ovat yhtä pitkät")



Town = "Lahti"
Street = "Mukkulankatu"
Building = 19

if(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print("You are at LAB")
elif(Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):
    print("You are in the correct town, but check the street address again")
elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print("You are completely lost...")


import random

print (random.random())
print(random.randint(1, 10))

# Tee yksinkertainen kivi, sakset, paperi peli random -metodia käyttäen. 

import random
pelaaja = int(input("Pelataan Kivi paperi sakset.\nAnna valintasi:\n1 - Kivi\2 - Paperi\n3 - Sakset\n"))
vastustaja = random.randint(1,3)
print(f"Pelasit {pelaaja}, vastustajasi pelasi {vastustaja}:")
if pelaaja==vastustaja:
    print("tasapeli")
elif(pelaaja==1 and vastustaja==3) or (pelaaja==2 and vastustaja==1) or (pelaaja==3 and vastustaja==2):
    print("Sinä voitit")
else:
    print("vastustaja voitti")
