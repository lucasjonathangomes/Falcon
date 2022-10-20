
import numpy as np
import pandas as pd
import seaborn as sb
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

jan = Tk()
jan.title('FALCON - Avaliação 360')
jan.configure(background='white')
jan.attributes('-alpha', 0.9)
width= jan.winfo_screenwidth()  
height= jan.winfo_screenheight() 
jan.geometry("%dx%d" % (width, height)) 

# def Full_Screen(jan, lig_deslg):
#     jan.attributes('-fullscreen', lig_deslg)

# def Apagar(item):
#     item.destroy()


# x = np.linspace(0, 10, 11)
# y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# # fit a linear curve an estimate its y-values and their error.
# a, b = np.polyfit(x, y, deg=1)
# y_est = a * x + b
# y_err = x.std() * np.sqrt(1/len(x) + (x - x.mean())**2 / np.sum((x - x.mean())**2))

# fig, ax = plt.subplots(dpi=100, figsize=(12, 8))
# ax.plot(x, y_est, '-')
# ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
# ax.plot(x, y, 'o', color='tab:brown')

# canvas = FigureCanvasTkAgg(fig, master=jan)
# canvas.draw()
# canvas.get_tk_widget().pack()

# '''
# Trabelho em equipe, cooperação e descentralização de conhecimento:
# Iniciativa e proatividade:
# Autodidaxia e agregação de conhecimento ao grupo:

# Entrega de resultados e participação efetiva no projeto:
# Competência técnica:
# '''
# jan.mainloop()

fig, ax = plt.subplots(dpi=100, figsize=(12, 8))

cars = pd.read_csv('C:\\Users\\LBerto1\\Study_Area\\Python\\Course\\DataScience\\Data\\mtcars.csv')
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

cars.index = cars.car_names

g1 = cars[['cyl', 'wt', 'mpg']]
colors = ['darkgray', 'lightsalmon', 'powderblue']
# g1.plot(color=colors)
ax.plot(g1, '-')
# ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
# ax.plot(x, y, 'o', color='tab:brown')


canvas = FigureCanvasTkAgg(fig, master=jan)
canvas.draw()
canvas.get_tk_widget().pack()
jan.mainloop()
