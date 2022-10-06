
from support import *


class Cadastrar:
    def __init__(self, jan):
        self.jan = jan
        self.imgbt_cadastrarsprint = Retorna_imagem("bt_cadastrar_sprint.png") 
        self.imgbt_cadastrarusuario = Retorna_imagem("bt_cadastrar_usuario.png")
        self.imgbt_cadastrartime =Retorna_imagem("bt_cadastrar_times.png")
        self.imgIconUser = Retorna_imagem("Icon_User.png")

        self.button_cadastrarsprint = Button(jan, image=self.imgbt_cadastrarsprint, command=lambda:self.CadastrarSprint())
        self.button_cadastrarsprint.place(x=50, y=180)

        self.label_cadastrarusuario = Button(jan, image=self.imgbt_cadastrarusuario, command=lambda:self.CadastrarUsuario())
        self.label_cadastrarusuario.place(x=50, y=240)

        self.label_cadastrartime = Button(jan, image=self.imgbt_cadastrartime, command=lambda:self.CadastrarTimes())
        self.label_cadastrartime.place(x=50, y=300)

        self.font = ("Arial", 18)
    
     # tirar o bg dps de ajustar a tela!
     # usar o frame para criar as funções  
    

    def CadastrarSprint(self):
        frame = Frame(self.jan, width=800, height= 500, bg='green')
        # frame.pack(side='right')
        frame.place(x=400, y=200)

        # inicio da sprint 1
        Label(frame, text='Sprint 1 - Início').place (x=0,y=0)
        self.inicio_sprint1 = Entry(frame, font=self.font, width=6)
        self.inicio_sprint1.place(x=0, y= 15)

        # fim da sprint 1
        Label(frame, text='Sprint 1 - Fim').place (x=100, y=0)
        self.fim_sprint1 = Entry(frame, font=self.font, width=5)
        # self.fim_sprint1.pack()
        self.fim_sprint1.place(x=100, y=15)
    

        # # inicio da Sprint 2
        # Label(frame, text='Sprint 2 - Início').pack()
        # self.inicio_sprint2 = Entry(frame, font=self.font)
        # self.inicio_sprint2.pack()

        # # Fim da Sprint 2
        # Label(frame, text='Sprint 2 - Fim').pack()
        # self.fim_sprint2 = Entry(frame, font=self.font, )
        # self.fim_sprint2.pack()

        # # inicio da Sprint 3
        # Label(frame, text='Sprint 3 - Início').pack()
        # self.inicio_sprint3 = Entry(frame, font=self.font)
        # self.inicio_sprint3.pack()

        # # Fim da Sprint 3
        # Label(frame, text='Sprint 3 - Fim').pack()
        # self.fim_sprint3 = Entry(frame, font=self.font, )
        # self.fim_sprint3.pack()

        # # Inicio da Sprint 4
        # Label(frame, text='Sprint 4 - Início').pack()
        # self.inicio_sprint4 = Entry(frame, font=self.font)
        # self.inicio_sprint4.pack()

        # # fim da Sprint 4
        # Label(frame, text='Sprint 4 - Fim').pack()
        # self.fim_sprint4 = Entry(frame, font=self.font)
        # self.fim_sprint4.pack()

    def CadastrarUsuario(self):
        frame = Frame(self.jan, width=800, height= 600, bg= 'yellow')
        frame.pack(side='right')
        # frame.place(x=500, y=200)

        self.listaCargo = ["Aluno PO", "Fake Client", "Líder Tecnico", "Aluno"]

        self.ComboBox_cargo = ttk.Combobox(frame, values=self.listaCargo)
        self.ComboBox_cargo.place(width=500, height=60, x=323, y=320)

        Label (frame, text='Nome').pack()
        self.entryNome = Entry(frame, font=self.font)
        self.entryNome.pack() 

        Label (frame, text='Email').pack()
        self.entryEmail = Entry(frame, font=self.font)
        self.entryEmail.pack()

        Label (frame, text='Senha').pack()
        self.entrySenha = Entry(frame, show="*", bd=2, font=("Arial", 20))
        self.entrySenha.place(width=500, height=60, x=323, y=647)

        self.cadastrar_fim = Button(frame, bd=0, image=self.cadastrar_fim, command=self.Salvar_user)
        # self.botaoCadastro.place(width=279, height=69, x=550, y=805)
        self.cadastrar_fim.place(width=279, height=69, x=800, y=505)

        self.lista_itens = [self.ComboBox_cargo, self.entryNome, self.entryEmail, self.entrySenha, self.botaoCadastro]




    def CadastrarTimes(self):
        x=323
        y=647
        frame = Frame(self.jan, width=800, height= 600, bg= 'red')
        frame.pack(side='right')
        self.entryTime = Entry(frame, bd=2, font=("Arial", 28))
        Label (frame, text='Times', font=("Arial",40)).place(x = x, y = y)
        self.entryTimes = Entry(frame, bd=2, font=("Arial",20))
        self.entryTimes.place(width=500, height=80, x=x, y=y+20)
        
        # self.entryTime.place( x=400, y=500)    
        self.entryTime.pack()
        # frame.place(x=500, y=200)


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

Cadastrar(jan)

jan.mainloop()

