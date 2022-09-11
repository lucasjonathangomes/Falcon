
from dataclasses import InitVar
from tkinter.ttk import LabeledScale
from support import * 

class AvaliacaoFK:
    def __init__(self, jan):
        '''Criando os elementos (Botões, Labels,...)'''
        self.jan = jan
        self.json_info = Ler_JSON('turma.json')

        label_nm = Label(jan, text='Avaliação Fake Client', font=('Helvetica', 30), fg='blue')
        label_nm.pack()

        self.info_turma = [*self.json_info]
        self.info_sprt = ['None']
        self.nome_PO = 'None'


        self.cliced_trma = StringVar()
        self.cliced_trma.set(self.info_turma[0])
        turma_bt = OptionMenu(jan, self.cliced_trma, *self.info_turma, command=lambda _:self.Mudar_nome(self.cliced_trma.get()))
        turma_bt.pack() 

        self.po_bt = Label(jan, text=self.nome_PO, fg='green')
        self.po_bt.pack()

        self.Criar_labels()


    def Criar_labels(self):
        font = ('Arial', 20)

        a = IntVar(self.jan)

        self.label_sprt = Label(self.jan, text='Sprint', font=font)
        self.label_sprt.place(x=50, y=100)

        self.labelScale_sprt = LabeledScale(self.jan, from_=1, to=5, variable=a, compound='button')
        self.labelScale_sprt.place(x=200, y=100)

        print(lambda _: a.get())

        self.label_turm = Label(self.jan, text='Nome da Turma:', font=font)
        self.label_turm.place(x=50, y=300)

        self.label_po = Label(self.jan, text='Nome do PO:', font=font)
        self.label_po.place(x=100, y=400)

        self.label_po_nm = Label(self.jan, text='Nome do PO:', font=font)
        self.label_po_nm.place(x=250, y=400)

        

    def Mudar_nome(self, key):
        if key == 'None':
            novo_texto = 'None'
        else:
            novo_texto = self.json_info[key]['PO']
        
        self.label_po_nm['text'] = novo_texto


        
    def Print(self):
        pass 


jan = Tk()
AvaliacaoFK(jan)
jan.mainloop()
        
