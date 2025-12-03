import os

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

LOCATIONS = ["Home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace"]

PROGRESS_FILE = "player_progress.txt"

def rot13(text: str) -> str:
    """
    ROT13-salaus/purkufunktio (Caesar cipher).
    Siirtää jokaista kirjainta 13 paikkaa eteenpäin aakkosissa.
    Koska aakkosia on 26, sama funktio sekä salaa että purkaa.
    
    Args:
        text: Salattava tai purettava teksti
    
    Returns:
        Salattu tai purettu teksti
    """
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
           
            index = (LOWER_ALPHABETS.index(char) + 13) % 26
            result += LOWER_ALPHABETS[index]
        elif char in UPPER_ALPHABETS:
       
            index = (UPPER_ALPHABETS.index(char) + 13) % 26
            result += UPPER_ALPHABETS[index]
        else:
           
            result += char
    return result

def read_progress():
    """
    Lukee pelaajan edistymistiedoston.
    Jos tiedostoa ei ole olemassa, luo sen alkuarvolla.
    
    Returns:
        Lista tiedoston riveistä
    """
  
    if not os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            f.write("current_location;next_location;passphrase\n")  
            f.write("0;1;qvfpvcyvar\n")  
            

    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def append_progress(line):
    """
    Lisää uuden edistymisrivin tiedoston loppuun.
    
    Args:
        line: Lisättävä rivi (ilman rivinvaihtoa)
    """
    with open(PROGRESS_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def main():
    """
    Pääfunktio: Hallitsee matkan yhteen keisarin palatsiin kerrallaan.
    Lukee edistymisen, matkustaa seuraavaan sijaintiin, lukee viestin ja tallentaa edistymisen.
    """
    print("Travel starting.")
    
    progress_lines = read_progress()

    last_line = None
    for line in reversed(progress_lines):
        line = line.strip()
        if line and ';' in line and not line.startswith('current_location'):
            last_line = line
            break
    
    if not last_line:
        print("Error: No valid progress data found!")
        return
    
    current_id, next_id, passphrase_rot = last_line.split(";")
    current_id = int(current_id)  
    next_id = int(next_id)        

    if next_id >= len(LOCATIONS) or current_id == next_id:
        print(f"Already at final location: {LOCATIONS[current_id]}. No more travel.")
        print("Travel ending.")
        return
    
   
    passphrase_plain = rot13(passphrase_rot)

    print(f"Currently at {LOCATIONS[current_id]}.")
    print(f"Travelling to {LOCATIONS[next_id]}...")
    print(f"...Arriving to the {LOCATIONS[next_id]}.")
    print("Passing the guard at the entrance.")
    print(f'"{passphrase_plain.capitalize()}!"')  
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")

    message_filename = f"{next_id}_{passphrase_rot}.gkg"
    
   
    if not os.path.exists(message_filename):
        sample_message = f"This is a secret message from {LOCATIONS[next_id]}."
        with open(message_filename, "w", encoding="utf-8") as f:
            f.write(rot13(sample_message) + "\n")

    with open(message_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

   
    first_line_ciphered = lines[0].strip()
    append_progress(first_line_ciphered)
    
    print("[Game] Progress autosaved!")
    print("Deciphering Emperor's message...")


    plain_message = ""
    for line in lines:
        plain_message += rot13(line)
    
  
    plain_message_file = f"{next_id}-{passphrase_plain}.txt"
    with open(plain_message_file, "w", encoding="utf-8") as f:
        f.write(plain_message)

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    main()
