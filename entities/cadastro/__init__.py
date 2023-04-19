def addCliente(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[031mErro ao inicializar o banco de dados\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[031mErro ao inserir dados\033[m')
        else:
            print('-' * 42)
            print('\033[036mCliente registrado com sucesso\033[m'.center(56))


