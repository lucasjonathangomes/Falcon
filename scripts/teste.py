from support import * 

jan = Tk()

# frame_dos_filtros = Frame(jan, width=500 , height=500)#, bg='blue')
# frame_dos_filtros.place(x=190, y=10)

# frame_das_perguntas = Frame(jan, width=500 , height=500)#, bg='midnightblue')
# frame_das_perguntas.place(x=700, y=10)

# perguntas = [
#             'Trabelho em equipe, cooperação e descentralização de conhecimento:',
#             'Iniciativa e proatividade:',
#             'Autodidaxia e agregação de conhecimento ao grupo:',
#             'Entrega de resultados e participação efetiva no projeto:',
#             'Competência técnica:'
# ]

# valores = [1, 2, 3, 4, 5]

# def Apagar(item):
#     item.destroy()

# Label(frame_dos_filtros, text='Aqui é onde vai os filtros').pack()
# Label(frame_das_perguntas, text='Aqui é onde vai sa perguntas').pack()
# # ttk.Combobox(frame_dos_filtros, font=('Arial', 10)).pack()
# respostas = Criar_Perguntas(frame_das_perguntas, perguntas)
# respostas = Criar_Perguntas(frame_dos_filtros, perguntas, values=valores, answer_style='combobox')

def Zerar_Valores():
    for z in lista:
        z.delete(0, END)

a = ttk.Combobox(jan, font=('Arial', 10), values=[1,2,3,4,5])
a.pack()
b = ttk.Combobox(jan, font=('Arial', 10), values=[1,2,3,4,5])
b.pack()
c = ttk.Combobox(jan, font=('Arial', 10), values=[1,2,3,4,5])
c.pack()
lista = [a,b,c]
Button(jan, text='Zerar valores', command=Zerar_Valores).pack()
jan.mainloop()



