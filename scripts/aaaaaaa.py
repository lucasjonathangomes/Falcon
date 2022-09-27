
from support import *


a = Tk()

p=['Cargo']
p2 = ['1,', '2sss']

d = Frame(a, width=800, height=800)
d.place(x=500, y=500)
Label(a, text='Nadalrete', font=("Comic Sans MS", 20, "bold")).pack()

Criar_Perguntas(a, perguntas=p2, answer_style='entry', font=('Bree Serif', 20, 'bold'))
Criar_Perguntas(d, perguntas=p, answer_style='combobox', values=[1,2,3,4,5], font=('Arial', 30, 'bold'))

a.mainloop()


