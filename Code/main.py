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

#Estilo da janela
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=120)

#criando display
frameTela = Frame(janela, width=240, height=50, bg=cor3, pady=0, padx=0, relief=FLAT)
frameTela.grid(row=0, column=0, sticky=NW)

#criando onde ficaram os botões
frameCorpo = Frame(janela, width=240, height=268, pady=0, padx=0, relief=FLAT)
frameCorpo.grid(row=1, column=0, sticky=NW)

# criando botões
button1 = Button(frameCorpo, text="C", width=11, height=2, bg=cor2,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button1.place(x=0, y=0)

button2 = Button(frameCorpo, text="%", width=5, height=2, bg=cor2,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button2.place(x=120, y=0)

button3 = Button(frameCorpo, text="/", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button3.place(x=180, y=0)

button4 = Button(frameCorpo, text="7", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button4.place(x=0, y=52)

button5 = Button(frameCorpo, text="8", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button5.place(x=60, y=52)

button6 = Button(frameCorpo, text="9", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button6.place(x=120, y=52)

button7 = Button(frameCorpo, text="*", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button7.place(x=180, y=52)

button8 = Button(frameCorpo, text="4", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button8.place(x=0, y=104)

button9 = Button(frameCorpo, text="5", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button9.place(x=60, y=104)

button10 = Button(frameCorpo, text="6", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button10.place(x=120, y=104)

button11 = Button(frameCorpo, text="-", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button11.place(x=180, y=104)

button12 = Button(frameCorpo, text="1", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button12.place(x=0, y=156)

button13 = Button(frameCorpo, text="2", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button13.place(x=60, y=156)

button14 = Button(frameCorpo, text="3", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button14.place(x=120, y=156)

button15 = Button(frameCorpo, text="+", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button15.place(x=180, y=156)

button16 = Button(frameCorpo, text="0", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button16.place(x=0, y=208)

button17 = Button(frameCorpo, text=".", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button17.place(x=120, y=208)

button18 = Button(frameCorpo, text="=", width=5, height=2, bg=cor5, fg=cor1,font=('Ivy 13 bold'), relief=FLAT, overrelief=RIDGE)
button18.place(x=180, y=208)

janela.mainloop()