import random

user_wins = 0
computer_wins = 0

options = ['rock','paper','scissors']
while True :
    user_input = input('type rock/paper/scissors or quit to quit').lower()
    if user_input == 'quit':
        quit()
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computers_pick = options[random_number]
    print('computer picked',computers_pick)
    if user_input == 'rock' and computers_pick =='scissors' :
        print('You win 🥳')
        user_wins +=1
        

    elif user_input == 'paper' and computers_pick =='rock' :
        print('You win 🥳')
        user_wins +=1
        

    elif user_input == 'scissors' and computers_pick =='paper' :
        print('You win 🥳')
        user_wins +=1

    else:
        print('Computer Wins 👤🦾')
        computer_wins +=1

print('GoodBye!')
    
