from random import randint
from time import sleep
def linhas(a):
    print(f'\33[32m{(len(a)+4)*"-"}')
    print('',"\033[7;31m",a,"\033[m" )
    print(f'\33[32m{(len(a)+4) * "-"}\33[m')
    """O texto escrito ficara entre sublinhado e soblinhado alem de ter uma coloracao avermelhada ao fundo"""


listj = []
listpc = []
try:
    linhas('Seek And Destroy')
    for c in range(1,4):
        a = int(input(f'Escolha o {c}° numero de 1 a 10 para jogar!!!\n'))
        sleep(0.1)
        if 0 < a < 11:
            listj.append(a)
            print('Adicionado')
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
        print(f'Voce tem {len(listj)} Vidas')
        print()
        print(listj)
        t = int(input('Digite um numero\n'))
        sleep(0.5)
        print()
        if t in listpc:
            listpc.remove(t)
            print(f'Voce acertou o PC! Agora ele tem {len(listpc)} vidas')
            sleep(0.5)
            print()
        if len(listpc) == 0:
            print('Voce Derrotou o temido computador, Grande Jogo!')
            sleep(0.5)
            print()
            break
        print(f'O PC esta com {len(listpc)} vidas')
        print()
        print(listpc)
        sleep(0.5)
        p = randint(1,10)
        print(f'O PC escolheu {p}')
        sleep(0.5)
        print()
        if p in listj:
            listj.remove(p)
            print(f'O PC te acertou, agora voce tem {len(listj)} vidas')
            sleep(0.5)
            print()
        if len(listj) == 0:
            print('Voce derrotou o temido PC parabens')
            sleep(0.5)
            print()
            break
except ValueError:
    print('Voce digitou algo estranho, abra o jogos novamente!')
except NameError:
    print('Voce digitou um numero invalido, abra o jogos novamente!')
finally:
    print('Bom jogo!')
