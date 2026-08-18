import random



def spin_row():
    symbols = ['🏀', '♥️', '🎲', '🎤', '🔔']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("********************")
    print("  |  ".join(row))
    print("********************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🏀":
            return bet * 3
        elif row[0] == "♥️":
            return bet * 5
        elif row[0] == "🎲":
            return bet * 10
        elif row[0] == "🎤":
            return bet * 20
        elif row[0] == "🔔":
            return bet * 7  

    return 0

def main():
    balance = 500

    print("**********************************************")
    print("---------------- Slot machine ----------------")
    print("Symbols: 🏀 | ♥️  | 🎲 | 🎤 | 🔔")
    print("**********************************************")

    while balance > 0:

        print(f"Current Balance: ${balance} ")

        bet = input("Enter the Amount you want to bet: ")

        if not bet.isdigit():
            print("Enter a Valid Number")
            continue

        bet = int(bet)

        if bet > balance:
            print("No sufficient Funds....")
            continue

        elif bet <= 0:
            print("The Bet must be greater than 0")
            continue

        balance-= bet

        row = spin_row()
        print("spinning.....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You Won ${payout}")

        else:
            print("Sorry You lost....")

        balance += payout

        choice = input("You want to play again? ").upper()

        if choice != 'Y':
            break

    print("**********************************************")
    print(f"Game Over! Your Final Balance is: ${balance}")
    print("**********************************************")


if __name__ == '__main__':
    main()