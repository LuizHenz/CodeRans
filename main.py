from so import identificar_so
from directory import criar_diretorio

so = identificar_so()

if 'Linux' == so:
    endereco = '/home/k4rma/Documentos'
    nome_diretorio = 'teste'
    criar_diretorio(endereco,nome_diretorio)
# else:
#     endereco_win = 'C:\Users\<usuario>\Documents'
#     nome_diretorio_win = 'teste'
#     criar_diretorio(endereco_win,nome_diretorio_win)

