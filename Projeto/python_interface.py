print('################################################')
print('########## Bem vindo ao poCIntividade ##########')
print('################################################')
print('')


def confere_mensagem(mensagem):
    permissao = input(f'A mensagem {mensagem} é permitida? (y/n) ')
    if permissao == 'y':
        return True
    else:
        return False


while True:
    print('Opcoes:')
    print('sair - fechar o programa')
    print('msg - enviar nova mensagem')
    print('')
    decisao = input()
    if decisao == 'sair':
        break
    elif decisao == 'msg':
        mensagem = input('sua mensagem: ')
        if confere_mensagem(mensagem):
            print(f'Mensagem enviada:\n{mensagem}')
        else:
            print('Mensagem proibida')
    else:
        print('opcao invalida')
    print('')
print('volte sempre')