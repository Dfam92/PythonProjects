from random import randint
from time import sleep
def linhas(a):
    print(f'\33[32m{(len(a)+4)*"-"}')
    print('',"\033[7;31m",a,"\033[m" )
    print(f'\33[32m{(len(a)+4) * "-"}\33[m')
    """The Text will be underlined and  with red background"""


listj = []
listpc = []
try:
    linhas('Seek And Destroy')
    for c in range(1,4):
        a = int(input(f'Choose the {c}° number between 1 and 10 for play!!!\n'))
        sleep(0.1)
        if 0 < a < 11:
            listj.append(a)
            print('Added')
            print()
        else:
            a = x
            break
    print(listj)
    for c in range (0,3):
        b = randint(1,10)
        listpc.append(b)
    print(listpc)
    while True:
        print(f'You Have {len(listj)} Lifes')
        print()
        print(listj)
        t = int(input('Play one number\n'))
        sleep(0.5)
        print()
        if t in listpc:
            listpc.remove(t)
            print(f'You Hitted the PC! Now he have {len(listpc)} lives')
            sleep(0.5)
            print()
        if len(listpc) == 0:
            print('You defeated the dreaded Computer, Well Played!')
            sleep(0.5)
            print()
            break
        print(f'The PC still have {len(listpc)} lives')
        print()
        print(listpc)
        sleep(0.5)
        p = randint(1,10)
        print(f'The PC played {p}')
        sleep(0.5)
        print()
        if p in listj:
            listj.remove(p)
            print(f'You are Hitted By PC, Now you have {len(listj)} lifes')
            sleep(0.5)
            print()
        if len(listj) == 0:
            print('You were defeated By The Evil PC, try again and beat him!')
            sleep(0.5)
            print()
            break
except ValueError:
    print('Something strange Happen, please Try Again!')
except NameError:
    print('You Played a wrong number,  please open the game again!')
finally:
    print('Good Game!')
