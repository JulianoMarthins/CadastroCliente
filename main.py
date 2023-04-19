from time import sleep
import entities.arquivo, entities.cadastro, entities.interface


print('-' * 42)
print('\033[033mProgramdo por JulianoMarthins\033[m'.center(50))


arquivo = 'cadastroPessoas.txt'

if entities.arquivo.arquivoExiste(arquivo):
    cond = True
    entities.arquivo.bandoDados(cond)
else:
    cond = False
    entities.arquivo.bandoDados(cond)
    entities.arquivo.criarArquivo(arquivo)


while True:
    resposta = entities.interface.menu(['Casdastrar Clientes', 'Listar Clientes', 'Sair do Programa'])

    if resposta == 1:
        entities.interface.cabeçalho('\033[033mNovo Cliente\033[m'.center(60))
        nome = str(input('Nome: '))
        idade = entities.interface.leiaInt('Idade: ')
        entities.cadastro.addCliente(arquivo, nome, idade)

    elif resposta == 2:
        entities.arquivo.lerArquivo(arquivo)
    elif resposta == 3:
        entities.interface.fecharPrograma()
        break

    else:
        print('\033[031mErro! Digite o número das opções válidas\033[m')
        sleep(1)
