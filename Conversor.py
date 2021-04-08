n = int(input('\033[4;34mDigite um numero  \n'))
print('Escolha um das bases para conversao: \n'
'[ 1 ] BINARIO \n'
'[ 2 ] Hexadecimal\n'
'[ 3 ] Octal\n''')
opcao = (int(input('Sua opcao ')))
if opcao == 1:
    print('O valor em Binario e {}'.format(bin(n)))
elif opcao == 2:
    print(' O valor em Hexadecimal e {}'.format(hex(n)))
elif opcao == 3:
    print(' O valor em octal e {}'.format(oct(n)))
else:
    print('Tente novamente, numero invalido')