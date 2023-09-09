import random

MAX_LINES= 3 
MAX_BET = 1000
MIN_BET = 10


ROWS = 3 
COLUMNS = 3


symbol_count = { "A": 2, "B" : 4, "C": 6, "D" : 8}

symbol_value = { "A": 5, "B" : 4, "C": 3, "D" : 2}


def checkwinnings(columns, lines, bet, values):
    winnings = 0 
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns: 
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                print("you lose")
                break
        else: 
            winnings += bet* values[symbol]
    return winnings




def get_slotmachine_spin(rows, columns, symbols):
    allsymbols= []
    for symbol,  symbol_count in symbols.items():
        for i in range(symbol_count):
            allsymbols.append(symbol)  # can rewrite

    cols = []

    for col in range(columns): 
        column = []
        currentsymbols = allsymbols.copy()
        for row in range(rows): 
            value = random.choice(currentsymbols)
            currentsymbols.remove(value)
            column.append(value)
        cols.append(column)

    return cols

def print_slotmachine(columns):
    
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): # i is the index and column is the item 
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")         

        print()
        


def deposit():
    while True:
        amount = input("What woud you like to deposit? $")
        if amount.isdigit() == True:
            amount = int(amount)
            if amount>0:
                break 
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
        
    return amount


def get_lines():
    while True:
        lines = input("Enter number of lines to bet on (1- " + str(MAX_LINES) + ")? ") 
        if lines.isdigit() == True:
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break 
            else: 
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
        
    return lines


def getbet():
    while True:
        bet = input("What would you like to bet on each line? $") 
        if bet.isdigit() == True:
            bet = int(bet)
            if MIN_BET<= bet <= MAX_BET:
                break 
            else: 
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
        
    return bet


def main():
    balance = deposit()
    lines = get_lines()

    while True:
        bet = getbet()
        totalbet = bet * lines
        if totalbet>balance:
            print(f"You don't have enough to bet that amount. Your current balance is ${balance}")
        else:
            break 
    print(f"You are betting ${bet} on {lines} lines which comes out to a total of ${totalbet} leaving you with ${balance - totalbet}")
    slots = get_slotmachine_spin(ROWS,COLUMNS,symbol_count)
    print_slotmachine(slots)
    winnings = checkwinnings(slots,lines, bet,symbol_value)
    print(f'You won ${winnings}')
main()