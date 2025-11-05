import os

# Vakiot aakkostoille ROT13-salausta varten
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Lista sijainneista (indeksi = sijainnin ID)
LOCATIONS = ["Home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace"]
# Tiedosto, johon pelaajan edistyminen tallennetaan
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
            # Pienille kirjaimille: etsi indeksi, lisää 13, käytä modulo 26
            index = (LOWER_ALPHABETS.index(char) + 13) % 26
            result += LOWER_ALPHABETS[index]
        elif char in UPPER_ALPHABETS:
            # Isoille kirjaimille: sama prosessi
            index = (UPPER_ALPHABETS.index(char) + 13) % 26
            result += UPPER_ALPHABETS[index]
        else:
            # Muut merkit (välilyönnit, välimerkit jne.) säilyvät ennallaan
            result += char
    return result

def read_progress():
    """
    Lukee pelaajan edistymistiedoston.
    Jos tiedostoa ei ole olemassa, luo sen alkuarvolla.
    
    Returns:
        Lista tiedoston riveistä
    """
    # Jos tiedostoa ei ole, luo se alkuarvoilla
    if not os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            f.write("current_location;next_location;passphrase\n")  # Otsikkorivi
            f.write("0;1;qvfpvcyvar\n")  # Alkudata: kotona, seuraavana Galban palatsi
    
    # Lue ja palauta kaikki rivit
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
    
    # Lue nykyinen edistymistilanne tiedostosta
    progress_lines = read_progress()

    # Etsi viimeinen validi data-rivi (jossa on puolipisteet)
    last_line = None
    for line in reversed(progress_lines):
        line = line.strip()
        # Ohita tyhjät rivit ja otsikkorivi
        if line and ';' in line and not line.startswith('current_location'):
            last_line = line
            break
    
    # Jos validia riviä ei löydy, virhetilanne
    if not last_line:
        print("Error: No valid progress data found!")
        return
    
    # Pura viimeisen rivin tiedot
    current_id, next_id, passphrase_rot = last_line.split(";")
    current_id = int(current_id)  # Nykyinen sijainti (numero)
    next_id = int(next_id)        # Seuraava kohde (numero)

    # Tarkista, olemmeko jo viimeisessä sijainnissa
    if next_id >= len(LOCATIONS) or current_id == next_id:
        print(f"Already at final location: {LOCATIONS[current_id]}. No more travel.")
        print("Travel ending.")
        return
    
    # Purkaa salattu salasana (ROT13 toimii molempiin suuntiin)
    passphrase_plain = rot13(passphrase_rot)

    # Tulosta matkan tiedot
    print(f"Currently at {LOCATIONS[current_id]}.")
    print(f"Travelling to {LOCATIONS[next_id]}...")
    print(f"...Arriving to the {LOCATIONS[next_id]}.")
    print("Passing the guard at the entrance.")
    print(f'"{passphrase_plain.capitalize()}!"')  # Huuda salasana vartijolle
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")

    # Muodosta salatun viestitiedoston nimi
    message_filename = f"{next_id}_{passphrase_rot}.gkg"
    
    # Jos tiedostoa ei ole, luo esimerkkiviesti (varmuuden vuoksi)
    if not os.path.exists(message_filename):
        sample_message = f"This is a secret message from {LOCATIONS[next_id]}."
        with open(message_filename, "w", encoding="utf-8") as f:
            f.write(rot13(sample_message) + "\n")

    # Lue salattu viesti tiedostosta
    with open(message_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Ensimmäinen rivi sisältää seuraavan sijainnin tiedot (salattu)
    # Lisää se edistymistiedostoon sellaisenaan
    first_line_ciphered = lines[0].strip()
    append_progress(first_line_ciphered)
    
    print("[Game] Progress autosaved!")
    print("Deciphering Emperor's message...")

    # Purkaa koko viesti (kaikki rivit) selkokielelle
    plain_message = ""
    for line in lines:
        plain_message += rot13(line)
    
    # Tallenna purettu viesti tiedostoon
    plain_message_file = f"{next_id}-{passphrase_plain}.txt"
    with open(plain_message_file, "w", encoding="utf-8") as f:
        f.write(plain_message)

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    main()