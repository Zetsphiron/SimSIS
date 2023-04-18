from tkinter import *
import tkinter.messagebox
import re

t = Tk()
t.geometry("400x500")

labelTitle = Label(t, text="VALIDADOR")
labelTitle.place(x=20, y=20)

labelEmail = Label(t, text="Correo")
labelEmail.place(x=20, y=50)
entryText = StringVar()
inputEmail = Entry(t, textvariable=entryText)
entryText.set("usuario@dominio.xyz")
inputEmail.place(x=160, y=50)

labelPass = Label(t, text="Contraseña")
labelPass.place(x=20, y=80)
inputPass = Entry(t, show="•")
inputPass.place(x=160, y=80)

labelPassConfirm = Label(t, text="Repetir contraseña")
labelPassConfirm.place(x=20, y=110)
inputPassConfirm = Entry(t, show="•")
inputPassConfirm.place(x=160, y=110)

buttonCheck = Button(t, text="Comprobar contraseña", command=lambda : passCompare())
buttonCheck.place(x=20, y=150)

buttonConfirm = Button(t, text="Confirmar", command=lambda : validate())
buttonConfirm.place(x=185, y=150)

labelResult = Label(t, text="[ Resultados... ]")
labelResult.place(x=60, y=210)

def passCompare():
    if (inputPass.get() != inputPassConfirm.get()):
        buttonCheck.config(fg = "red")
    else:
        buttonCheck.config(fg = "green")

def validate():
    out = re.compile('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W)(?!.*\s).{12,}$')
    if out.match(inputPass.get()):
        labelResult.config(fg = "green")
        labelResult["text"] = "Bien!"
    else:
        labelResult.config(fg = "red")
        labelResult["text"] = """Mal! Requisitos:
        \nMínimo doce caracteres de longitud\
        \nAl menos una letra mayúscula.\
        \nAl menos una letra minúscula.\
        \nAl menos un caracter especial de los siguientes:
        \n` ~ ! @ # $ % ^ & * ( ) - = _ + [ ]\
        \n{ } ; : ' " < > , . / | \ ?
        \nLa cadena no puede contener espacios en blanco."""


t.mainloop()