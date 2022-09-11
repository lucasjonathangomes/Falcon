
# --------------------------------
# Tela de avaliação do Fake Client
# --------------------------------


from support import * 


class AvaliacaoFK:
    def __init__(self, jan):
        '''Criando os elementos (Botões, Labels,...)'''
        self.jan = jan
        json_turma = Ler_JSON('turma.json')

        default = ['None']

        # self.options_po = ['PO 1', 'PO 2', 'PO 3', 'PO 4', 'PO 5']
        # self.options_sprt = ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4', 'Sprint 5']
        # self.options_trma = ['Turma 1', 'Turma 2', 'Turma 3', 'Turma 4', 'Turma 5']

        label_nm = Label(jan, text='Avaliação Fake Client', font=('Helvetica', 30), fg='blue')
        label_nm.pack()

        # self.cliced = StringVar()
        # self.cliced.set(default[0])
        # turma_bt = OptionMenu(jan, self.cliced, *json_turma['None'])
        # turma_bt.pack()

        self.info_turma = [*json_turma]
        self.Botao_Turma()
        self.Botao_PO()


    # def Botao_Sprint(self, turma):
    #     self.cliced_sprt = StringVar()
    #     self.cliced_sprt.set(turma[0])
    #     self.sprint = OptionMenu(jan, self.cliced_sprt, *turma)
    #     self.sprint.pack() 

    def Botao_Turma(self):
        self.cliced_trma = StringVar()
        self.cliced_trma.set(self.info[0])
        turma_bt = OptionMenu(jan, self.cliced_trma, *self.info)
        turma_bt.pack() 

    def Botao_PO(self):
        self.cliced_po = StringVar()
        self.cliced_po.set(self.info[0])
        po_bt = OptionMenu(jan, self.cliced_po, *self.info)
        po_bt.pack()

    def Button_options(self, txt):
            Label(jan, text=txt).pack()
            print(txt)

    
    def Pegar_elementos_por_chave(self, key):
        pass 

        
        

'''        # # Criando os botões
        # self.cliced_trma = StringVar()
        # self.cliced_trma.set(self.options_trma[0])
        # turma_bt = OptionMenu(jan, self.cliced_trma, *self.options_trma, command=lambda _:self.Button_options(self.cliced_trma.get()))
        # turma_bt.pack()

        # self.cliced_po = StringVar()
        # self.cliced_po.set(self.options_po[0])
        # po_bt = OptionMenu(jan, self.cliced_po, *self.options_po, command=lambda _:self.Button_options(self.cliced_po.get()))
        # po_bt.pack()

        # self.cliced_sprt = StringVar()
        # self.cliced_sprt.set(self.options_sprt[0])
        # sprint = OptionMenu(jan, self.cliced_sprt, *self.options_sprt, command=lambda _:self.Button_options(self.cliced_sprt.get()))
        # sprint.pack()'''




jan = Tk()
AvaliacaoFK(jan)

# options = ['Brasil', 'Argerntina', 'Mexico', 'Colombia', 'Chile']

# cliced = StringVar()
# cliced.set(options[0])




jan.mainloop()
        
