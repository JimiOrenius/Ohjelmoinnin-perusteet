import random
random.seed(1234)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

decor_line = "#" * 25

def main():

    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    player_wins = 0
    player_losses = 0
    player_draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")

        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 3.\n")
            continue

        if choice == 0:
            print("\nResults:")
            print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})")
            print(f"RPS-3PO - wins ({player_losses}), losses ({player_wins}), draws ({player_draws})\n")
            print("Program ending.")
            break

        if choice not in [1, 2, 3]:
            print("Invalid choice. Try again.\n")
            continue

        bot_choice = random.randint(1, 3)
        print("Rock! Paper! Scissors! Shoot!\n")

        print(decor_line)
        if choice == 1:
            print(f"{player_name} chose rock.")
            print(rock)
        elif choice == 2:
            print(f"{player_name} chose paper.")
            print(paper)
        else:
            print(f"{player_name} chose scissors.")
            print(scissors)

        print(decor_line)
        if bot_choice == 1:
            print("RPS-3PO chose rock.")
            print(rock)
        elif bot_choice == 2:
            print("RPS-3PO chose paper.")
            print(paper)
        else:
            print("RPS-3PO chose scissors.")
            print(scissors)
        print(decor_line + "\n")

        if choice == bot_choice:
            chosen = ["rock", "paper", "scissors"][choice - 1]
            print(f"Draw! Both players chose {chosen}.\n")
            player_draws += 1
        elif (choice == 1 and bot_choice == 3) or (choice == 2 and bot_choice == 1) or (choice == 3 and bot_choice == 2):
            if choice == 1 and bot_choice == 3:
                print(f"{player_name} rock beats RPS-3PO scissors.\n")
            elif choice == 2 and bot_choice == 1:
                print(f"{player_name} paper beats RPS-3PO rock.\n")
            else:
                print(f"{player_name} scissors beats RPS-3PO paper.\n")
            player_wins += 1
        else:
            if bot_choice == 1 and choice == 3:
                print(f"RPS-3PO rock beats {player_name} scissors.\n")
            elif bot_choice == 2 and choice == 1:
                print(f"RPS-3PO paper beats {player_name} rock.\n")
            else:
                print(f"RPS-3PO scissors beats {player_name} paper.\n")
            player_losses += 1

if __name__ == "__main__":
    main()