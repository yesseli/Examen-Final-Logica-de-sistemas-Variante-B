from tkinter import ttk
from tkinter import *

# ("I Curso")
# ("II Semestre")
# ("III Su Nobre Completo")
# ("IV Su Número De Carné")
class Desk:
    def __init__(self, window):
        
        anchura = 1000   
        altura = 800
          
        self.wind = window

        self.wind.geometry(str(anchura)+'x'+str(altura))
 
        self.wind.columnconfigure(0, weight=1)
        
        self.wind.title('Examen Final')

        frame = LabelFrame(self.wind, text = 'Calificacion')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        Label(frame, text = 'Ingrese el primer numero: ').grid(row = 1, column = 0)
        
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        Label(frame, text = 'Ingrese el segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        

        Label(frame, text = 'Ingrse el segundo numero: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, column = 1)
        
      
        Button (frame, text = 'Iniciar', command = self.bottonR).grid(row = 6, columnspan = 5, sticky = W + E)
        Button (frame, text = 'Mostrar', command = self.bottonD).grid(row = 7, columnspan = 5, sticky = W + E)
     
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    
    def bottonR(self):
        a=float(self.var1.get())
        b=float(self.var2.get())
        c=float(self.var3.get())
        if (a<c):
            self.message['text'] = 'La Operacion Es y A es Menor : {}'.format(a*b*c)
        elif(a==c):
            self.message['text'] = 'A y C son Iguales LA SUMA ES : {}'.format(a+b+c)
        elif(b==0):
            print ("La Resta Es:",a-c)
            self.message['text'] = 'Y es Igual a 0 : {}'.format(a-c)
        else:
            print ("Ingrese los Numeros")

    def bottonD(self):
    
        if(1, 2, 3):
          self.message['text'] = "Concatenacion de nuemros : {}".format(1==2==3)
        elif(1 ,2, 3):
          self.message['text'] = 'Repeticion de numero  : {}'.format(1*2+3)
        else:
           print ("Ingrese Un  Numero")
  
   
   

if __name__ == '__main__':
    
    window = Tk()
    
    app = Desk(window)

    window.mainloop()