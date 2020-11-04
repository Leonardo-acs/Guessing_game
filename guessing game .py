import random
name = str((input('HI, what is your name ? ')))
print(f'Well, {name}, i am thinking in a number between 1 and 20.')
secretnumber = random.randint(1,20)
cont = 6

#ask the player to guess 6 times
print('You have six chances, take a guess:')
for guesses in range(1,7):
    guess = int(input())
    if guess > secretnumber :
        print('Your guess is too high',end=', ')
        print(f'now you have {cont - guesses} guesses:')
    elif guess < secretnumber :
        print('Your guess is too low',end=', ')
        print(f'now you have {cont - guesses} guesses:')
    else :
        break # rigth guess
if guess == secretnumber :
    print(f'Good job {name} you guessed my number in {guesses} guesses!')
else:
    print(f'YOU LOSE,the number i was thinking of was {str(secretnumber)}')
