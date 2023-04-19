from time import sleep


def linha(tam = 42):
    return '-' * tam


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            sleep(1)
            continue

        except (KeyboardInterrupt):
            print('\n\033[31mUsuário não digitou nenhum valor.\033[m')
            sleep(1)
            return 0

        else:
            return num


def fecharPrograma():
    print('-' * 42)
    print('\033[033mFechando o programa'.center(56))
    print('Obrigado por usar\033[m'.center(54))
    print('-' * 42)


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[033mSistema de Menu\033[m'.center(58))
    c = 1

    for item in lista:
        print(f'\033[33m{c} \033[m- \033[34m{item}\033[m')
        c += 1
    print(linha())

    opc = leiaInt('\033[033mDigite sua opção: \033[m')
    return opc
