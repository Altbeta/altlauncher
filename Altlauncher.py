from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import os
import string
import wget
import requests
import xml.etree.ElementTree as ET
import hashlib
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
import base64

XML_URL = "https://altbeta.qwa.su/files/versions.xml"
DOWNLOAD_URL_BASE = "https://altbeta.qwa.su/files/"
UPDATE_URL = "https://altbeta.qwa.su/install.html"
CSV_FILE = 'local_database.csv'
INSTALL_DIR = "C:\\.altbeta"

NAME = "Altlauncher"
VERSION = 0.1
GENERATION = 1

IMG_BASE = "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"
ICO_BASE = "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"
img_data = base64.b64decode(IMG_BASE)



natives = f"{INSTALL_DIR}\\client\\natives"
jars = f"{INSTALL_DIR}\\client\\jutils-1.0.0.jar;{INSTALL_DIR}\\client\\launchwrapper-1.0.jar;{INSTALL_DIR}\\client\\libraryjavasound-20101123.jar;{INSTALL_DIR}\\client\\librarylwjglopenal-20100824.jar;{INSTALL_DIR}\\client\\lwjgl_util-2.9.4.jar;{INSTALL_DIR}\\client\\lwjgl-2.9.4.jar;{INSTALL_DIR}\\client\\rdi-1.0.jar;{INSTALL_DIR}\\client\\soundsystem-20120107.jar;{INSTALL_DIR}\\client\\asm-9.2.jar;{INSTALL_DIR}\\client\\asm-tree-9.2.jar;{INSTALL_DIR}\\client\\codecjorbis-20230120.jar;{INSTALL_DIR}\\client\\codecwav-20101023.jar;{INSTALL_DIR}\\client\\deobfuscated.jar;{INSTALL_DIR}\\client\\jinput-2.0.5.jar;{INSTALL_DIR}\\client\\json-20230311.jar"



libraries = f"{INSTALL_DIR}\\client\\minecraft.jar;{INSTALL_DIR}\\client\\jinput.jar;{INSTALL_DIR}\\client\\lwjgl_util.jar;{INSTALL_DIR}\\client\\lwjgl.jar;"
# libraries = f"{INSTALL_DIR}\\client\\minecraft.jar"
allowed_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_-'
settings = {'session': 12345, 'path_jre_bin': os.environ.get('JAVA_HOME', ''), 'nickname': 'Player'}

def show_error(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.exec_()

def authenticate(user, password, version):
    url = "http://altbeta.qwa.su/game/auth.php"  # замените на URL вашего auth.php
    data = {
        'user': user,
        'password': password,
        'version': version
    }

    response = requests.post(url, data=data)

    if response.text == 'Bad login':
        show_error('Ошибка', 'Неправильное имя пользователя или пароль')
    
    print(response)
    print(response.text)
    
    if response.status_code == 200:
        parts = response.text.split(':')
        username = parts[2]
        session_id = parts[3]


        print(parts)
        print(f'{username}, {session_id}')

        initialize_minecraft(username, session_id)
    else:
        show_error("Error:", f"{response.status_code}")

def start():
    global nickname, password
    nickname_text = nickname.text()
    password_text = password.text()
    if any(char not in allowed_chars for char in nickname_text):
        show_error("Ошибка", "Псевдоним содержит недопустимые символы")
        return
    authenticate(nickname_text, password_text, 13)
    
def check_update():
    response = requests.get(XML_URL)
    if response.status_code == 200:
        with open('versions.xml', 'wb') as file:
            file.write(response.content)
        tree = ET.parse('versions.xml')
        root = tree.getroot()
        latest_version = root.find('version')
        file_name = latest_version.find('file_name').text
        version = int(latest_version.find('version').text)
        md5 = latest_version.find('md5').text
        local_version = 0

        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, 'r') as file:
                local_version = int(file.read().strip())

        if version > local_version:
            download_update(file_name, md5)
            with open(CSV_FILE, 'w') as file:
                file.write(str(version))
    else:
        show_error("Ошибка", "Не удалось получить обновления")

def download_update(file_name, expected_md5):
    file_url = DOWNLOAD_URL_BASE + file_name
    file_path = os.path.join(INSTALL_DIR, file_name)
    wget.download(file_url, file_path)
    if verify_md5(file_path, expected_md5):
        unzip_file(file_path, INSTALL_DIR)
    else:
        show_error("Ошибка", "Контрольная сумма не совпадает")

def verify_md5(file_path, expected_md5):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest().upper() == expected_md5

def unzip_file(file_path, extract_to):
    import zipfile
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def initialize_minecraft(username, sessionid):
    java_home_path = read_file('C:/.altbeta/altfiles/javahome.txt')
    args = read_file('C:/.altbeta/altfiles/args.txt')
    if not java_home_path or not args:
        show_error("Ошибка", "Не удалось прочитать необходимые файлы для запуска")
        return
    java_executable = os.path.join(java_home_path.strip(), "bin", "javaw.exe")
    command = f'"{java_executable}" {args} -Djava.library.path="{natives}" -cp "{libraries}" net.minecraft.client.Minecraft "{username}" "{sessionid}"'
    print(command)
    os.system(f"{command}")
    # subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    exit()

def read_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    return None

def checkfiles():
    if not os.path.isdir('C:/.altbeta/altfiles'):
        os.mkdir('C:/.altbeta/altfiles')
    if not os.path.isfile('C:/.altbeta/altfiles/args.txt'):
        with open('C:/.altbeta/altfiles/args.txt', 'w') as file:
            file.write('-Xms1G -Xmx1G -Xmn512M')
    if not os.path.isfile('C:/.altbeta/altfiles/javahome.txt'):
        with open('C:/.altbeta/altfiles/javahome.txt', 'w') as file:
            java_home = os.environ.get('JAVA_HOME', '')
            if java_home:
                file.write(java_home)
            else:
                show_error('Java не найдена', 'Переменная среды JAVA_HOME не найдена. Укажите путь к Java вручную.')

def main():
    global nickname, password

    app = QApplication(sys.argv)
    root = QWidget()
    root.setWindowTitle(f"{NAME} {VERSION}")
    root.setFixedSize(395, 245)

    txtlogo = QLabel(NAME, root)
    txtlogo.setAlignment(Qt.AlignCenter)
    txtlogo.setStyleSheet("color:white;font-size:48px;font-weight:600;")
    
    nickname = QLineEdit(root)
    password = QLineEdit(root)
    password.setEchoMode(QLineEdit.Password)

    


    canvas_bg = QLabel(root)
    pixmap = QPixmap()
    if not pixmap.loadFromData(img_data):
        print("Не удалось загрузить изображение из данных")
        sys.exit(1)
    canvas_bg.setPixmap(pixmap)
    canvas_bg.setStyleSheet("background-color:#037;")
    canvas_bg.setGeometry(0, 0, 395, 245)
    canvas_bg.lower()

    nickname_label = QLabel('Никнейм: ', root)
    password_label = QLabel('Пароль:  ', root)
    nickname_label.setStyleSheet('color:white;font-family:courier;')
    password_label.setStyleSheet('color:white;font-family:courier;')

    start_button = QPushButton("Играть!", root)
    start_button.clicked.connect(start)
    # start_button.setStyleSheet('font-family:courier;')
    
    settings_button = QPushButton("Настройки", root)
    settings_button.clicked.connect(settings_window)
    # settings_button.setStyleSheet('font-family:courier;')

    nickname_layout = QHBoxLayout()
    nickname_layout.addWidget(nickname_label)
    nickname_layout.addWidget(nickname)

    password_layout = QHBoxLayout()
    password_layout.addWidget(password_label)
    password_layout.addWidget(password)

    layout = QVBoxLayout()
    layout.addWidget(txtlogo)
    layout.addLayout(nickname_layout)
    layout.addLayout(password_layout)
    layout.addWidget(start_button)
    layout.addWidget(settings_button)

    root.setLayout(layout)
    root.show()
    sys.exit(app.exec_())


def settings_window():
    def save_args():
        with open('C:/.altbeta/altfiles/args.txt', 'w') as file:
            file.write(args_entry.text())
        with open('C:/.altbeta/altfiles/javahome.txt', 'w') as file:
            file.write(javahome_entry.text())
        dialog.close()

    def load_args():
        return read_file('C:/.altbeta/altfiles/args.txt') or ''

    def load_javahome():
        return read_file('C:/.altbeta/altfiles/javahome.txt') or ''

    checkfiles()
    args_txt = load_args()
    javahome_txt = load_javahome()

    dialog = QDialog()
    dialog.setWindowTitle(f"{NAME} - Настройки")
    dialog.setFixedSize(275, 165)

    txtlogo = QLabel('Настройки', dialog)
    txtlogo.setAlignment(Qt.AlignCenter)

    args_entry = QLineEdit(dialog)
    args_entry.setText(args_txt)

    javahome_entry = QLineEdit(dialog)
    javahome_entry.setText(javahome_txt)

    save_button = QPushButton("Сохранить", dialog)
    save_button.clicked.connect(save_args)

    layout = QVBoxLayout()
    layout.addWidget(txtlogo)
    layout.addWidget(args_entry)
    layout.addWidget(javahome_entry)
    layout.addWidget(save_button)

    dialog.setLayout(layout)
    dialog.exec_()


main()
