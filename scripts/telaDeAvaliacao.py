from cgitb import text
from email.policy import default
from tkinter import *
from turtle import left
from tkinter import ttk
from msilib.schema import ComboBox
from support import *


path = Caminho_ate_Falcon()+"//fotos//"
master = Tk()
master.geometry("1440x1024+350+20")
master.iconbitmap(default=path+"telaCadastro.png")
master.resizable(width=FALSE, height=FALSE)

# Localizar arquivos de imagem
imgFundo = PhotoImage(file="fotos\\tela_de_avaliacao.png")
imgBtCancelar = PhotoImage(file="fotos\\bt_cancelar.png")
imgBtConfirmar = PhotoImage(file="fotos\\bt_confirmar.png")

# Abrir imagem
label_fundo = Label(master, image=imgFundo)
label_fundo.pack()

label_BtCancelar = Label(master, image=imgBtCancelar)
label_BtCancelar.pack()
label_BtCancelar.place(width=230, height=45, x=750, y=570)

label_BtConfirmar = Label(master, image=imgBtConfirmar)
label_BtConfirmar.pack()
label_BtConfirmar.place(width=230, height=45, x=980, y=570)

# Caixa de seleção da avaliação
listaCargo = [1,2,3,4,5,6,7,8,9,10]

ComboBox_1 = ttk.Combobox(values=listaCargo)
ComboBox_1.place(width=75, height=30, x=970, y=170)

ComboBox_2 = ttk.Combobox(values=listaCargo)
ComboBox_2.place(width=75, height=30, x=970, y=250)

ComboBox_3 = ttk.Combobox(values=listaCargo)
ComboBox_3.place(width=75, height=30, x=970, y=340)

ComboBox_4 = ttk.Combobox(values=listaCargo)
ComboBox_4.place(width=75, height=30, x=970, y=420)

ComboBox_5 = ttk.Combobox(values=listaCargo)
ComboBox_5.place(width=75, height=30, x=970, y=510)

master.mainloop()