
# --------------------------------
# Tela de avaliação do Fake Client
# --------------------------------

from tkinter import ttk
from support import * 

class AvaliacaoFK:
    def __init__(self, jan, user):
        '''Criando os elementos (Botões, Labels,...)'''
        self.jan = jan
        self.json_info = Ler_JSON('turma.json')
        self.user = user
        self.perguntas = [
            'Trabelho em equipe, cooperação e descentralização de conhecimento:',
            'Iniciativa e proatividade:',
            'Autodidaxia e agregação de conhecimento ao grupo:',
            'Entrega de resultados e participação efetiva no projeto:',
            'Competência técnica:'
        ]

        self.label_title = Label(jan, text='Avaliação Fake Client', font=('Helvetica', 30), fg='blue')
        self.label_title.pack()

        self.info_turma = [*self.json_info]
        self.info_time = ['None']
        self.info_sprt = ['None']

        self.font = ('Arial', 15)

        self.frame_direito = Frame(self.jan, width=700, height=500)
        self.frame_direito.place(x=500,y=80)

        self.Criar_labels()
        self.lista_perguntas_label, self.lista_perguntas_entry = Criar_Perguntas(self.frame_direito, self.perguntas, font=('Arial', 15))
        
        self.espaco = Label(self.frame_direito)
        self.espaco.pack()
        self.enviar = Button(self.frame_direito, text='Enviar Avaliação', command=lambda:self.Salvar_avaliacao())
        self.enviar.pack()

        # Apagando todos os itens
        self.all_itens = self.lista_label_info + self.lista_perguntas_label + self.lista_perguntas_entry + [self.label_title, self.espaco, self.enviar]

    def Salvar_avaliacao(self):
        empty_list = ['None', None, '', ' ']
        tudo_respondido = True
        for resposta in self.lista_perguntas_entry:              
            if resposta.get().strip() in empty_list:
                tudo_respondido = False 
                break 
        
        if self.label_po_nm['text'] == '--':
            tudo_respondido = False 

        if tudo_respondido:
            # Salvar e apagar os Label, Entry e Button
            self.Salvar_no_JSON()
            Destruir_itens(self.all_itens)
        
        else: 
            messagebox.showerror('Erro ao salvar', 'Todas as perguntas devem ser respondidas e/ou não foi escolhido o PO')
    
    def Salvar_no_JSON(self):
        def get_key():
            try:
                key = int(max(list(historico[self.user.user][nome_do_PO]))) + 1
            except:
                key = 1
            
            return str(key) 

        historico = Ler_JSON('histrc.json')
        
        nome_do_PO = self.label_po_nm['text']

        if not self.user.user in historico:
            historico[self.user.user] = {}
        
        if not nome_do_PO in historico[self.user.user]:
            historico[self.user.user][nome_do_PO] = {}
        
        key = get_key()
        dict_perguntas = self.QnA_como_dict(self.lista_perguntas_label, self.lista_perguntas_entry)
        historico[self.user.user][nome_do_PO][key] = dict_perguntas

        Salvar_JSON('histrc.json', historico)


    def QnA_como_dict(dict, perguntas, respostas):
        cont = 0
        dict_QnA = {}
        for pergunta in perguntas:
            try:
                resposta = respostas[cont]

                if str(type(pergunta)) == "<class 'tkinter.Label'>":
                    pergunta = pergunta['text']
                
                if str(type(resposta)) == "<class 'tkinter.Entry'>":
                    resposta = resposta.get()
                
                dict_QnA[pergunta] = resposta
            except:
                pass 

            cont += 1

        return dict_QnA

    def Criar_labels(self):
        ##########
        # Sprint
        sprints = IntVar(self.jan)
        self.label_sprt = Label(self.jan, text='Sprint', font=self.font)
        self.label_sprt.place(x=50, y=100)

        self.labelScale_sprt = ttk.LabeledScale(self.jan, from_=1, to=5, variable=sprints, compound='button')
        self.labelScale_sprt.place(x=220, y=100)
        ##########

        ##########
        # Turma
        self.label_turm = Label(self.jan, text='Nome da Turma:', font=self.font)
        self.label_turm.place(x=50, y=150)

        self.cliced_trma = StringVar(self.jan)
        self.cliced_trma.set(self.info_turma[0])
        self.label_turm_nm = OptionMenu(self.jan, self.cliced_trma, *self.info_turma, command=lambda _:self.Mudar_times(self.cliced_trma.get()))
        self.label_turm_nm.place(x=220, y=150) 
        ##########

        ##########
        # Time
        self.label_time = Label(self.jan, text='Nome do time:', font=self.font)
        self.label_time.place(x=50, y=200)

        self.label_time_nm = Label(self.jan, text='--', font=self.font)
        self.label_time_nm.place(x=220, y=200)
        ##########

        ##########
        # PO
        self.label_po = Label(self.jan, text='Nome do PO:', font=self.font)
        self.label_po.place(x=50, y=250)

        self.label_po_nm = Label(self.jan, text='--', font=self.font)
        self.label_po_nm.place(x=220, y=250)

        self.lista_label_info = [self.label_sprt, self.labelScale_sprt, self.label_turm, self.label_turm_nm, 
                                self.label_time, self.label_time_nm, self.label_po, self.label_po_nm]

    def Mudar_times(self, key=None):
        try:
            if self.cliced_trma.get() == 'None':
                self.option_time_nm.destroy()
                self.label_time_nm = Label(self.jan, text='--', font=self.font)
                self.label_time_nm.place(x=220, y=200)
            
            else:
                try:
                    self.option_time_nm.destroy()
                except:
                    pass 
                self.label_time_nm.destroy()
                self.info_time = [*self.json_info[key]]
                self.cliced_time = StringVar(self.jan)
                self.cliced_time.set(self.info_time[0])
                self.option_time_nm = OptionMenu(self.jan, self.cliced_time, *self.info_time, command=lambda _: self.Mudar_PO())
                self.option_time_nm.place(x=220, y=200)      

        except:
            pass 
        
        if key == 'None' or self.cliced_time.get() == 'None':
            self.Mudar_PO()

    def Mudar_PO(self):
        try:
            self.label_po_nm['text'] = self.json_info[self.cliced_trma.get()][self.cliced_time.get()]['PO']
        except:
            self.label_po_nm['text'] = '--' 


        
        
        


# jan = Tk()
# AvaliacaoFK(jan)
# jan.mainloop()

