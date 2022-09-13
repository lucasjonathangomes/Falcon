
from support import * 

class AvaliacaoFK:
    def __init__(self, jan):
        '''Criando os elementos (Botões, Labels,...)'''
        self.jan = jan
        self.json_info = Ler_JSON('turma.json')

        label_nm = Label(jan, text='Avaliação Fake Client', font=('Helvetica', 30), fg='blue')
        label_nm.pack()

        self.info_turma = [*self.json_info]
        self.info_time = ['None']
        self.info_sprt = ['None']

        self.font = ('Arial', 15)

        


        self.Criar_labels()


    def Criar_labels(self):
        ##########
        # Turma
        self.label_turm = Label(self.jan, text='Nome da Turma:', font=self.font)
        self.label_turm.place(x=50, y=150)

        self.cliced_trma = StringVar(self.jan)
        self.cliced_trma.set(self.info_turma[0])
        self.label_turm_nm = OptionMenu(jan, self.cliced_trma, *self.info_turma, command=lambda _:self.Mudar_times(self.cliced_trma.get()))
        self.label_turm_nm.place(x=220, y=150) 
        ##########

        ##########
        # Time
        self.label_time = Label(self.jan, text='Nome do time:', font=self.font)
        self.label_time.place(x=50, y=200)

        self.cliced_time = StringVar(self.jan)
        self.cliced_time.set('None')
        self.option_time_nm = OptionMenu(jan, self.cliced_time, 'None')
        self.option_time_nm.place(x=220, y=200)
        ##########

        ##########
        # PO
        self.label_po = Label(self.jan, text='Nome do PO:', font=self.font)
        self.label_po.place(x=50, y=250)

        self.label_po_nm = Label(self.jan, text='--', font=self.font)
        self.label_po_nm.place(x=220, y=250)
        ##########


        self.butttto = Button(self.jan, text='--', command=lambda: self.PRINT())
        self.butttto.place(x=100, y=100)
    

    def Mudar_times(self, key):        
        try:
            menu = self.label_time_nm["menu"]
            menu.delete(0)
        except:
            pass 

        lista_de_times = [*self.json_info[key]]
        
        self.option_time_nm.destroy()
        self.cliced_time = StringVar(self.jan)
        self.cliced_time.set(lista_de_times[0])
        self.option_time_nm = OptionMenu(jan, self.cliced_time, *lista_de_times, command=lambda _: self.Mudar_PO())
        self.option_time_nm.place(x=220, y=200)

        if key == 'None':
            self.Mudar_PO()

        
        
        # self.cliced_time.set(lista_de_times[0])
        # self.label_time_nm['command'] = self.Mudar_PO
        # self.label_time_nm.config(command=self.Mudar_PO)

        self.info_time = ['None', *lista_de_times]

    def Mudar_PO(self):
        print('veio')
        try:
            self.label_po_nm['text'] = self.json_info[self.cliced_trma.get()][self.cliced_time.get()]['PO']
        except:
            self.label_po_nm['text'] = '--' 

        




jan = Tk()

# menu = Menu(jan)
# menu2 = Menu(menu, tearoff=0)
# menu2.add_command(label='Teste 1')
# menu2.add_command(label='Teste 2')
# menu2.add_command(label='Teste 3')
# menu2.add_command(label='Teste 4', command=lambda:AvaliacaoFK(jan))

# menu.add_cascade(label='Perfil', menu=menu2, )
# jan.config(menu=menu, width=20, height=50)
# jan.config()

AvaliacaoFK(jan)
jan.mainloop()
        
