print("Program starting.")
print("") #tyhjärivi myös \n käy
WordCount = 0
CharCount = 0
#kirjain ja sanalaskurit alkaa 0

Word = input("Insert word (empty stops): ")
while Word != "":
    WordCount += 1
    CharCount += len(Word)
    Word = input("Insert word (empty stops): ")

print("\nYou inserted:")
print(f"- {WordCount} words")
print(f"- {CharCount} characters\n")

print("Program ending.")

#while-loop kun haluat toistaa jotain niin kauan kuin jokin ehto on tosi
#for-loop yleensä lun tiedät etukäteen, montako kertaa haluat toistaa jotain
#While true on ikuinen silmukka joka toistuu kunnes sen itse pysäyttää
#Break - loptettaa silmukan kokonaan
#continue - hyppää seuraavaan kierrokseen