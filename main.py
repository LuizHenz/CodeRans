from cryptography.fernet import Fernet
import os
import platform

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

def user_name():
    return os.getenv('USER') or os.getenv('LOGNAME')

so = identificar_so()

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

nome = user_name()
diretorio_path = f'/home/{nome}/Documentos/teste'


key_path = 'key.key'
if os.path.exists(key_path):
    key = load_key(key_path)
else:
    key = generate_key()
    save_key(key, key_path)

for filename in os.listdir(diretorio_path):
    if os.path.isfile(os.path.join(diretorio_path, filename)):
        file_path = os.path.join(diretorio_path, filename)
        output_path = os.path.join(diretorio_path, f'encrypted_{filename}')
        encrypt_file(file_path, key, output_path)
        print(f'Arquivo {filename} criptografado com sucesso.')

        if not filename.startswith('encrypted_'):
            os.remove(file_path)
            print(f'Arquivo original {filename} removido.')

for filename in os.listdir(diretorio_path):
    if filename.startswith('encrypted_'):
        encrypted_file_path = os.path.join(diretorio_path, filename)
        decrypted_file_path = os.path.join(diretorio_path, filename[len('encrypted_'):])
        decrypt_file(encrypted_file_path, key, decrypted_file_path)
        print(f'Arquivo {filename} descriptografado.')


print('Processo de criptografia realizado com sucesso')