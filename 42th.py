# Python Slot Machine

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0
    
def main():
    balance = 100

    print("**************************")
    print(" Welcome to Python Slots  ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐ ")
    print("**************************")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Balance")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("spinning")
        print("spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You Won ${payout}")
        else:
            print("Sorry you lost the round")    

        balance += payout    

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break
  print("********************************************")
  print(f"Game Over! Your final balance is $(balance)")
  print("********************************************")

if __name__ == '__main__':    
    main()
    
