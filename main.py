from cryptography.fernet import Fernet
import platform
import os

def identificar_so():
    sistema = platform.system()
    release = platform.release()

    if 'Windows' in sistema:
        print(f'Sistema Operacional: {sistema}')
        print(f'Release: {release}')
    elif 'Linux' in sistema:
        distro = platform.freedesktop_os_release()
        print(distro['NAME'], distro['VERSION'])
    else:
        print(f'Sistema Operacional não reconhecido: {sistema}')
    
    return sistema


def criar_diretorio(caminho, nome):
    end_comp = os.path.join(caminho, nome)

    try:
        os.makedirs(end_comp)
        print(f'Diretório criado: {end_comp}')
    except OSError as error:
        print(f'Erro: {error}')


so = identificar_so()

if 'Linux' == so:
    endereco = '/home/k4rma/Documentos'
    nome_diretorio = 'teste'
    criar_diretorio(endereco,nome_diretorio)
# else:
#     endereco_win = 'C:\Users\<usuario>\Documents'
#     nome_diretorio_win = 'teste'
#     criar_diretorio(endereco_win,nome_diretorio_win)
