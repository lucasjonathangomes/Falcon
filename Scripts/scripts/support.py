
import os
from tkinter import Tk
from tkinter import *
from random import randrange, choice
from re import findall


def Imagem(nome):
    '''Retorna a imagem da pasta "fotos"'''
    path = findall(r'.*Scripts', os.path.dirname(__file__))[0]
    return PhotoImage(file=f'{path}\\fotos\\{nome}')





