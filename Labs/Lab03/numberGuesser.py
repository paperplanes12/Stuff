import random

MIN = 0
MAX = 10
NUM_VALUES = 3

def handle_guess(guess, values):
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present.
    if (values.count(guess) > 0):
        values.remove(guess)
    return values

def find_closest(guess, values):
    # This function should return the closest value
    # to the guessed value.
    return min(values, key=lambda x:abs(x-guess))

def run_game(values):
    # While there are values to be guessed and the user hasn't
    # quit (with 'q'), the game should wait for the user to input
    # their guess and then reveal whether the closest number is
    # lower or higher.
    print(f'Numbers are between {MIN} and {MAX} inclusive. There are {len(values)} values left.')
    check = 0
    while (check == 0):
        guess = input('Guess: ')
        if (guess == 'q'):
            return
        guess = int(guess)
        #if value is inside the list
        if (values.count(guess) > 0):
            print(f'You found {guess}! It was in the list.')
            handle_guess(guess, values)
        else:
            closest = find_closest(guess, values)
            s = ""
            if (closest > guess):
                s = "higher"
            else:
                s = "lower"
            print(f"The closest to {guess} is {s}")

        if (len(values) > 0):
            print(f'There are {len(values)} left.')
        else:
            print('Congratulations! You won!')
            check = 1
        
    print('Thanks for playing! See you soon.')

if __name__ == '__main__':
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
