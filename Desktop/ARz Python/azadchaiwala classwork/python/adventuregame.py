name = input('Type your username: ')
print('🎄WELCOME TO MY ADVENTURE GAME ',name,' 🎄')
print('You are playing this game to save the princess, be the king and live happily ever after or DIE ☠️')
answer = input('You are on a dirt road 🛣️, it has two ways 🔀 , select left ◀ or right ▶: ').lower()
if answer == 'left':
    answer = input('you came across a river, Type swim to swim 🏊‍♀️ and walk to walk around 🚶').lower()
    if answer in 'swim':
        print('As you were swimming 🏊‍♀️, the shark ate 🦈 you and you died ☠️')
    elif answer in 'walk':
        print('As you were walking 🚶 you encountered a wehsi nigga 👨🏿 and he started running after you with a gun 🔫🏃🏾‍♂️ ')
        answer = input('do you wanna fight the wehshi nigga 🤼  or run away 🏃, type fight to fight or run to run away').lower()
        if answer == 'fight':
            print('you fought the nigga 🤼 but the wehshi nigga 🔫🏃🏾‍♂️ killed you ☠️, it is a shame that you lost to the nigga')
        elif answer == 'run':
            print('you ran away from the nigga but you encountered a wild bear 🐻 ahead')
            answer = input('Now do you want to fight the nigga 🤼 or fight the bear 🐻, Type nigga to fight the nigga or type bear to fight the bear').lower()
            if answer == 'nigga':
                print('you fought the nigga 🤼 but the wehshi nigga 🔫🏃🏾‍♂️ killed you ☠️, it is a shame that you lost to the nigga')
            elif answer == 'bear':
                print('you fought the bear 👨‍🔧🐻 but the bear 🐻 killed you ☠️, atleast you didnt die by a nigga')
            else:
                ('invalid option . YOU DIED ☠️')
        else:
            print('invalid option . YOU DIED ☠️')
    else:
        print('invalid option . YOU DIED ☠️')

elif answer == 'right':
    print('you chose right, now as you are walking you came across a weapon wizard ')
    answer = input('The wizard asks you if you needed a weapon, Type Weapon to select a weapon or No to not equip a weapon').lower()
    if answer == 'weapon':
        print('The wizard gives you two options , The Ultimate Sword or The Ultimate Spear')
        answer = input('Type sw to equip the sword or sp to equip the spear').lower()
        if answer == 'sw':
            print('you chose THE ULTIMATE SWORD and you encounter the commander of the slaying dragon and he is a red devil with a strong weapon , if you win your weapon will upgrade')
            print('You managed to kill the red devil and you ULTIMATE SWORD upgraded')
            print('You move forward and encounter the strongest after the slaying dragon')
            print('He is a very powerful man with a lot of power, and you fight him')
            print('It was a close fight and you won and your weapon upgraded')
            print('Now your ULTIMATE slaying dragon and you could see the princess on the tower window crying for help')
            answer = input('the dragon offers you wealth,Type Yes to accept the offer or No to reject the offer').lower()
            if answer == 'yes':
                print('You said yes but the slaying dragon betrayed you and you died')
            elif answer == 'no':
                print('You said No and fought the dragon')
                print('you both fought hard ')
                print('you are the verge of death do you want to try winning or just die without dying')
                answer = input('type try to try or accept your fate and type fate').lower()
                if answer == 'try':
                    print('you try but you didnt have the power of love and you die as the dragon was too strong')
                elif answer == 'fate':
                    print('You are having Flashbacks of your life and you are dying')
                    print('you hear the princess crying and your aderline rush your sword absorbs the power of love as a hidden power and upgrade')
                    print('For the princess you wake up and throw your sword with full strenght as a final blow')
                    print('the slaying dragon dies and you have won')
                    print('You become the king and become wealthy and marry the princess and live happily ever after')
                else:
                    print('invalid option . YOU DIED ☠️')
            else:
                print('invalid option . YOU DIED ☠️')          
            

        elif answer == 'sp':
            print('you chose THE ULTIMATE SPEAR and you encounter the commander of the slaying dragon and he is a red devil with a strong weapon , if you win your weapon will upgrade')
            print('You managed to kill the red devil and you ULTIMATE SPEAR upgraded')
            print('You move forward and encounter the strongest after the slaying dragon')
            print('He is a very powerful man with a lot of power, and you fight him')
            print('You were close but the man won and laughed over your pityful death')
        else:
            print('invalid option . YOU DIED ☠️')
    elif answer == 'no':
        print('Now you didnt take the weapon and you encounter the commander of the slaying dragon and he is a red devil with a strong weapon , if you win your weapon will upgrade ')
        print('You tried to fight the red devil but lost')
    else:
        print('invalid option . YOU DIED ☠️')
else:
    print('invalid option . YOU DIED ☠️')