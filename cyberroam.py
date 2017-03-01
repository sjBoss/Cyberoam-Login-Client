import tkinter
from tkinter import *
import webbrowser
from selenium import webdriver
from pyvirtualdisplay import Display
import transpositionEncrypt, transpositionDecrypt
import os
import re
import time
#36.         translated = transpositionEncrypt.encryptMessage(myKey, content)


def execute_auto():
    file = open("detail.txt", "r")
    myKey = 10
    content = file.read()
    file.close()
    translated = transpositionDecrypt.decryptMessage(myKey, content)
    file = open("detail.txt","w")
    file.write(translated)
    file.close()
    file = open("detail.txt", "r")
    str_info = file.read()
    #print(str_info)
    usernamereg = re.compile(r'!u@\S+')
    passwordreg = re.compile(r'//!p@\S+')
    username = usernamereg.search(str_info)
    password = passwordreg.search(str_info)
    usrstr = username.group()[3:]
    idtext.insert(INSERT, usrstr)
    passstr = password.group()[5:]
    passInput.insert(INSERT, passstr)
    file.close()
    display = Display(visible=0, size=(800, 600))
    display.start()
    portal = webdriver.Firefox()
    portal.get("http://172.16.0.30:8090/httpclient.html")
    enter_user_id = portal.find_element_by_name("username")
    enter_pass = portal.find_element_by_name("password")
    enter_user_id.send_keys(usrstr)
    enter_pass.send_keys(passstr)
    portal.implicitly_wait(3)
    enter_pass.submit()
    #time.sleep(1)

    check = portal.find_element_by_tag_name('xmp')

    if check.text == "You have successfully logged in":
        status.config(text = "Logged in")
    elif check.text == "The system could not log you on. Make sure your password is correct":
        status.config(text = "Try Again")
    else:
        status.config(text="Data Limit Exceeded")
    portal.quit()

    file = open("detail.txt", "r")
    content = file.read()
    file.close()
    translated = transpositionEncrypt.encryptMessage(myKey, content)
    file = open("detail.txt","w")
    file.write(translated)
    file.close()


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def execute_save(event):

    file = open("detail.txt","w")
    myKey = 10
    str1 = idtext.get()
    str2 = passInput.get()
    str3 = "!u@" + str1 + "\n" + "//!p@" + str2
    file.write(str3)
    file.close()
    file = open("detail.txt", "r")
    content = file.read()
    file.close()
    translated = transpositionEncrypt.encryptMessage(myKey, content)
    file = open("detail.txt","w")
    file.write(translated)
    file.close()


def execute_login(event):

   usrstr = idtext.get()
   passstr = passInput.get()

   if usrstr!="" and passstr!="" :
      display = Display(visible=0, size=(800, 600))
      display.start()
      portal = webdriver.Firefox()
      portal.get("http://172.16.0.30:8090/httpclient.html")
      enter_user_id = portal.find_element_by_name("username")
      enter_pass = portal.find_element_by_name("password")
      enter_user_id.send_keys(usrstr)
      enter_pass.send_keys(passstr)
      portal.implicitly_wait(3)
      enter_pass.submit()
      #time.sleep(1)

      check = portal.find_element_by_tag_name('xmp')

      if check.text == "You have successfully logged in":
          status.config(text="Logged in")
      elif check.text == "The system could not log you on. Make sure your password is correct":
          status.config(text="Try Again")
      else:
          status.config(text="Data Limit Exceeded")


      portal.quit()
   else:
       print("enter username and password")



root = Tk()
root.geometry("362x170")
root.title("Gateway to your web experience!")
root.configure(background = "yellow")
root.resizable(width = False, height = False)
photo1 = PhotoImage(file="~/final.png")


heading = Label(root,text = "LOGIN",font = "Serif 15",background = "yellow",foreground = "red")
heading.place(relx = 0.5, rely = 0.1,anchor = "center")

status = Label(root,text = "",font = "Serif 10",background = "yellow",foreground = "blue")
status.place(relx = 0.8, rely = 0.1,anchor = "center")

cyber = Label(root, image = photo1,background = "yellow")
cyber.place(relx = 0.13, rely = 0.12, anchor = "center")

userid = Label(root,text = "ID_number",font = "Serif 11",background = "yellow")
userid.place(relx = 0.13,rely = 0.3,anchor = "center")

idtext = Entry(root,width = "28")
idtext.place(relx = 0.6, rely = 0.3,anchor= "center")

password = Label(root,text = "Password",font = "Serif 11", background = "yellow")
password.place(relx = 0.113, rely = 0.56, anchor= "center")

passInput = Entry(root,width = "28",show = "*")
passInput.place(relx = 0.6,rely = 0.56, anchor = "center")

auto = Button(root,text = "AUTO", width = 6, bg = "grey",foreground = "white",command = execute_auto)
auto.place(relx = 0.5, rely = 0.8, anchor = "center")

save = Button(root, text = "SAVE", width = 6, bg = "grey",foreground = "white")
save.place(rely = 0.8, relx = 0.25, anchor = "center")

login = Button(root, text = "LOGIN",width = 6, bg = "grey",foreground = "white")
login.place(rely = 0.8, relx = 0.75,anchor = "center")

save.bind("<Button-1>",execute_save)
login.bind("<Button-1>",execute_login)
center(root)
root.mainloop()
