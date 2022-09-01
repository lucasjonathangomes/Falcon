
from tkinter import Tk
from tkinter import *
from random import randrange

def Apertei_no_login():
    x = randrange(10, 700)
    y = randrange(10, 700)
    Label(text='Apertei no botão de Login', font=('Arial', 20), fg='blue').place(x=x, y=y)


jan = Tk()

Label(text='Login', fg='red', font=('Arial', 100)).place(x=500, y=300)

user = Label(text='Usuario', font=('Arial', 20), fg='blue').place(x=500, y=500)
user_entry = Entry(width=25).place(x=610, y=515)

pasw = Label(text='Senha', font=('Arial', 20), fg='blue').place(x=500, y=600)
pasw_entry = Entry(width=25).place(x=610, y=615)

login_button = Button(text='Login', font=('Arial', 15), fg='blue', command=Apertei_no_login).place(x=700, y=700)


jan.mainloop()

