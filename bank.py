is_logined = False
is_quit = False
balance = 10000


def withdraw_money():
    global balance
    try:
        w_amount = int(input('How much money you want to withdraw :       '))
        if w_amount > balance:
            print('Your account does not have that much money')
        elif w_amount == 0:
            print('What you are fooling around here')
        else:
            balance -= w_amount
            print(f'{w_amount} has been withrawn from your account your total balance left is {balance}')
            print('')
    except:
        print('Please enter a number')

def deposit_money():
    global balance
    try:
        d_amount = int(input('How much money you want to deposit : '))
        balance = balance + d_amount
        print(f'{d_amount} has been deposited to your account your total balance is {balance}')
        print('')
    except:
        print('Please enter a number')

def show_balance():
    print(f'Your balance is {balance}')
    print('')

def start():
    while is_quit == False:
            res = input('Press w for withdraw and d to deposit and b to show your balance : ')
            if res == 'w':
                withdraw_money()
            elif res == 'd':
                deposit_money()
            elif res == 'b':
                show_balance()
            elif res == 'help':
                print('Press w for withdrawing money')
                print('Press d for depositing money')
                print('Press b for showing your balance')
                print('Press q for showing quiting the program')
            elif res == 'q':
                break
            else:
                print('Enter a correct value from given type help for commands')

start()
