# importando tkinter
from tkinter import *
from tkinter import ttk

#Coloração da interface
cor1 = "#3b3b3b" # preto
cor2 = "#feffff" # branco
cor3 = "#38576b" # azul
cor4 = "#eceff1" # cinza
cor5 = "#ffab40" # laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("240x310")
janela.config(bg=cor1)

# Variaveis
valores = ""
valorTexto = StringVar()

#Funções
def entradaValor(event):
    global valores

    valores = valores + str(event)
    valorTexto.set(valores)

def calcular():
    global valores
    resultado = str(eval(valores))
    valorTexto.set(resultado)
    valores = ""

def apagar():
    global valores
    valores = ""
    valorTexto.set("")

#colocando uma linha horizontal
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=119)

#criando display
frameTela = Frame(janela, width=240, height=50, bg=cor3, pady=0, padx=0, relief=FLAT)
frameTela.grid(row=0, column=0, sticky=NW)

#criando onde ficaram os botões
frameCorpo = Frame(janela, width=240, height=260, pady=0, padx=0, relief=FLAT)
frameCorpo.grid(row=1, column=0, sticky=NW)

#inserindo numeros na tela
app_tela = Label(frameTela, textvariable=valorTexto, width=16, height=2, padx=7, relief=FLAT, anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg="#37474f", fg=cor2)
app_tela.place(x=0, y=0)

# criando botões
button1 = Button(frameCorpo, command=lambda:apagar(), text="C", width=17, height=2, bg=cor2,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button1.place(x=0, y=0)

#button2 = Button(frameCorpo, command=lambda:entradaValor("%"), text="%", width=5, height=2, bg=cor2,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
#button2.place(x=120, y=0)

button3 = Button(frameCorpo, command=lambda:entradaValor("/"), text="/", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button3.place(x=180, y=0)

button4 = Button(frameCorpo, command=lambda:entradaValor("7"), text="7", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button4.place(x=0, y=52)

button5 = Button(frameCorpo, command=lambda:entradaValor("8"), text="8", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button5.place(x=60, y=52)

button6 = Button(frameCorpo, command=lambda:entradaValor("9"), text="9", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button6.place(x=120, y=52)

button7 = Button(frameCorpo, command=lambda:entradaValor("*"), text="*", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button7.place(x=180, y=52)

button8 = Button(frameCorpo, command=lambda:entradaValor("4"), text="4", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button8.place(x=0, y=104)

button9 = Button(frameCorpo, command=lambda:entradaValor("5"), text="5", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button9.place(x=60, y=104)

button10 = Button(frameCorpo, command=lambda:entradaValor("6"), text="6", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button10.place(x=120, y=104)

button11 = Button(frameCorpo, command=lambda:entradaValor("-"), text="-", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button11.place(x=180, y=104)

button12 = Button(frameCorpo, command=lambda:entradaValor("1"), text="1", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button12.place(x=0, y=156)

button13 = Button(frameCorpo, command=lambda:entradaValor("2"), text="2", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button13.place(x=60, y=156)

button14 = Button(frameCorpo, command=lambda:entradaValor("3"), text="3", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button14.place(x=120, y=156)

button15 = Button(frameCorpo, command=lambda:entradaValor("+"), text="+", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button15.place(x=180, y=156)

button16 = Button(frameCorpo, command=lambda:entradaValor("0"), text="0", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button16.place(x=0, y=208)

button17 = Button(frameCorpo, command=lambda:entradaValor("."), text=".", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button17.place(x=120, y=208)

button18 = Button(frameCorpo, command=lambda:calcular(), text="=", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button18.place(x=180, y=208)

janela.mainloop()