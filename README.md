## Aviso: 
Este código é fornecido apenas para fins de estudo. Não assumo responsabilidade pelo uso indevido ou por quaisquer danos causados a terceiros. Use por sua própria conta e risco.

### Crie um ambiente virtual e ative-o:
```
python3 -m venv venv

source venv/bin/activate
```
### Instale o PyInstaller:
```
pip install pyinstaller
```
### Instale as dependências do projeto:
```
pip install -r requirements.txt
```
### Gere o executável com PyInstaller:
```
pyinstaller --onefile --add-data "requirements.txt:." main.py

pyinstaller --onefile --add-data "requirements.txt:." --add-data "install_deps.sh:." --add-data "pacote:./pacote" main.py
```
 Os executáveis serão gerados no diretório 'dist'.
