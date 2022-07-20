# Importando tudo da bilioteca tkinter
from curses.ascii import alt
import sys, os
from tkinter import *
from turtle import heading
from unittest import result

from sqlalchemy import over

# Cores
preto =        '#212121'
branco =       '#f9fafb'
azul =         '#64b5f6'
cinza_claro =  '#36474f'
cinza_escuro = '#273238'

# Janela
janela = Tk()
janela.title('Calculadora')
janela.config(bg = preto)

# Definindo as dimensões do app
largura = 400
altura = 600

largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

# Definindo o ícone da janela
program_directory = sys.path[0]
janela.iconphoto(True, PhotoImage(file = os.path.join(program_directory, 'icon.png')))

# Criando os Frames
visor = Frame(janela, width = 400, height = 200, bg = preto)
visor.grid(row = 0, column = 0)

botoes = Frame(janela, width = 400, height = 600, bg = cinza_escuro)
botoes.grid(row = 1, column = 0)

# Variável "dígito"
digito = ''

caractere_numerico = StringVar()

# Criando as funções
def entrada_de_valores(event):

    # Tornando a variável dígito reutilizável
    global digito
    digito = digito + str(event)

    # Passando o valor para a tela:
    caractere_numerico.set(digito)

def calcular():
    resultado = eval(digito)
    caractere_numerico.set(resultado)

def limpar_visor():
    global digito
    digito = ''
    caractere_numerico.set('')

# Criando a Label do Visor
app_label = Label(visor, textvariable = caractere_numerico, width = 26, height = 3,
                  relief = FLAT, anchor = 'e', justify = RIGHT, font = ('Ivy 18'),
                  bg = preto, fg = branco)
app_label.place(x = 0, y = 100)

# Criando os Botões
bt_1 = Button(botoes, text = 'C', width = 14, height = 3, bg = cinza_claro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = limpar_visor)
bt_1.place(x = 0, y = 0)

bt_2 = Button(botoes, text = '%', width = 6, height = 3, bg = cinza_claro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('%'))
bt_2.place(x = 198, y = 0)

bt_3 = Button(botoes, text = '/', width = 6, height = 3, bg = cinza_claro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('/'))
bt_3.place(x = 300, y = 0)

bt_4 = Button(botoes, text = '7', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('7'))
bt_4.place(x = 0, y = 80)

bt_5 = Button(botoes, text = '8', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('8'))
bt_5.place(x = 99, y = 80)

bt_6 = Button(botoes, text = '9', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('9'))
bt_6.place(x = 198, y = 80)

bt_7 = Button(botoes, text = 'X', width = 6, height = 3, bg = cinza_claro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('*'))
bt_7.place(x = 299, y = 80)

bt_8 = Button(botoes, text = '4', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('4'))
bt_8.place(x = 0, y = 160)

bt_9 = Button(botoes, text = '5', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('5'))
bt_9.place(x = 99, y = 160)

bt_10 = Button(botoes, text = '6', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('6'))
bt_10.place(x = 198, y = 160)

bt_11 = Button(botoes, text = '-', width = 6, height = 3, bg = cinza_claro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('-'))
bt_11.place(x = 299, y = 160)

bt_12 = Button(botoes, text = '1', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('1'))
bt_12.place(x = 0, y = 240)

bt_13 = Button(botoes, text = '2', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('2'))
bt_13.place(x = 99, y = 240)

bt_14 = Button(botoes, text = '3', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('3'))
bt_14.place(x = 198, y = 240)

bt_15 = Button(botoes, text = '+', width = 6, height = 3, bg = cinza_claro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('+'))
bt_15.place(x = 299, y = 240)

bt_16 = Button(botoes, text = '0', width = 14, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('0'))
bt_16.place(x = 0, y = 320)

bt_17 = Button(botoes, text = '.', width = 6, height = 3, bg = cinza_escuro, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = lambda: entrada_de_valores('.'))
bt_17.place(x = 198, y = 320)

bt_18 = Button(botoes, text = '=', width = 6, height = 3, bg = azul, fg = branco,
              font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE, command = calcular)
bt_18.place(x = 300, y = 320)




janela.mainloop()