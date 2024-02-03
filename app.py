import sys, webbrowser
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
from PyQt6.QtGui import QFont
from template import Ui_mainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(window)

window.setWindowTitle("Notepad - Editor de Texto")  # Mudando o título da janela
ui.text_edit.setFont(QFont("Arial", 12))


## Funções
def salvar():
    texto = ui.text_edit.toPlainText()
    path = QFileDialog.getSaveFileName(
        None, "Salvar arquivo de texto:", "", "Arquivos de texto (*.txt)"
    )
    if ".txt" not in str(path[0]):
        path_atual = str(path[0]) + ".txt"
    else:
        path_atual = str(path[0])
    with open(str(path_atual), "w") as file:
        file.write(texto)

    file_name = str(path[0]).split("/")

    title = "Notepad - " + str(file_name[-1])
    window.setWindowTitle(title)


def novo():
    if (
        ui.text_edit.toPlainText() != ""
    ):  # Aqui verifico se a caixa de texto está limpa. Oferecendo a opção para salvar
        try:
            salvar()
        except:
            pass
    conteudo = ""
    ui.text_edit.setPlainText(conteudo)


def abrir():
    path = QFileDialog.getOpenFileName(
        None, "Salvar arquivo de texto:", "", "Arquivos de texto (*.txt)"
    )
    arquivo = open(str(path[0]))
    conteudo = arquivo.read()

    file_name = str(path[0]).split("/")

    title = "Notepad - " + str(file_name[-1])
    window.setWindowTitle(title)

    ui.text_edit.setPlainText(conteudo)
    arquivo.close()


def copiar():
    ui.text_edit.copy()


def colar():
    ui.text_edit.paste()


def sobre():
    about = QMessageBox()
    about.setWindowTitle("Olá mundo!")
    about.setText("""Notepad\n\nEste é um bloco de notas simples""")
    about.resize(300, 250)
    about.exec()


def site_qt():
    url = f"https://www.riverbankcomputing.com/static/Docs/PyQt6/"

    webbrowser.open(url)


def autor():
    url = f"https://github.com/elizeubarbosaabreu"

    webbrowser.open(url)


## Botões e ação dos menus
ui.btn_save.clicked.connect(salvar)
ui.actionSalvar.triggered.connect(salvar)
ui.btn_new.clicked.connect(novo)
ui.actionNovo.triggered.connect(novo)
ui.btn_open.clicked.connect(abrir)
ui.actionAbrir.triggered.connect(abrir)
ui.actionCopiar.triggered.connect(copiar)
ui.actionColar.triggered.connect(colar)
ui.actionO_que_isso.triggered.connect(sobre)
ui.actionPyQT6.triggered.connect(site_qt)
ui.actionAutor.triggered.connect(autor)

window.show()
sys.exit(app.exec())
