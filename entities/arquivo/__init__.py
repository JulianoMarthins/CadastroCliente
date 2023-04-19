from time import sleep
import entities.interface
from entities import interface


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        print('\033[036mBanco de dados criado com sucesso\033[m'.center(54))
        a.close()
    except:
        print('\033[31mHouve um erro na criaçao do arquivo\033[m'.center(56))


def bandoDados(cond):
    if cond:
        print('-' * 42)
        print('\033[033mAcessando banco de dados\033[m'.center(56))
        sleep(2)
        print('\033[036mAcesso permitido\033[m'.center(62))
        sleep(1)
    else:
        print('-' * 42)
        print('\033[033mAcessando banco de dados\033[m'.center(56))
        sleep(2)
        print('\033[031mAcesso negado\033[m'.center(62))
        print('-' * 42)
        sleep(2)
        print('\033[033mCriando banco de dados\033[m'.center(62))
        sleep(4)


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[031mErro ao ler o arquivo!\033[m')
    else:
        entities.interface.cabeçalho('Pessoas Cadastradas'.center(50))
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'\033[36mNome: {dado[0]:<26}{dado[1]:>3} anos\033[m')
    finally:
        a.close()
