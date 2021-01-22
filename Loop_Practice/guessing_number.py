import random

random_number = random.randint(0,10)
x = None

# start with guessing number
def start_game(random_number,x):
    while x != random_number:
        x = int(input('Please Enter a number between 1 to 10\n'))
        # if it's too high tell users to their number is too low
        if x > random_number:
            print('Your number is Too high, please guess lower.')
        elif x < random_number:
            print('Your number is Too low, please guess higher.')

    ask = input('Do yout wanna play again or not Y/N').upper()
    if ask == 'Y':
        random_number = random.randint(0,10)
        x = None
        start_game(random_number,x)
    elif ask == 'N':
        print('hope to see you next time')
    else:
        print('Please type Y/N\n')


start_game(random_number,x)
