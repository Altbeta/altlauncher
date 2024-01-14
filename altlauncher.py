from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import threading as thr
import zipfile
import shutil as su
import wget
import os
import xml.etree.ElementTree as ET
import webbrowser

name = "Altlauncher"
version = "0.0"
release = ""
build2 = '2'
libraries = "client/minecraft.jar;client/jinput.jar;client/lwjgl_util.jar;client/lwjgl.jar;"
special_chars = ['@', "'", '"', '№', '#', '$', ';', '%', '^', ':', '&', '?', '*', '(', ')', '{', '}', '[', ']', '|', '/', ',', '`', '~', '\\', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', ' ']

info_title = "Инфо"
warning_title = "Внимание!"
error_title = "Ошибка!"
ask_title = warning_title

err_spaceInNicknameerr_SpaceInNickname = "В полях не должно быть пробелов!"
err_SpecialCharactersInNickname = "В полях не должно быть спец символов!"
err_FailedToCreateClientDirectory = "Создать директорию client не удалось"
err_NoInternetConnection = "Отсутствует подключение к интернету..."
err_UpdateUnavailable = "Автоматическое обновление пока что недоступно в ващей операционной системе"

warn_NoClientInstalled = "Отсутствует клиент!"
warn_FunctionUnavailable = "Данная функция пока недоступна, ждите обновления!"
warn_FileNotFoundOnServerIgnoring = "Указанный файл отсутствует на сервере, игнорируем..."
warn_FirstLaunchMessage = "Это ваш первый запуск лаунчера, пожалуйста, выберите и скопируйте путь к папке bin в папке java!"

info_AutomaticDownloadingClient = "Секунду, сейчас всё скачаем..."
info_DownloadFinished = "Загрузка завершена"
info_DownloadStarted = "Ждите уведомления об окончании загрузки"

ask_AvailableUpdate = "Доступно обновление! Хотите скачать?"

xmlerr_NoInternetConnectionFoundTitle = "Отсутствует интернет!"
xmlerr_NoInternetConnectionFoundDescription = "Такое случается, поэтому предлагаем вам поиграть\nв \"Оффлайн режиме\" (при условии что вы скачали клиент) :3"

websiteForDownload = 'https://atarwn.github.io/abl'

workingDirectory = '.altbeta'

label_ContactLinkDescription = "По всем вопросам на наш Discord сервер:"
label_ContactLink = "https://discord.gg/5x5N6a4nUX"












if not os.path.exists("res"):
    os.mkdir("res")
elif not os.path.exists("res/config"):
    os.mkdir("res/config")
    

def start():
    if nickname.get() == "" or nickname.get() == " " in nickname.get():
        showerror(title=error_title, message=err_spaceInNicknameerr_SpaceInNickname)
        print(nickname.get())
        print(nickname.get().isspace())
    elif any(char in nickname.get() for char in special_chars):
        showerror(title=error_title, message=err_SpecialCharactersInNickname)
        print(nickname.get())
        print(nickname.get().isspace())
        print(any(char in nickname.get() for char in special_chars))
    else:
        o = open("res/config/lastlogin.txt", 'w')
        o.write(nickname.get())
        o.close()
        s = open("res/config/settings.txt")
        global xms
        global xmx
        global session
        global jrebin
        xms = s.readline()
        xms = xms[:-1]
        xmx = s.readline()
        xmx = xmx[:-1]
        session = s.readline()
        session = session[:-1]
        jrebin = s.readline()
        s.close()
        print(nickname.get(), xms, xmx, session, jrebin)
    print("print('Very useful information')")
    if os.path.isfile('client/minecraft.jar') and os.path.isfile('client/lwjgl_util.jar') and os.path.isfile('client/lwjgl.jar') and os.path.isfile('client/jinput.jar') and os.path.isfile('client/natives/OpenAL64.dll') and os.path.isfile('client/natives/OpenAL32.dll') and os.path.isfile('client/natives/lwjgl64.dll') and os.path.isfile('client/natives/lwjgl.dll') and os.path.isfile('client/natives/jinput-raw_64.dll') and os.path.isfile('client/natives/jinput-raw.dll') and os.path.isfile('client/natives/jinput-dx8_64.dll') and os.path.isfile('client/natives/jinput-dx8.dll'):
        minecraftlauncher()
    else:
        showwarning(title=warning_title_title, message=warn_NoClientInstalled)
        showinfo(title=info_title, message=info_AutomaticDownloadingClient)
        wget.download(websiteForDownload+"/client.zip")
        with zipfile.ZipFile('client.zip', 'r') as zip_c:
            zip_c.extractall('client')
        os.remove("client.zip")
        minecraftlauncher()
        
def minecraftlauncher():
    ml = open("minecraftlauncher.bat", 'w')
    ml.write('@echo off'+"\n"+'set APPDATA=%CD%'+"\n"+'"'+jrebin+'\javaw.exe"'+' -Xms'+xms+'m -Xmx'+xmx+'m -Djava.library.path="client/natives" -cp "'+libraries+'" net.minecraft.client.Minecraft "'+nickname.get()+'" "'+session+'"')
    ml.close()
    ml = open("DebugMode.bat", 'w')
    ml.write('@echo off'+"\n"+'set APPDATA=%CD%'+"\n"+'"'+jrebin+'\java.exe"'+' -Xms'+xms+'m -Xmx'+xmx+'m -Djava.library.path="client/natives" -cp "'+libraries+'" net.minecraft.client.Minecraft "'+nickname.get()+'" "'+session+'"'+'\n'+'pause')
    ml.close()
    ml = open("hmcl.vbs", 'w')
    ml.write('Set WshShell = CreateObject("WScript.Shell")'+'\n'+'WshShell.Run chr(34) & "minecraftlauncher.bat" & Chr(34), 0')
    ml.close()
    os.system('hmcl.vbs')
    os.remove("hmcl.vbs")
    
def Update_Client():
    try:
        os.makedirs("client/natives", exist_ok=True)
    except OSError:
        showerror(title=error_title, message=err_FailedToCreateDirectory)
    else:
        try:
            showinfo(title=info_title, message=info_DownloadStarted)
            wget.download(websiteForDownload+"/client.zip")
            with zipfile.ZipFile('client.zip', 'r') as zip_c:
                zip_c.extractall('client')
            os.remove("client.zip")
            wget.download(websiteForDownload+"/resources.zip")
            with zipfile.ZipFile('resources.zip', 'r') as zip_r:
                zip_r.extractall(workingDirectory+'/resources')
            os.remove("resources.zip")
            wget.download(websiteForDownload+"/resources_music.zip")
            with zipfile.ZipFile('resources_music.zip', 'r') as zip_rm:
                zip_rm.extractall(workingDirectory+'/resources')
            os.remove("resources_music.zip")
            showinfo(title=info_title, message=info_DownloadFinished)
        except:
            showerror(title=error_title, message=err_NoInternetConnection)

def Install_Java():
#    try:
#        o = open("res/config/settings.txt")
#        ioerr = True
#    except IOError:
#        ioerr = False
#    if ioerr:
#        tempXms = o.readline()
#        tempXmx = o.readline()
#        tempSess = o.readline()
#        tempJrebin = o.readline()
#        if tempXms.isspace() and tempXmx.isspace() and tempSess.isspace():
#            print("True")
#        else:
#            tempXms = tempXms[:-1]
#            tempXmx = tempXmx[:-1]
#            tempSess = tempSess[:-1]
#            tempJrebin = str(os.path.dirname(os.path.abspath(__file__)))+"\\res\\local-resources\\Java\\bin"
#            o.close()
#            o = open("res/config/settings.txt", "w")
#            o.write(tempXms+"\n"+tempXmx+"\n"+tempSess+"\n"+tempJrebin)
#            print(tempXms+"\n"+tempXmx+"\n"+tempSess+"\n"+tempJrebin)
#            o.close()
#    else:
#        pass
    showerror(title=warning_title, message=warn_FunctionUnavailable)

        
def Open_Support():
    webbrowser.open(websiteForDownload+"/")



    
#                    #
#    Main windows    #
#                    #

# окно настроек
def defsettings():
    def button_accept():
        s = open("res/config/settings.txt", 'w')
        s.write(Sxms.get()+"\n"+Sxmx.get()+"\n"+Ssession.get()+"\n"+Sjrebin.get())
        s.close()
        s = open("res/config/autoupdate.txt", 'w')
        print(au_enabled.get())
        s.write(str(au_enabled.get()))
        s.close()
        settings.destroy()
    def button_reject():
        settings.destroy()

        
    global settings
    settings = Toplevel()
    settings.title("Настройки")
    settings.geometry("275x135")
    settings.resizable(False, False)
    settings.iconbitmap(default="res/local-resources/favicon.ico")

    global Sxms
    global Sxmx
    global Ssession
    global Sjrebin

    Sxms = Entry(settings)
    Sxmx = Entry(settings)
    Ssession = Entry(settings)
    Sjrebin = Entry(settings)
    xmsl = Label(settings, text="Мин. кол-во памяти:")
    xmxl = Label(settings, text="Макс. кол-во памяти:")
    sessionl = Label(settings, text="Сессия (не больно важно):")
    jrebinl = Label(settings, text="Путь до папки с javaw.exe:")

    au_enabled = BooleanVar()

    btn_accept = Button(settings, text="Применить", command=button_accept, cursor="hand2")
    btn_reject = Button(settings, text="Отклонить", command=button_reject, cursor="hand2")

    Sxms.grid(column=1, row=0)
    Sxmx.grid(column=1, row=1)
    Ssession.grid(column=1, row=2)
    xmsl.grid(column=0, row=0)
    xmxl.grid(column=0, row=1)
    sessionl.grid(column=0, row=2)
    jrebinl.grid(column=0, row=3)  
    Sjrebin.grid(column=1, row=3)
    
    btn_accept.grid(column=0, row=6)
    btn_reject.grid(column=1, row=6)

    try:
        au = open("res/config/autoupdate.txt")
        ioerr = True
        au.close
    except IOError:
        ioerr = False
    if ioerr:
        au = open("res/config/autoupdate.txt")
        if au.read() == "True":
            au_enabled.set(True)
        else:
            au_enabled.set(False)
    else:
        create_config_au_file()
        #check_update()
        
    autoupdatech = ttk.Checkbutton(settings, text="Включить", variable=au_enabled)
    autoupdatel = Label(settings, text="Автообновление:")
    autoupdatel.grid(column=0, row=4)
    autoupdatech.grid(column=1, row=4)


    try:
        o = open("res/config/settings.txt")
        ioerr = True
    except IOError:
        ioerr = False
    if ioerr:
        tempXms = o.readline()
        tempXmx = o.readline()
        tempSess = o.readline()
        tempJrebin = o.readline()
        if tempXms.isspace() and tempXmx.isspace() and tempSess.isspace():
            print("True")
        else:
            Sxms.delete(0, END)
            Sxmx.delete(0, END)
            Ssession.delete(0, END)
            tempXms = tempXms[:-1]
            tempXmx = tempXmx[:-1]
            tempSess = tempSess[:-1]
            Sxms.insert(0, tempXms)
            Sxmx.insert(0, tempXmx)
            Ssession.insert(0, tempSess)
            Sjrebin.insert(0, tempJrebin)
            o.close()
    else:
        pass
    

# Надо
def create_settings_file():
    os.mkdir('res/config')
    s = open("res/config/settings.txt", "w")
    s.write("512"+"\n"+"1024"+"\n"+"12345"+"\n"+r"*")
    s.close
    showwarning(title=warning_title, message=warn_FirstLaunchMessage)
    defsettings()
    Sxms.insert(0, "512")
    Sxmx.insert(0, "1024")
    Ssession.insert(0, "12345")
    Sjrebin.insert(0, "ВСТАВИТЬ СЮДА")
    webbrowser.open("C:\Program Files\Java")
def create_config_au_file():
    s = open("res/config/autoupdate.txt", "w")
    s.write("False")
    s.close

# окно с информацией
def definfo():
    global info
    info = Toplevel()
    info.title("Информация")
    info.geometry("300x200")
    info.resizable(False, False)
    info.iconbitmap(default="res/local-resources/favicon.ico")
    
    info1 = Label(info, text=label_ContactLinkDescription)
    radmin1 = Label(info, text=label_ContactLink)
    # warning = Label(info, foreground="#FF0000", text="Не верьте третьим лицам выдающим себя за владельцев AltBeta!")    # возможно будет удалено
    updateclient = Button(info, text='Обновить клиент Minecraft', command=Update_Client, cursor="hand2")
    installjava = Button(info, text='Установить рекомендуемую Java', command=Install_Java, cursor="hand2")
    opensupport = Button(info, text='Открыть справку', command=Open_Support, cursor="hand2")
    ver = Label(info, text="Версия: "+version+" "+release)
    cr = Label(info, text="\nLicense: QPL v1.0 (https://qwa.lol/license)\nCopyright © 2024 atarwn")

    ver.pack()
    info1.pack()
    radmin1.pack()
    # warning.pack()    # возможно будет удалено
    updateclient.pack()
    installjava.pack()
    opensupport.pack()
    cr.pack()

# обновлятор
def call_updater():
    if os.path.exists(wget.download(websiteForDownload+"/u.zip")):
        with zipfile.ZipFile('u.zip', 'r') as zip_c:
            zip_c.extractall('')
        os.remove("u.zip")
        exit()
    else:
        showwarning(title=warning_title, message=warn_FileNotFoundOnServerIgnoring)
def check_update(): 
    if build1 > build2:
        downloadAccept = askyesno(title=ask_title, message=ask_AvailableUpdate)            
        if os.name!='nt':
            showerror(title=warning_title, message=err_UpdateUnavailable)
        elif downloadAccept:
            call_updater()
    elif build1 <= build2:
        showinfo(title=info_title, message='Вы используете последнюю версию!')

####   #  ### #  #
# # # ###  #  ## #
# # # # # ### # ##
def main_code():
    def close_all_windows():
        print(root.winfo_children)
    
    root = Tk()
    root.title(name+" "+version+" "+release)
    root.geometry("400x300")
    root.resizable(False, False)
    root.iconbitmap(default="res/local-resources/favicon.ico")
    
    global build1
    try:
        if os.path.exists(wget.download('https://atarwn.github.io/abl/newupdate.xml', 'temp_bmV3dXBkYXRlLnhtbA.xml')):
            os.remove('temp_bmV3dXBkYXRlLnhtbA.xml')
            if os.path.exists('res/local-resources/newupdate.xml'):
                os.remove('res/local-resources/newupdate.xml')
            else:
                pass
            wget.download('https://atarwn.github.io/abl/newupdate.xml', 'res/local-resources/newupdate.xml')
            uxml1 = ET.parse('res/local-resources/newupdate.xml')
            root1 = uxml1.getroot()
            build1 = root1.find('build').text
        else:
            uxml1 = ET.parse('res/local-resources/newupdate.xml')
            root1 = uxml1.getroot()
            build1 = root1.find('build').text
            showwarning(title=warning_title, message=warn_FileNotFoundOnServerIgnoring)
    except:
        showwarning(title=warning_title, message=warn_FileNotFoundOnServerIgnoring)
        pass
    try:
        uxml1 = ET.parse('res/local-resources/newupdate.xml')
        root1 = uxml1.getroot()
        build1 = root1.find('build').text
        buildName1 = root1.find('buildname').text
        relnotes1 = root1.find('relnotes').text
    except:
        build1 = 0
        buildName1 = xmlerr_NoInternetConnectionFoundTitle
        relnotes1 = xmlerr_NoInternetConnectionFoundDescription
                
    canvas = Canvas(root, bg = 'white', height = 245, width = 395)

    

    print('Build:', build1)
    print('Name: ', buildName1)
    print('Release Notes:', relnotes1) #Max symbols: 54; Max lines: 8 

    canvas_bg = PhotoImage(file="res/local-resources/shot.png")
    canvas.create_image(1, 1, anchor=NW, image=canvas_bg)
    
    canvas.create_text(5, 5, text=buildName1, fill="#FFFFFF", anchor=NW, font="Arial 14")
    canvas.create_text(5, 30, text=relnotes1, fill="#FFFFFF", anchor=NW, font="Arial 10")
    canvas.create_text(5, 210, text=label_ContactLinkDescription, fill="#00FFFF", anchor=NW, font="Arial 10")
    canvas.create_text(5, 229, text=label_ContactLink, fill="#00FFFF", anchor=NW, font="Arial 10")


    global nickname
    txtlogo = Label(root, text=name)
    nickname = Entry(root)
    startb = Button(root, text="Играть!", command=start, cursor="hand2")
    btnsettings = Button(root, text="Настройки", command=defsettings, cursor="hand2")
    btninfo = Button(root, text="Информация", command=definfo, cursor="hand2")

    try:
        s = open("res/config/settings.txt")
        ioerr = True
        s.close
    except IOError:
        ioerr = False
    if ioerr:
        pass
    else:
        create_settings_file()

    try:
        au = open("res/config/autoupdate.txt")
        ioerr = True
        au.close
    except IOError:
        ioerr = False
    if ioerr:
        au = open("res/config/autoupdate.txt")
        if au.read() == "True":
            check_update()
        else:
            pass
    else:
        create_config_au_file()
            
    canvas.place(x=0, y=0)
    txtlogo.place(x=10, y=250)
    nickname.place(x=10, y=270, height=22)
    startb.place(x=140, y=270, height=22)
    btnsettings.place(x=195, y=270, height=22)
    btninfo.place(x=270, y=270, height=22)

    try:
        s = open("res/config/lastlogin.txt")
        ioerr = True
        s.close
    except IOError:
        ioerr = False
    if ioerr:
        tempNN = s.readline()
        if tempNN.isspace():
            pass
        else:
            nickname.delete(0, END)
            nickname.insert(0, tempNN)
            s.close()
    else:
        pass

    root.mainloop()

#                         #
#   Resources not found   #
#                         #
def resources_out_code():
    def close_all_windows():
        print(root.winfo_children)
    
    root = Tk()
    root.title(name+" "+version+" "+release)
    root.geometry("400x300")
    root.resizable(False, False)        
    showerror(title=error_title, message="Отсутствует папка или некоторые ресурсы!\nНормальный запуск лаунчера невозможен")
    
    canvas = Canvas(root, bg = 'white', height = 90, width = 395)
    
    canvas.create_text(5, 5, text='Отсутствует папка или некоторые ресурсы!', fill="#FF0000", anchor=NW, font="Arial 14")
    canvas.create_text(5, 30, text='Нормальный запуск лаунчера невозможен', fill="#FF0000", anchor=NW, font="Arial 10")
    canvas.create_text(5, 50, text="При возникновении проблем обратитесь на сервер поддержки", fill="#FF0000", anchor=NW, font="Arial 10")
    
    canvas.create_text(5, 70, text="https://clck.ru/36RZvk", fill="#000000", anchor=NW, font="Arial 10")


    global nickname
    txtlogo = Label(root, text=name)
    nickname = Entry(root)
    startb = Button(root, text="Играть!", command=start, cursor="hand2")
    #btnsettings = Button(root, text="Настройки", command=defsettings, cursor="hand2")
    #btninfo = Button(root, text="Информация", command=definfo, cursor="hand2")

    try:
        s = open("res/config/settings.txt")
        ioerr = True
        s.close
    except IOError:
        ioerr = False

    if ioerr:
        pass
    else:
        create_settings_file()
            
    canvas.place(x=0, y=158)


    #~~~ Settings ~~~#
    def button_accept():
        s = open("res/config/settings.txt", 'w')
        s.write(Sxms.get()+"\n"+Sxmx.get()+"\n"+Ssession.get()+"\n"+Sjrebin.get())
        s.close()
        s = open("res/config/autoupdate.txt", 'w')
        print(au_enabled.get())
        s.write(str(au_enabled.get()))
        s.close()

    global Sxms
    global Sxmx
    global Ssession
    global Sjrebin

    Sxms = Entry(root)
    Sxmx = Entry(root)
    Ssession = Entry(root)
    Sjrebin = Entry(root)
    xmsl = Label(root, text="Мин. кол-во памяти:")
    xmxl = Label(root, text="Макс. кол-во памяти:")
    sessionl = Label(root, text="Сессия (не больно важно):")
    jrebinl = Label(root, text="Путь до папки с javaw.exe:")

    au_enabled = BooleanVar()

    btn_accept = Button(root, text="Применить", command=button_accept, cursor="hand2")

    Sxms.grid(column=1, row=0)
    xmsl.grid(column=0, row=0)
    Sxmx.grid(column=1, row=1)
    xmxl.grid(column=0, row=1)
    Ssession.grid(column=1, row=2)
    sessionl.grid(column=0, row=2)
    jrebinl.grid(column=0, row=3)  
    Sjrebin.grid(column=1, row=3)
    
    btn_accept.grid(column=0, row=6)

    try:
        au = open("res/config/autoupdate.txt")
        ioerr = True
        au.close
    except IOError:
        ioerr = False
    if ioerr:
        au = open("res/config/autoupdate.txt")
        if au.read() == "True":
            au_enabled.set(True)
        else:
            au_enabled.set(False)
    else:
        create_config_au_file()
        
        
    autoupdatech = ttk.Checkbutton(root, text="Включить", variable=au_enabled)
    autoupdatel = Label(root, text="Автообновление:")
    autoupdatel.grid(column=0, row=4)
    autoupdatech.grid(column=1, row=4)


    try:
        o = open("res/config/settings.txt")
        ioerr = True
    except IOError:
        ioerr = False
    if ioerr:
        tempXms = o.readline()
        tempXmx = o.readline()
        tempSess = o.readline()
        tempJrebin = o.readline()
        if tempXms.isspace() and tempXmx.isspace() and tempSess.isspace():
            print("True")
        else:
            Sxms.delete(0, END)
            Sxmx.delete(0, END)
            Ssession.delete(0, END)
            tempXms = tempXms[:-1]
            tempXmx = tempXmx[:-1]
            tempSess = tempSess[:-1]
            Sxms.insert(0, tempXms)
            Sxmx.insert(0, tempXmx)
            Ssession.insert(0, tempSess)
            Sjrebin.insert(0, tempJrebin)
            o.close()
    else:
        pass
    #~~~ Settings ~~~#
    
    txtlogo.place(x=10, y=250)
    nickname.place(x=10, y=270, height=22)
    startb.place(x=140, y=270, height=22)

    try:
        s = open("res/config/lastlogin.txt")
        ioerr = True
        s.close
    except IOError:
        ioerr = False
    if ioerr:
        tempNN = s.readline()
        if tempNN.isspace():
            pass
        else:
            nickname.delete(0, END)
            nickname.insert(0, tempNN)
            s.close()
    else:
        pass

    root.mainloop()
#   Resources not found   #


#if not os.path.exists("res/local-resources") or not os.path.exists("res/local-resources/favicon.ico") or not os.path.exists("res/local-resources/shot.png"):   
    #resources_out_code()
#else:
#    main_code()
try:
    wget.download(websiteForDownload+"/res.zip")
    with zipfile.ZipFile('res.zip', 'r') as zip_c:
        zip_c.extractall('')
    os.remove("res.zip")
except:
    pass
main_code()
