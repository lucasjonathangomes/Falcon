
from support import * 

class Avaliar:
    def __init__(self, jan, user=None):
        self.jan = jan 
        self.user = user 
        self.itens_nulos = ['', None]

        # Frame 1 - Aluno
        self.frame_aluno = Frame(jan)
        self.frame_aluno.place(width=300, height=300, x=50, y=150)

        # Frame 2 - Avaliar
        self.frame_avaliar = Frame(jan)
        self.frame_avaliar.place(width=650, height=600, x=640, y=150)

        # Ler o JSON
        self.info_json = Ler_JSON('turma.json')

        # Listas das Turmas, Times e Alunos
        self.lista_turmas = list(self.info_json)
        self.lista_times  = []
        self.lista_alunos = []
        
        self.perguntas = [
            'Trabelho em equipe, cooperação e descentralização de conhecimento:',
            'Iniciativa e proatividade:',
            'Autodidaxia e agregação de conhecimento ao grupo:',
            'Entrega de resultados e participação efetiva no projeto:',
            'Competência técnica:'
        ]

        self.Criar_elementos()
    
    def Criar_elementos(self):
        # Localizar arquivos de imagem
        self.img_cancelar  = Retorna_imagem('bt_cancelar.png')
        self.img_confirmar = Retorna_imagem('bt_confirmar.png')
        self.img_icon_user = Retorna_imagem('Icon_User.png')

        self.label_IconUser = Label(self.jan, image=self.img_icon_user)
        self.label_IconUser.place(x=10, y=10)

        # Aluno
        Label(self.frame_aluno, text='turma').pack()
        self.cbox_turma = ttk.Combobox(self.frame_aluno, values=self.lista_turmas)
        self.cbox_turma.pack()
        self.cbox_turma.bind("<<ComboboxSelected>>", lambda _: self.Atualizar_Combobox(self.cbox_turma, 'time'))

        Label(self.frame_aluno, text='time').pack()
        self.cbox_time = ttk.Combobox(self.frame_aluno, values=self.lista_times)
        self.cbox_time.pack()
        self.cbox_time.bind("<<ComboboxSelected>>", lambda _: self.Atualizar_Combobox(self.cbox_time, 'aluno'))

        Label(self.frame_aluno, text='aluno').pack()
        self.cbox_aluno = ttk.Combobox(self.frame_aluno, values=self.lista_alunos)
        self.cbox_aluno.pack()

        # Botões 
        self.bt_cancelar = Button(self.frame_avaliar, text='Voltar', command=lambda:self.Voltar())
        self.bt_cancelar.place(x=80, y=450)

        self.bt_cancelar = Button(self.frame_avaliar, text='Limpar', command=lambda:self.Limpar_Avaliacao())
        self.bt_cancelar.place(x=150, y=450)

        self.bt_confirmar = Button(self.frame_avaliar, image=self.img_confirmar, command=lambda:self.Enviar())
        self.bt_confirmar.place(x=350, y=450)

        # Perguntas 
        perguntas, self.respostas = Criar_Perguntas(self.frame_avaliar, self.perguntas, width=5, answer_style='combobox', values=[1,2,3,4,5], font=('Arial', 15))

    def Enviar(self):
        tudo_respondido = self.Verificar_respostas()

        if tudo_respondido:
            self.Salvar_no_JSON()
            self.Limpar_Avaliacao()
        
    def Limpar_Avaliacao(self):
        for r in self.respostas:
            r.delete(0, END)
        
        self.lista_times  = list(self.info_json[self.cbox_turma.get()])
        self.lista_alunos = ['']

        self.cbox_time['values'] = self.lista_times
        self.cbox_aluno['values'] = self.lista_alunos
        self.cbox_aluno.delete(0, END)
        self.cbox_time.delete(0, END)

    def Verificar_respostas(self):
        if self.cbox_aluno.get().strip() in self.itens_nulos:
            messagebox.showerror('Não foi selecionado um aluno', 
                                    'Antes de finalizar a avaliação, por favor escolha um aluno')
            return False 
            
        for r in self.respostas:
            r = r.get().strip()

            if r in self.itens_nulos or not r.isnumeric():
                messagebox.showerror('Letra na nota', 
                                    'Em alguma resposta você digitou uma letra ou esta em branco, só aceitamos numero. Em caso de duvida, seleciona uma opção do "select"')

                return False
        
        return True 
        
    def Atualizar_Combobox(self, combox, oq_atualizar):
        def Get_key():
            acesso = self.user['Perfil'].lower()

            if acesso == 'aluno':
                key = 'Desenvolvedores' 
            
            else: # FK
                key = 'PO'
            
            return key 
            
        combox = combox.get().strip().lower()
        try:
            if oq_atualizar == 'time':
                combox_turma = self.cbox_turma.get()
                nova_lista = list(self.info_json[combox_turma])
                self.cbox_time['values'] = nova_lista 
                
                nova_lista_2 = ['']
                self.cbox_aluno['values'] = nova_lista_2 
                self.cbox_aluno.delete(0, END)
                self.cbox_time.delete(0, END)

            elif oq_atualizar == 'aluno':
                key = Get_key() # Pegar quem vai avaliar com base no cargo da pessoa
                # key = 'Desenvolvedores'
                combox_turma = self.cbox_turma.get()
                combox_time = self.cbox_time.get()
                nova_lista = self.info_json[combox_turma][combox_time][key]
                self.cbox_aluno['values'] = nova_lista 
                self.cbox_aluno.delete(0, END)
        except:
            messagebox.showerror(f'{oq_atualizar} invalida', f'{oq_atualizar.title()} "{combox}" não existe. Selecione uma opção da lista')
        
    def Salvar_no_JSON(self):
        def get_key():
            try:
                key = int(max(list(historico[nome_usuario][aluno]))) + 1
            except:
                key = 1
            
            return str(key) 

        historico = Ler_JSON('histrc.json')
        
        nome_usuario = self.user['User']
        aluno = self.cbox_aluno.get().strip()

        if not nome_usuario in historico:
            historico[nome_usuario] = {}
        
        if not aluno in historico[nome_usuario]:
            historico[nome_usuario][aluno] = {}
        
        key = get_key()
        dict_perguntas = self.QnA_como_dict(self.perguntas, self.respostas)
        historico[nome_usuario][aluno][key] = dict_perguntas

        Salvar_JSON('histrc.json', historico)

    def QnA_como_dict(dict, perguntas, respostas):
        cont = 0
        dict_QnA = {}
        for pergunta in perguntas:
            try:                
                dict_QnA[pergunta] = respostas[cont].get()
            except:
                break 

            cont += 1

        return dict_QnA

    def Voltar(self):
        self.frame_aluno.destroy()
        self.frame_avaliar.destroy()
        # Chamar o arquivo de "Menu"
     
# jan = Tk()
# Avaliar(jan, {'User': 'lukas', 'Perfil': 'Aluno'})
# jan.mainloop()
