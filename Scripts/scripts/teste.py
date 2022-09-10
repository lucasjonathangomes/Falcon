
import os
from tkinter import Tk
from tkinter import *
from random import randrange, choice

jan = Tk()

path = os.path(__file__)
print(path)
imagem = PhotoImage(file=path+'\\falcao.png')
Label(jan, image=imagem).pack()


jan.mainloop()




