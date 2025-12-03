ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ROTOR_I   = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II  = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
ROTOR_IV  = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
ROTOR_V   = "VZBRGITYUPSDNHLXAWMJQOFECK"

REFLECTOR_A = "EJMZALYXVBWFCRQUONTSPIKHGD"
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

def make_inverse_wiring(wiring: str) -> str:
    """Given a wiring string of length 26, return the inverse mapping string."""
    inv = ['?'] * 26
    for i, ch in enumerate(wiring):
        inv[ord(ch) - 65] = ALPHABET[i]
    return ''.join(inv)

def idx(ch: str) -> int:
    return ord(ch) - 65

def letter(i: int) -> str:
    return ALPHABET[i % 26]

class Enigma:
    def __init__(self, rotors:list[str], reflector:str, start_positions=None):
        assert len(rotors) == 3, "Three rotors required"
        self.rotors = rotors[:]              
        self.inv_rotors = [make_inverse_wiring(r) for r in self.rotors]
        self.reflector = reflector
        self.positions = start_positions[:] if start_positions else [0,0,0]

    def reset_positions(self):
        self.positions = [0,0,0]

    def step_rotors(self):
        """Simple stepping: rightmost rotor advances by 1 each keypress (mod 26)."""
        self.positions[2] = (self.positions[2] + 1) % 26
       
    def forward_through_rotor(self, rotor_idx:int, ch:str) -> str:
        """
        Forward direction substitution through one rotor.
        rotor_idx: 0(left) .. 2(right)
        Applies position offset when mapping.
        """
        pos = self.positions[rotor_idx]
        in_index = (idx(ch) + pos) % 26
        wired_char = self.rotors[rotor_idx][in_index]
        out_index = (idx(wired_char) - pos) % 26
        return letter(out_index)

    def reverse_through_rotor(self, rotor_idx:int, ch:str) -> str:
        """
        Reverse direction substitution through one rotor (uses inverse wiring).
        """
        pos = self.positions[rotor_idx]
        in_index = (idx(ch) + pos) % 26
        wired_char = self.inv_rotors[rotor_idx][in_index]
        out_index = (idx(wired_char) - pos) % 26
        return letter(out_index)

    def reflect(self, ch:str) -> str:
        """Reflector mapping (no position offset)."""
        return self.reflector[idx(ch)]

    def encrypt_char(self, ch:str) -> str:
        """Encrypt single uppercase letter. Rotors step BEFORE encryption."""
        self.step_rotors()
        
        c = ch
        for rotor_idx in (2, 1, 0):
            c = self.forward_through_rotor(rotor_idx, c)

        c = self.reflect(c)
       
        for rotor_idx in (0, 1, 2):
            c = self.reverse_through_rotor(rotor_idx, c)

        return c

    def encrypt_row(self, text:str):
        """
        Reset rotor positions to [0,0,0] then encrypt all letters in text.
        Non-letters are passed unchanged.
        Returns converted string and detailed log ((in, out, positions_after_step) per char).
        """
        self.reset_positions()
        out_chars = []
        log = []
        for ch in text:
            if ch.upper() in ALPHABET:
                out = self.encrypt_char(ch.upper())
                out_chars.append(out)
                log.append((ch.upper(), out, tuple(self.positions)))
            else:
                out_chars.append(ch)
                log.append((ch, ch, tuple(self.positions)))
        return ''.join(out_chars), log

def choose_reflector(code:str) -> str:
    code = code.upper()
    if code == 'A':
        return REFLECTOR_A
    if code == 'B':
        return REFLECTOR_B
    if code == 'C':
        return REFLECTOR_C
    raise ValueError("Unknown reflector code. Choose A, B or C.")

def main():
    print("Insert config(filename): (demo uses built-in config)")
    plugs = input("Insert plugs (y/n)?: ").strip().lower()
    if plugs == 'y':
        print("Plugboard prompt acknowledged but plugboard is not implemented in this exercise.")
    else:
        print("No extra plugs inserted.")

  
    rotors = [ROTOR_I, ROTOR_II, ROTOR_III]
    
    refl_choice = input("Choose reflector (A/B/C) [B]: ").strip().upper() or 'B'
    try:
        reflector = choose_reflector(refl_choice)
    except ValueError:
        print("Invalid reflector choice, defaulting to B.")
        reflector = REFLECTOR_B

    enigma = Enigma(rotors, reflector, start_positions=[0,0,0])
    print("Enigma initialized.\n")

    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            print("\nEnigma closing.")
            break
        converted, log = enigma.encrypt_row(row)

        for inp, out, pos in log:
            if inp.upper() in ALPHABET:
                print(f'Character "{inp}" illuminated as "{out}"')
            else:
                print(f'Character "{inp}" passed unchanged as "{out}"')
        print(f'Converted row - "{converted}".\n')

if __name__ == "__main__":
    main()
