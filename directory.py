import os

def criar_diretorio(caminho, nome):
    end_comp = os.path.join(caminho, nome)

    try:
        os.makedirs(end_comp)
        print(f'Diretório criado: {end_comp}')
    except OSError as error:
        print(f'Erro: {error}')