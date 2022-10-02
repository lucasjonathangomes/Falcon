
from random import randint
from support import *


class Avaliar:
    def __init__(self, jan):
        self.jan = jan
        self.path = Caminho_ate_Falcon()+"//fotos//"
        self.all_info = Ler_JSON('turma.json')

        self.jan.geometry("1440x1024+350+20")
        self.jan.iconbitmap(default=self.path+"avaliacao.png")
        self.jan.resizable(width=FALSE, height=FALSE)

        self.Criar_Label()

    def Criar_Label(self):
        self.img_fundo = Retorna_imagem('avaliacao.png')
        self.img_botao = Retorna_imagem("botao.png")
               
        self.label_fundo = Label(self.jan, image=self.img_fundo)
        self.label_fundo.pack()

        self.turmas = list(self.all_info)
        self.times = []
        self.pessoas = []

        # ComboBox das Turmas
        self.ComboBox_turma = ttk.Combobox(values=self.turmas)
        self.ComboBox_turma.place(width=500, height=60, x=290, y=155)
        self.ComboBox_turma.bind("<<ComboboxSelected>>", lambda _: self.Atualizar_Combobox(self.ComboBox_turma, 'time'))

        # ComboBox dos Times
        self.ComboBox_time = ttk.Combobox(values=self.times)
        self.ComboBox_time.place(width=500, height=60, x=290, y=245)
        self.ComboBox_time.bind("<<ComboboxSelected>>", lambda _: self.Atualizar_Combobox(self.ComboBox_time, 'pessoa'))

        # ComboBox das Pessoas 
        self.ComboBox_pessoa = ttk.Combobox(values=self.pessoas)
        self.ComboBox_pessoa.place(width=500, height=60, x=290, y=325)
        # self.ComboBox_pessoa.bind("<<ComboboxSelected>>")

        self.entry1 = Entry(self.jan, bd=2, font=("Calibri", 20), justify=LEFT)
        self.entry1.place(width=100, height=60, x=790, y=440)

        self.entry2 = Entry(self.jan, bd=2, font=("Calibri", 20), justify=LEFT)
        self.entry2.place(width=100, height=60, x=790, y=525)

        self.entry3 = Entry(self.jan, bd=2, font=("Calibri", 20), justify=LEFT)
        self.entry3.place(width=100, height=60, x=790, y=655)

        self.entry4 = Entry(self.jan, bd=2, font=("Calibri", 20), justify=LEFT)
        self.entry4.place(width=100, height=60, x=790, y=790)

        self.entry5 = Entry(self.jan, bd=2, font=("Calibri", 20), justify=LEFT)
        self.entry5.place(width=100, height=60, x=790, y=880)

        self.perguntas = [
            'Trabelho em equipe, cooperação e descentralização de conhecimento:',
            'Iniciativa e proatividade:',
            'Autodidaxia e agregação de conhecimento ao grupo:',
            'Entrega de resultados e participação efetiva no projeto:',
            'Competência técnica:'
        ]
        self.respostas = [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5]
        # self.botaoEnviar = Button(self.jan, bd=0, image=self.img_botao, command=self.Enviar)
        self.botaoEnviar = Button(self.jan, text='Enviar', command=self.Enviar)
        # self.botaoCadastro.place(width=279, height=69, x=550, y=805)
        self.botaoEnviar.place(width=279, height=69, x=800, y=505)


    def Enviar(self):
        self.times.append(randint(1, 100))
        self.ComboBox_time['values'] = self.times
        # print(self.times)
    
    def Atualizar_Combobox(self, combox, oq_atualizar):
        combox = combox.get().strip()
        try:
            if oq_atualizar.lower() == 'time':
                combox_turma = self.ComboBox_turma.get()
                nova_lista = list(self.all_info[combox_turma])
                self.ComboBox_time['values'] = nova_lista

            elif oq_atualizar.lower() == 'pessoa':
                key = '' # Pegar quem vai avaliar com base no cargo da pessoa
                combox_turma = self.ComboBox_turma.get()
                combox_time = self.ComboBox_time.get()
                # nova_lista = list(self.all_info[combox_turma][combox_time][key])
                # nova_lista = self.all_info[combox_turma][combox_time]['Desenvolvedores']
                nova_lista = list(self.all_info[combox_turma][combox_time]['Desenvolvedores'])
                self.ComboBox_pessoa['values'] = nova_lista 
        except:
            messagebox.showerror(f'{oq_atualizar} invalida', f'{oq_atualizar} "{combox}" não existe. Seleciona da lista')
        
          
    def Nivel_de_acesso(self):
        pass 

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
# Avaliar(jan)
# jan.mainloop()

