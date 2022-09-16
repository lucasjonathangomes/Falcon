from cgitb import text
from tkinter import *
from turtle import left
from tkinter import ttk
from msilib.schema import ComboBox
from support import *

# def salvarUser ():
#    cargo = ComboBox_cargo.get()
#    nome = entryNome.get()
#    email = entryEmail.get()
#    senha = entrySenha.get()
   #usuário

#    dicionario = {
#       "joão":{"cargo": cargo,"nome": nome, "email": email,"senha": senha}
#       }     
#    Salvar_JSON("userTest.json",dicionario)

path = Caminho_ate_Scripts()+"//fotos//"
master = Tk()
master.geometry("1440x1024+350+20")
master.iconbitmap(default=path+"avaliacao.png")
master.resizable(width=FALSE, height=FALSE)

imgFundo = PhotoImage("avaliacao.png")
imgFundo = Retorna_imagem('avaliacao.png')
botao = Retorna_imagem("botao.png")

label_fundo = Label(master, image=imgFundo)
label_fundo.pack()

listaCargo = ["Admin", "Aluno PO", "Líder do Grupo/Instrutor","Fake Client", "Líder Tecnico", "Aluno"]

#ComboBox_cargo = ttk.Combobox(values=listaCargo)
#ComboBox_cargo.place(width=500, height=60, x=323, y=320)

entryEmail = Entry(master, bd=2, font=("Calibri", 20), justify=LEFT)
entryEmail.place(width=500, height=60, x=290, y=160)

entryTime = Entry(master, bd=2, font=("Calibri", 20), justify=LEFT)
entryTime.place(width=500, height=60, x=290, y=240)

entrySprint = Entry(master, bd=2, font=("Calibri", 20), justify=LEFT)
entrySprint.place(width=500, height=60, x=290, y=320)

entry1 = Entry(master, bd=2, font=("Calibri", 20), justify=LEFT)
entry1.place(width=100, height=60, x=790, y=440)

entry2 = Entry(master, bd=2, font=("Calibri", 20), justify=LEFT)
entry2.place(width=100, height=60, x=790, y=525)

entry3 = Entry(master, bd=2, font=("Calibri", 20), justify=LEFT)
entry3.place(width=100, height=60, x=790, y=655)

entry4 = Entry(master, bd=2, font=("Calibri", 20), justify=LEFT)
entry4.place(width=100, height=60, x=790, y=790)

entry5 = Entry(master, bd=2, font=("Calibri", 20), justify=LEFT)
entry5.place(width=100, height=60, x=790, y=880)






# Botão

# botaoCadastro = Button(master,command=salvarUser, bd=0, image=botao)
# botaoCadastro.place(width=279, height=69, x=550, y=805)

master.mainloop()