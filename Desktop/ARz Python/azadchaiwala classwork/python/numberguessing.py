import random
range = input('Enter a number to set a range 🙂 ')
if range.isdigit():
    range = int(range)
    if range <=0:
        print('Please type a number larger than zero 🙄 ')
        quit()
else:
    print('Enter a Number Stupid 😡 ')
    quit()
random_number = random.randint(0,range)
guesses = 0
while True :
    guesses += 1
    user_guess = input('make a guess 🤔 ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print('ENTER A NUMBER STUPID DUMBASS 🤬 ')
        continue
    if user_guess == random_number:
        print('HURRAY! YOU GOT IT 🎉 ')
        break
    else:
        if user_guess>random_number:
            print('You are above the range moron 😑 ')
        elif user_guess>random_number:
            print('You are below the range moron 😑 ')
        else:
            ('checking...')
        print('LOSER TRY AGAIN 💩👎 ')
print('you got it, in',guesses,'guesses')
if guesses == 0 :
    print('🤯 ')

if guesses > 0 and guesses <= 5 :
    print('😁👍 ')

if guesses > 5 and guesses <= 10 :
    print('👍 ')
if guesses > 10 and guesses <= 20 :
    print('💩🤭 ')
