#slot machine
import random

def spin_row():
    symbols = ["🍋", "🍊", "🍒", "🍇", "⭐️"]
    return [random.choice(symbols) for symbol in range(3)]
    
    # results = [ ]
    #for symbol in range(3):
     #   results.append(random.choice(symbols))
    #return results

#or list comprehension
# return [random.choice(symbols)for symbol in range(3)]
# ^ what this says: for every iteration in range 3 return a random symbol

def print_row(row):
    print(" | ".join(row)) #" " is a separater for list, .join() tells you to join each iterable by a bar


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍋":
            return bet * 3
        elif row[0] == "🍊":
            return bet * 4
        elif row[0] == "🍇":
            return bet * 5
        elif row[0] == "⭐️":
            return bet * 10
    return 0

def main():
    balance = 100
    print("----------------------------------\n🍋🍊🍒🍇🫐  Slot Machine 🍋🍊🍒🍇🫐\n----------------------------------")
    print("   Your symbols are: 🍋🍊🍒🍇⭐️\n----------------------------------")

    while balance > 0:

        print(f"\nYour current balance is ${balance}\n")
        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("\nEnter a valid number\n")
            continue

        bet = int(bet)

        if bet > balance:
            print("\nInsufficient funds\n")
            continue

        if bet <= 0:
            print("\nBet must be greater than 0)\n")
            continue

        if bet > 0 and bet < balance:
            balance -= bet
            row = spin_row()
            print("Spinning...\n")
            print_row(row)
# if all 3 symbols match calculate a pay out and give to user
            payout = get_payout(row, bet)

            if payout > 0:
                print(f"You won ${payout}")
            else:
                print("Sorry, you lost this round")
            balance += payout

# when someone wins or runs out of money stop program

            playagain = input("\nDo you want to play again? (Y/N): ").upper()
            if playagain != "Y":
                break
            print(f"Game over. Your final balance is: ${balance}")






if __name__ == "__main__":
    main()