
from tkinter import font
from support import *


class Cadastrar:
    def __init__(self, jan):
        self.jan = jan
        self.imgbt_cadastrarsprint = Retorna_imagem("bt_cadastrar_sprint.png") 
        self.imgbt_cadastrarusuario = Retorna_imagem("bt_cadastrar_usuario.png")
        self.imgbt_cadastrartime =Retorna_imagem("bt_cadastrar_times.png")
        self.imgIconUser = Retorna_imagem("Icon_User.png")
        self.imgcadastrar_fim = Retorna_imagem("cadastrar_fim.png")
        self.imgcancelar_fim = Retorna_imagem("cancelar_fim.png")

        self.button_cadastrarsprint = Button(jan, image=self.imgbt_cadastrarsprint, command=lambda:self.Iniciar_perguntas('sprint'))
        self.button_cadastrarsprint.place(x=50, y=180)

        self.label_cadastrarusuario = Button(jan, image=self.imgbt_cadastrarusuario, command=lambda:self.Iniciar_perguntas('usuario'))
        self.label_cadastrarusuario.place(x=50, y=240)

        self.label_cadastrartime = Button(jan, image=self.imgbt_cadastrartime, command=lambda:self.Iniciar_perguntas('time'))
        self.label_cadastrartime.place(x=50, y=300)


        self.font = ("Arial", 18)

    def CadastrarSprint(self):

        # inicio da sprint 1
        Label(self.frame, text='Sprint 1 - Início', font=self.font).place(x=0,y=0)
        self.inicio_sprint1 = Entry(self.frame, font=self.font, width=10)
        self.inicio_sprint1.place(x=20, y= 50)

        # fim da sprint 1
        Label(self.frame, text='Sprint 1 - Fim', font=self.font).place (x=250, y=0)
        self.fim_sprint1 = Entry(self.frame, font=self.font, width=10)
        # self.fim_sprint1.pack()
        self.fim_sprint1.place(x=280, y=50)
    
        # -----------------------------------------------------------
        
        # inicio da sprint 2
        Label(self.frame, text='Sprint 2 - Início', font=self.font).place(x=0,y=100)
        self.inicio_sprint1 = Entry(self.frame, font=self.font, width=10)
        self.inicio_sprint1.place(x=20, y= 150)

        # fim da sprint 2
        Label(self.frame, text='Sprint 2 - Fim', font=self.font).place (x=250, y=100)
        self.fim_sprint1 = Entry(self.frame, font=self.font, width=10)
        # self.fim_sprint2.pack()
        self.fim_sprint1.place(x=280, y=150)

        # -----------------------------------------------------------
    
        # inicio da sprint 3
        Label(self.frame, text='Sprint 3 - Início', font=self.font).place(x=0,y=200)
        self.inicio_sprint1 = Entry(self.frame, font=self.font, width=10)
        self.inicio_sprint1.place(x=20, y= 250)

        # fim da sprint 3
        Label(self.frame, text='Sprint 3 - Fim', font=self.font).place (x=250, y=200)
        self.fim_sprint1 = Entry(self.frame, font=self.font, width=10)
        # self.fim_sprint3.pack()
        self.fim_sprint1.place(x=280, y=250)
         # -----------------------------------------------------------
    
        # inicio da sprint 4
        Label(self.frame, text='Sprint 4 - Início', font=self.font).place(x=0,y=300)
        self.inicio_sprint1 = Entry(self.frame, font=self.font, width=10)
        self.inicio_sprint1.place(x=20, y= 350)

        # fim da sprint 4
        Label(self.frame, text='Sprint 4 - Fim', font=self.font).place (x=250, y=300)
        self.fim_sprint1 = Entry(self.frame, font=self.font, width=10)
        # self.fim_sprint4.pack()
        self.fim_sprint1.place(x=280, y=350)

    def Iniciar_perguntas(self, cadastrar):
        try:
            self.frame.destroy()
        except:
            pass 
        
        self.label_cadastrarfim = Button(jan, image=self.imgbt_cadastrar_fim, command=lambda:self.Iniciar_perguntas('cadastro fim'))
        self.label_cadastrarfim.place(x=280, y=500)

        self.label_cancelarfim = Button(jan, image=self.imgbt_cancelar_fim, command=lambda:self.Salvar)
        self.label_cancelarfim.place(x=0, y=500)

        self.frame = Frame(self.jan, width=800, height= 500)
        self.frame.place(x=800, y=180)

        if cadastrar == 'sprint':
            self.CadastrarSprint()

        elif cadastrar == 'time':
            self.CadastrarTimes() 

        elif cadastrar == 'usuario':
            self.CadastrarUsuario() 

    def CadastrarUsuario(self):
        self.listaCargo = ["Aluno PO", "Fake Client", "Líder Tecnico", "Aluno"]

        Label (self.frame, text='Cargo', font=self.font).pack()
        self.ComboBox_cargo = ttk.Combobox(self.frame, values=self.listaCargo, font=self.font)#, font=('Arial', 10))
        self.ComboBox_cargo.pack()

        Label(self.frame).pack()

        self.per, self.re = Criar_Perguntas(self.frame, perguntas=['Nome', 'Email', 'Senha'], font=self.font)

    def CadastrarTimes(self):
        self.entryTime = Entry(self.frame, bd=2, font=("Arial", 28))
        Label (self.frame, text='Times', font=("Arial",40)).place(x = x, y = y)
        self.entryTimes = Entry(self.frame, bd=2, font=("Arial",20))
        self.entryTimes.place(width=500, height=80, x=x, y=y+20)
        
        # self.entryTime.place( x=400, y=500)    
        self.entryTime.pack()

    def CadastrarTurma(self):
        self.entryTurma = Entry(self.jan, bd=4, font=("Arial", 20), justify=LEFT)
        self.entryTurma.place(width=500, height=60, x=400, y=580)   

    def Salvar_sprint (self):
         self.inicio_sprint1 = self.inicio_sprint1.get().strip()
         self.fim_sprint1 = self.inicio_sprint1.get().strip()
         self.inicio_sprint2 = self.inicio_sprint2.get().strip()
         self.fim_sprint2 = self.inicio_sprint2.get().strip()
         self.inicio_sprint3 = self.inicio_sprint.get().strip()
         self.fim_sprint3 = self.inicio_sprint.get().strip()
         self.inicio_sprint4 = self.inicio_sprint.get().strip()
         self.fim_sprint4 = self.inicio_sprint.get().strip()
    
    def Salvar_user (self):
        self.ComboBox_cargo = self.ComboBox_cargo.get().strip()
        self.entryNome = self.entryNome  
        self.entryEmail = self.entryEmail 
        self.entrySenha = self.entrySenha 


jan = Tk()
jan.geometry("%dx%d" % (jan.winfo_screenwidth(), jan.winfo_screenheight()))
Cadastrar(jan)

jan.mainloop()

