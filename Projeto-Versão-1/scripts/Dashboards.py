
import numpy as np
import pandas as pd
import seaborn as sb
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

jan = Tk()
jan.title('FALCON - Avaliação 360')
# jan.geometry('900x500')
jan.configure(background='white')
# jan.resizable(width=False, height=False)
jan.attributes('-alpha', 0.9)
# jan.attributes('-fullscreen', True)
width= jan.winfo_screenwidth()  
height= jan.winfo_screenheight() 
jan.geometry("%dx%d" % (width, height)) 

def Full_Screen(jan, lig_deslg):
    jan.attributes('-fullscreen', lig_deslg)

def Apagar(item):
    item.destroy()

# frame_direito = Frame(jan, width=500 , height=500)#, bg='blue')
# frame_direito.place(x=700, y=10)

# frame_esquerdo = Frame(jan, width=500 , height=500)#, bg='midnightblue')
# frame_esquerdo.place(x=190, y=10)

# Button(frame_direito, text='Ligar Fullscreen', command=lambda:Full_Screen(jan, True)).pack()
# Button(frame_direito, text='Desligar Fullscreen', command=lambda:Full_Screen(jan, False)).pack()

# Label(frame_esquerdo, text='Testando... 1').pack()
# Label(frame_esquerdo, text='Testando... 2').pack()
# Button(frame_esquerdo, text='Apagar frame diretito', command=lambda:Apagar(frame_direito)).pack()

# cars = pd.read_csv('C:\\Users\\LBerto1\\Study_Area\\Python\\Course\\DataScience\\Data\\mtcars.csv')
# cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# cars.index = cars.car_names

# mpg = cars['mpg']

# sb.catplot(mpg)

# nomes = ['Lukas', 'Maria', 'Jão', 'Larissa']
# cores = ['green', 'blue', 'purple', 'yellow']
# notas = [10, 9, 8, 8]

# fig, axs = plt.subplots(dpi=100, figsize=(12, 8), facecolor='#A0DCF6')
# fig.suptitle('Graficos')
# axs.bar(nomes, notas, color=cores)

# canvas = FigureCanvasTkAgg(fig, master=jan)
# canvas.draw()
# canvas.get_tk_widget().pack()

x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve an estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) + (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots(dpi=100, figsize=(12, 8))
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')

canvas = FigureCanvasTkAgg(fig, master=jan)
canvas.draw()
canvas.get_tk_widget().pack()

'''
perguntas = [
            'Trabelho em equipe, cooperação e descentralização de conhecimento:',
            'Iniciativa e proatividade:',
            'Autodidaxia e agregação de conhecimento ao grupo:',
            'Entrega de resultados e participação efetiva no projeto:',
            'Competência técnica:'
]

## Graficos interessantes para usar ##

sb.regplot(x='hp', y='mpg', data=cars, scatter=True)

cars.plot(kind='scatter', x='hp', y='mpg', c=['green'], s=150)

sb.catplot(mpg)

plt.plot(x, y, ds='steps', lw=5)
plt.plot(x, y, lw=5)
plt.show()

g1 = df[['cyl', 'wt', 'mpg']]
colors = ['darkgray', 'lightsalmon', 'powderblue']
g1.plot(color=colors)

'''

# a = {1: 10, 2:20, 3:30, 4:40, 5:50}
# b = list(a.values())

# plt.pie(b)
# plt.legend(loc='upper right')
# plt.show()

jan.mainloop()

