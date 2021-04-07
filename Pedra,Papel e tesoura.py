import random
a = int(input('faca sua escolha\n'
              '[1] pedra\n'
              '[2] papel\n'
              '[3] tesoura\n'''))
lista = int(random.randint(1, 3))
#papel = 2 / pedra = 3 / tesoura = 1
PC = lista
if a == 1 and PC == 1:
    print('Voce Venceu Pedra bate tesoura')
elif a == 2 and PC == 3:
    print('Voce Venceu Papel engole a pedra')
elif a == 3 and PC == 2:
    print('Voce Venceu Tesoura corta o papel')
elif a == 1 and PC == 2:
    print('VOce perdeu Papel engole a pedra')
elif a == 2 and PC == 1:
    print('Voce perdeu Tesoura corta o papel')
elif a == 3 and PC == 3:
    print('Voce perdeu Pedra bate tesoura')
else:
    print(' Ix!!! empatou jogue outra vez')




