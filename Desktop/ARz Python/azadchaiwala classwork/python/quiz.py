print('Welcome to my Quiz ')

playing = input('Do you wanna play?,just answer in yes or no ')

if playing.lower() != 'yes' :
    print('🤬 🖕')
    quit()
    
print('Okay, lets play 🤗')
score = 0

print('Question 1')
answer = input('what does CPU stands for ? ')
if answer.lower() == 'central processing unit':
    print('Correct! 🤩 ')
    score += 1
else:
    print('incorrect 😣 ')
    print('better luck next time 😗 ')


print('Question 2')
answer = input('what does RAM stands for ? ')
if answer.lower() == 'random access memory':
    print('Correct! 🤩 ')
    score += 1
else:
    print('incorrect 😣 ')
    print('better luck next time 😗 ')


print('Question 3')
answer = input('How many basic logical operators are there ? ')
if answer.lower() == 'three':
    print('Correct! 🤩 ')
    score += 1
else:
    print('incorrect 😣 ')
    print('better luck next time 😗 ')

print('you got '+str( score) +'questions correct')
print('your percentage is '+str( (score/3)*100) +'%')

if score >2:
    print(' 😍🎉 ')

if score ==2:
    print(' 🙂👌 ')

if score ==1:
    print(' 😐👍 ')

if score ==0:
    print(' 😳👎 ')
