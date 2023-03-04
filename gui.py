from tkinter import *

def sumar():
    try:
        resultado["text"]="Resultado: "+str(int(labelC.get())+int(labelB.get()))
    except:
       resultado["text"]="Resultado: error, no se pudo convertir a entero esta cadena"
       
ventana=Tk()
ventana.geometry("400x400")
boton=Button(ventana,text="sumar",command=sumar)
resultado=Label(ventana,text="Resultado:")
boton.place(x=50, y=127)
resultado.place(x=50,y=160)
label=Label(ventana,text="a:")
label.place(x=45, y=50)
labelA=Label(ventana,text="b:")
labelA.place(x=45, y=100)
labelB=Entry(ventana)
labelB.place(x=80, y=100)
labelC=Entry(ventana)
labelC.place(x=80, y=50)
ventana.mainloop()

