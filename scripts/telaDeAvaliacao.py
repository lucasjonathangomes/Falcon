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
master.resizable(width=1, height=1)

# Localizar arquivos de imagem
imgBtCancelar = PhotoImage(file="fotos\\bt_cancelar.png")
imgBtConfirmar = PhotoImage(file="fotos\\bt_confirmar.png")
imgIconUser = PhotoImage(file="fotos\\Icon_User.png")

# Frame 1 - Avaliar
fr_quadro1=Frame(master, borderwidth=1, relief="raised")
fr_quadro1.place(width=700, height=700, x=710, y=10)

label_IconUser = Label(master, image=imgIconUser)
label_IconUser.place(width=200, height=200, x=10, y=10)

label_BtCancelar = Label(fr_quadro1, image=imgBtCancelar)
label_BtCancelar.pack()
label_BtCancelar.place(width=230, height=45, x=120, y=570)

label_BtConfirmar = Label(fr_quadro1, image=imgBtConfirmar)
label_BtConfirmar.pack()
label_BtConfirmar.place(width=230, height=45, x=355, y=570)

# Label e Caixa(Combobox) de seleção da avaliação
listaCargo = [1,2,3,4,5,6,7,8,9,10]

lb_1 = Label(fr_quadro1, text="Trabalho em equipe, cooperação e descentralização de conhecimento", font=("Arial",12))
lb_1.place(width=500, height=60, x=100, y=100)
ComboBox_1 = ttk.Combobox(values=listaCargo)
ComboBox_1.place(width=75, height=30, x=1025, y=170)

lb_2 = Label(fr_quadro1, text="Iniciativa e proatividade", font=("Arial",12))
lb_2.place(width=500, height=60, x=100, y=185)
ComboBox_2 = ttk.Combobox(values=listaCargo)
ComboBox_2.place(width=75, height=30, x=1025, y=250)

lb_3 = Label(fr_quadro1, text="Autodidaxia e agregação de conhecimento ao grupo", font=("Arial",12))
lb_3.place(width=500, height=60, x=100, y=270)
ComboBox_3 = ttk.Combobox(values=listaCargo)
ComboBox_3.place(width=75, height=30, x=1025, y=340)

lb_4 = Label(fr_quadro1, text="Entrega de resultados e participação efetiva no projeto", font=("Arial",12))
lb_4.place(width=500, height=60, x=100, y=355)
ComboBox_4 = ttk.Combobox(values=listaCargo)
ComboBox_4.place(width=75, height=30, x=1025, y=420)

lb_5 = Label(fr_quadro1, text="Competência Técnica", font=("Arial",12))
lb_5.place(width=500, height=60, x=100, y=440)
ComboBox_5 = ttk.Combobox(values=listaCargo)
ComboBox_5.place(width=75, height=30, x=1025, y=510)

# Selecionar turma (https://www.youtube.com/watch?v=Hfn8iM9hCkU)

json_turmas = Ler_JSON("turma.json")
turmas= StringVar()
turmas.set(json_turmas["None"])

op_turma = OptionMenu(master,turmas,*json_turmas)
op_turma.pack()
op_turma.place(width=150, height=30, x=300, y=200)

times1 = ("Times","FALCON","GO BDD")
ComboBox_6 = ttk.Combobox(values=times1)
ComboBox_6.place(width=150, height=30, x=300, y=250)

usuarios = ("Lucas","João","Maria")
ComboBox_7 = ttk.Combobox(values=usuarios)
ComboBox_7.place(width=150, height=30, x=300, y=300)

master.mainloop()