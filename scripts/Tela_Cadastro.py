
from support import *


class Cadastrar:
    def __init__(self, jan):
        self.jan = jan
        self.bt_confirmar_ja_existe = False

        self.imgbt_cadastrarsprint = Retorna_imagem("bt_cadastrar_sprint.png") 
        self.imgbt_cadastrarusuario = Retorna_imagem("bt_cadastrar_usuario.png")
        self.imgbt_cadastrartime =Retorna_imagem("bt_cadastrar_times.png")
        self.imgIconUser = Retorna_imagem("Icon_User.png")

        self.frame_botoes = Frame(self.jan, width=400, height=450)#, bg='green')
        self.frame_botoes.place(x=50, y=180)

        # self.frame = Frame(self.jan, width=800, height= 500, bg='blue')
        # self.frame.place(x=800, y=180)

        self.button_cadastrarsprint = Button(self.frame_botoes, image=self.imgbt_cadastrarsprint, command=lambda:self.Iniciar_perguntas('sprint'))
        # self.button_cadastrarsprint.place(x=50, y=180)
        self.button_cadastrarsprint.pack()
        Label(self.frame_botoes).pack()

        self.label_cadastrarusuario = Button(self.frame_botoes, image=self.imgbt_cadastrarusuario, command=lambda:self.Iniciar_perguntas('usuario'))
        # self.label_cadastrarusuario.place(x=50, y=240)
        self.label_cadastrarusuario.pack()
        Label(self.frame_botoes).pack()

        self.label_cadastrartime = Button(self.frame_botoes, image=self.imgbt_cadastrartime, command=lambda:self.Iniciar_perguntas('time'))
        # self.label_cadastrartime.place(x=50, y=300)
        self.label_cadastrartime.pack()
        Label(self.frame_botoes).pack()

        self.font = ("Arial", 18)


    def CadastrarSprint(self):
        def Deletar_calendario(frame, botao, data):
            botao['text'] = data
            Destruir_itens([frame])

        def Mostrar_Calendario(botao):
            frame_calendario = Frame(self.jan, width=340, height=450)
            frame_calendario.place(x=685, y=400)

            data = Calendar(frame_calendario)
            data.pack()
            Label(frame_calendario).pack()
            Button(frame_calendario, text='Selecionar data', 
                    command=lambda:Deletar_calendario(frame_calendario, botao, data.get_date())).pack()


        def Salvar_sprint_no_dict(inicio, fim):
            sprint = self.label_sprint['text'].strip(':')
            sprint_split = sprint.split()
            self.sprints_dict[sprint] = {'Inicio': inicio, 'Fim': fim}
            sprint = f'{sprint_split[0]} {int(sprint_split[1]) + 1}:'
            self.label_sprint['text'] = sprint

        def Add_sprint():
            inicio = self.sprt_inicio_bt['text']
            fim    = self.sprt_fim_bt['text']
            sprint = self.label_sprint['text'].strip(':')

            if not (inicio == 'Selecionar' or  fim == 'Selecionar'):
                self.list_box_sprints.insert(END, f'{sprint} --> Inicio: {inicio} - Fim: {fim}')
                # Label(self.main_frame, text=table, font=font).pack()
                # self.list_tables_name.append(table)
                Salvar_sprint_no_dict(inicio, fim)
                self.sprt_inicio_bt['text'] = 'Selecionar'
                self.sprt_fim_bt['text']    = 'Selecionar'
                print(self.sprints_dict)
            
            else:
                messagebox.showerror('Data invalida', 'Selecione uma data para inicio e fim da sprint')

        font = ('Arial', 15)
        font_bt = ('Arial', 12)

        self.sprints_dict = {}

        self.frame.place(x=455, y=180)

        self.label_sprint = Label(self.frame, text='Sprint 1:', font=font)
        self.label_sprint.place(x=50, y=0)

        Label(self.frame, text='Inicio:', font=font).place(x=150, y=0)
        self.sprt_inicio_bt = Button(self.frame, text='Selecionar', font=font_bt, command=lambda:Mostrar_Calendario(self.sprt_inicio_bt)) 
                    # command=lambda:Deletar_calendario(frame_calendario, botao, data.get_date())).pack()
        self.sprt_inicio_bt.place(x=212, y=0)

        Label(self.frame, text='Fim:', font=font).place(x=350, y=0)
        self.sprt_fim_bt = Button(self.frame, text='Selecionar', font=font_bt, command=lambda:Mostrar_Calendario(self.sprt_fim_bt)) 
                    # command=lambda:Deletar_calendario(frame_calendario, botao, data.get_date())).pack()
        self.sprt_fim_bt.place(x=400, y=0)

        add_sprint = Button(self.frame, text='Add', font=font_bt, command=Add_sprint)
        add_sprint.place(x=550, y=0)

        self.frame_sprint = Frame(self.frame, width=400, height=200)#, bg='green')
        self.frame_sprint.place(x=50, y=50)

        scrollbar = Scrollbar(self.frame_sprint)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.list_box_sprints = Listbox(self.frame_sprint, yscrollcommand=scrollbar.set, width=100)
        self.list_box_sprints.pack(side=LEFT, fill=BOTH)

        scrollbar.config(command=self.list_box_sprints.yview)


    def CadastrarSprint_2(self):
        def Deletar_calendario(frame, botao, data):
            botao['text'] = data
            Destruir_itens([frame])

        def Mostrar_Calendario(botao):
            frame_calendario = Frame(self.jan, width=340, height=450)
            frame_calendario.place(x=455, y=180)

            data = Calendar(frame_calendario)
            data.pack()
            Label(frame_calendario).pack()
            Button(frame_calendario, text='Selecionar data', 
                    command=lambda:Deletar_calendario(frame_calendario, botao, data.get_date())).pack()

        # inicio da sprint 1
        Label(self.frame, text='Sprint 1 - Início', font=self.font).place(x=0,y=0)
        self.inicio_sprint1 = Entry(self.frame, font=self.font, width=10)
        self.inicio_sprint1.place(x=20, y= 50)

        # fim da sprint 1
        Label(self.frame, text='Sprint 1 - Fim', font=self.font).place (x=250, y=0)
        # self.fim_sprint1 = Entry(self.frame, font=self.font, width=10)
        self.sprt_1_inicio = Button(self.frame, text='Click', font=self.font, command=lambda:Mostrar_Calendario(self.sprt_1_inicio))
        # self.fim_sprint1.pack()   
        self.sprt_1_inicio.place(x=280, y=50)
    
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

    def Iniciar_perguntas(self, cadastrar_oq):
        try:
            self.frame.destroy()
            self.cadastrar.destroy()
            self.cancelar.destroy()
            self.label_vazio.destroy()
            if cadastrar_oq != 'None':
                self.bt_confirmar_ja_existe = False
        except:
            pass 

        self.frame = Frame(self.jan, width=800, height= 500)
        self.frame.place(x=800, y=180)
        
        if not self.bt_confirmar_ja_existe:
            self.img_cadastrar = Retorna_imagem("cadastrar_fim.png")
            self.img_cancelar = Retorna_imagem("cancelar_fim.png")
            self.cadastrar = Button(self.frame_botoes, image=self.img_cadastrar, command=lambda:self.Salvar(cadastrar_oq), 
                                    width=150, height=20)
            # self.cadastrar.place(x=250, y=400)
            self.cadastrar.pack(side='bottom')
            
            self.label_vazio = Label(self.frame_botoes)
            self.label_vazio.pack(side='bottom')

            self.cancelar = Button(self.frame_botoes, image=self.img_cancelar, command=lambda:self.Iniciar_perguntas('None'), 
                                    width=150, height=20)
            # self.cancelar.place(x=10, y=400)
            self.cancelar.pack(side='bottom')

            self.bt_confirmar_ja_existe = True

        if cadastrar_oq == 'sprint':
            self.CadastrarSprint()

        elif cadastrar_oq == 'time':
            self.CadastrarTimes() 

        elif cadastrar_oq == 'usuario':
            self.CadastrarUsuario() 

    def CadastrarUsuario(self):
        self.listaCargo = ["Aluno PO", "Fake Client", "Líder Tecnico", "Aluno"]

        Label (self.frame, text='Cargo', font=self.font).pack()
        self.ComboBox_cargo = ttk.Combobox(self.frame, values=self.listaCargo, font=self.font)#, font=('Arial', 10))
        self.ComboBox_cargo.pack()

        Label(self.frame).pack()

        self.per_user, self.re_user = Criar_Perguntas(self.frame, perguntas=['Nome', 'Email', 'Senha'], font=self.font)

    def CadastrarTimes(self):
        self.turmas = Ler_JSON('turma.json')
        lista_turmas = list(self.turmas)

        Label (self.frame, text='Turma', font=self.font).pack()
        self.ComboBox_turma = ttk.Combobox(self.frame, values=lista_turmas, font=('Arial', 15))
        self.ComboBox_turma.pack()

        Label(self.frame).pack()

        Label (self.frame, text='Qual vai ser o nome do time?', font=self.font).pack()
        self.entryTime = Entry(self.frame, font=("Arial",15), width=15)
        self.entryTime.pack()
        
    def CadastrarTurma(self):
        self.entryTurma = Entry(self.jan, bd=4, font=("Arial", 20), justify=LEFT)
        self.entryTurma.place(width=500, height=60, x=400, y=580)   

    def Salvar_sprint (self):
        pass 

    def Salvar_user (self):
        def Validar_info(nome, email, cargo, senha, users):
            status = False 
            user = email.split('@')[0].lower().strip()

            # Verificar Cargo 
            if cargo.strip() == '' or cargo.strip() not in self.listaCargo:
                messagebox.showerror('Cargo', 'O cargo não existe e/ou não foi selecionando')
            # Verificar Nome
            elif nome.strip() == '':
                messagebox.showerror('None', 'O nome é obrigatório')
            
            # Verificar Email
            elif '@' not in email:
                messagebox.showerror('Email invalido', 'O Email está no formato errado. \nExemplo: exemplo@gmail.com')

            # Verificar User
            elif user in users:
                messagebox.showerror('Nome do Email ja cadastrado', f'O nome "{user}" ja esta cadastrado, se esqueceu a senha aperte em "esqueci a senha" na hora de fazer o login. \nOBS: A extenção do email não diferencia o nome de usuario.')

            # Verificar Senha
            elif len(senha) < 5:
                messagebox.showerror('Senha', 'A senha deve ter no minimo 5 digitos')
    
            # Passou em todos os anteriores
            else:
                status = True 
            
            return status, user

        dict_info_entry = {}
        cont = 0
        for info in self.per_user:
            dict_info_entry[info['text'].lower().strip()] = self.re_user[cont]           
            cont += 1

        cargo = self.ComboBox_cargo.get()

        users = Ler_JSON('users.json')
        
        nome = dict_info_entry['nome'].get()
        email = dict_info_entry['email'].get()
        senha = dict_info_entry['senha'].get()

        info_user_valido, user_name = Validar_info(nome, email, cargo, senha, users)

        if info_user_valido:
            users[user_name] = {   
                                            "nome": nome,
                                            "cargo": cargo,
                                            "email": email,
                                            "acesso": 'Aluno',
                                            "senha": senha
                                        }
            print('salvo')
            Salvar_JSON('users.json', users)
            self.Iniciar_perguntas('usuario')

    def Salvar_time(self):
        turma = self.ComboBox_turma.get()
        time = self.entryTime.get()

        if turma in self.turmas:
            lista_times = [time.upper() for time in self.turmas[turma]]
            if time.upper() in lista_times:
                messagebox.showerror('Time ja existe', f'O time {time} já existe, escolha outro nome')

            else:
                self.turmas[turma][time] = {}
                Salvar_JSON('turma.json', self.turmas)
                # self.Limpar_itens([self.entryTime, self.ComboBox_turma])
                self.Iniciar_perguntas('time')

    def Salvar(self, salvar_oq):
        if salvar_oq == 'sprint':
            self.Salvar_sprint()

        elif salvar_oq == 'time':
            self.Salvar_time()

        elif salvar_oq == 'usuario':
            self.Salvar_user() 

    def Limpar_itens(self, itens:list):
        for item in itens:
            try:
                item.delete(0, END)
            except:
                pass 


jan = Tk()
jan.geometry("%dx%d" % (jan.winfo_screenwidth(), jan.winfo_screenheight()))
Cadastrar(jan)

jan.mainloop()

