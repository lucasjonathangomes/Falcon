# from cgitb import text
# from email.policy import default
# from tkinter import *
# from turtle import left
# # from tkinter import ttk
# from msilib.schema import ComboBox
from support import *

path = Caminho_ate_Falcon()+"//fotos//"
master = Tk()
master.geometry("1440x1024+350+20")
master.resizable(width=1, height=1)

# Localizar arquivos de imagem
# imgbt_cadastrarsprint= PhotoImage(file="fotos\\bt_cadastrarsprint.png")
# imgbt_cadastrarusuario = PhotoImage(file="fotos\\bt_cadastrarusuario.png")
# imgbt_cadastrartime = PhotoImage(file="fotos\\bt_cadastrartime.png")
# imgIconUser = PhotoImage(file="fotos\\Icon_User.png")

imgbt_cadastrarsprint = Retorna_imagem("bt_cadastrar_sprint.png") 
imgbt_cadastrarusuario = Retorna_imagem("bt_cadastrar_usuario.png")
imgbt_cadastrartime =Retorna_imagem("bt_cadastrar_times.png")
imgIconUser = Retorna_imagem("Icon_User.png")

# Frame 1 - Icone dimen
label_IconUser = Label(master, image=imgIconUser)
label_IconUser.place(width=200, height=200, x=10, y=10)

label_cadastrarsprint = Label(master, image=imgbt_cadastrarsprint)
label_cadastrarsprint.place(width=400, height=80, x=50, y=180)

label_cadastrarusuario = Label(master, image=imgbt_cadastrarusuario)
label_cadastrarusuario.place(width=400, height=80, x=50, y=240)

label_cadastrartime = Label(master, image=imgbt_cadastrartime)
label_cadastrartime.place(width=400, height=80, x=50, y=300)



master.mainloop()
