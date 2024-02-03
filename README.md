
# NOTEPAD

Este é um aplicativo simples em python usando pyqt6, cuja única função é criar ou ler um arquivo de texto. Também apresenta ferramentas integradas para copiar e colar trechos de textos. O tema do aplicativo acompanha o tema do sistema.

![Tema Claro visualizado no Kubuntu](/images/captura_de_tela_light.png)
![Tema escuro](/images/captura_de_tela.png)

## Instalação

- Baixe o repositório com o comando 
~~~python
git clone https://github.com/elizeubarbosaabreu/Notepad-Editor-De-Texto-Em-Python.git
~~~
- Navegue até o repositório e crie um Ambiente de Desenvolvimento Local (env) e executar o **app.py**.
~~~python
cd Notepad-Editor-De-Texto-Em-Python/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
python3 app.py
~~~
- No windows o comando para acessar o Ambiente de Desenvolvimento Local (env) muda um pouco:
~~~python
source env\Scripts\activate
~~~
- A forma de executar também pode variar em alguns sistemas operacionais...

## Transformando o Notepad em um software portátil
- Você pode converter qualquer arquivo python em executável utilizando o **pyinstaller**. Leia a documentação dele [neste link](https://pyinstaller.org/en/stable/).
- Instale o pyinstaler dentro do Ambiente de Desenvolvimento Local:
~~~shell
pip install pyinstaller
~~~
Crie o executável:
~~~shell
pyinstaller --onefile app.py
~~~
- Perceba que dentro da pasta/diretório do projeto foram criados duas pastas/diretórios: *buid e dist*
![terminal](/images/terminal.png)
- Dentro da pasta/diretório está o arquivo **app** ou **app.exe** que é o nosso executável portátil. Dá para criar um atalho para ele ou copiar ele para um outro diretório, pendrive, etc...

## Obrigado por aprender junto comigo!