print('################################################')
print('########## Bem vindo ao poCIntividade ##########')
print('################################################')
print('')
print('Opcoes:')
print('sair - fechar o programa')
print('msg - enviar nova mensagem')
print('')

while True:
    decisao = input()
    if decisao == 'sair':
        break
    elif decisao == 'msg':
        input('sua mensagem: ')
    else:
        print('opcao invalida')
    print('')
print('volte sempre')