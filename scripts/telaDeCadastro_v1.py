from cgitb import text
from email.policy import default
from tkinter import *
from turtle import left
from tkinter import ttk
from msilib.schema import ComboBox
from support import *

def salvarUser ():
   cargo = ComboBox_cargo.get()
   nome = entryNome.get()
   email = entryEmail.get()
   senha = entrySenha.get()


   dicionario = {
      "joão":{"cargo": cargo,"nome": nome, "email": email,"senha": senha}
      }     
   Salvar_JSON("userTest.json",dicionario)

path = Caminho_ate_Falcon()+"//fotos//"
master = Tk()
master.geometry("1440x1024+350+20")
master.iconbitmap(default=path+"telaCadastro.png")
master.resizable(width=FALSE, height=FALSE)

# imgFundo = PhotoImage("telaCadastro.png")
imgFundo = PhotoImage(file="fotos\\telaCadastro.png")
botao = Retorna_imagem("botao.png")

label_fundo = Label(master, image=imgFundo)
label_fundo.pack()

listaCargo = ["Admin", "Aluno PO", "Líder do Grupo/Instrutor","Fake Client", "Líder Tecnico", "Aluno"]

ComboBox_cargo = ttk.Combobox(values=listaCargo)
ComboBox_cargo.place(width=500, height=60, x=323, y=320)

entryNome = Entry(master, bd=2, font=("Arial", 20), justify=LEFT)
entryNome.place(width=500, height=60, x=323, y=447)

entryEmail = Entry(master, bd=2, font=("Arial", 20), justify=LEFT)
entryEmail.place(width=500, height=60, x=323, y=547)

esconderSenha = StringVar()
entrySenha = Entry(master, textvariable=esconderSenha, show="*", bd=2, font=("Arial", 20), justify=LEFT)
entrySenha.place(width=500, height=60, x=323, y=647)

# Botão

def verificaSenha():
   nome = entryNome.get()
   senha = entrySenha.get()
   selecao = ComboBox_cargo.get()
   print("selecao", selecao)

botaoCadastro = Button(master,command=salvarUser, bd=0, image=botao)
# botaoCadastro.place(width=279, height=69, x=550, y=805)
botaoCadastro.place(width=279, height=69, x=800, y=505)

master.mainloop()