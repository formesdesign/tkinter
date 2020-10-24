from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    __temperaturaAnt = "" #creen una cadena
    
        #finestra    
    def __init__(self):
        Tk.__init__(self)
        self.geometry("210x150")
        self.title("TERMOMETRE")
        self.configure(bg = "orange")
        self.resizable(0,0)#es x que la finestra tinga el tamany que li donem
        
        self.temperatura = StringVar(value="")
        #trace es de tk, w: vol dir escriue, farem un nou metode
        self.temperatura.trace("w", self.validateTemperature)
        self.tipoUnidad = StringVar(value="C")

        #metodo creen un nou, lo que anem a ficar en la finestra
        self.createLayout()

        #variables de control especifiques del Tk
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lblUnidad = ttk.Label(self, text="Graus:").place( x=10, y=45)
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F",command=self.selected).place(x=20, y=70)
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C",command=self.selected).place(x=20, y=100)


    def start(self):
        self.mainloop()
        
    def validateTemperature(self, *args):#args son arguments de tk
        nuevoValor = self.temperatura.get()
        #amb get extraigo el valor, amb set
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
        except:
            self.temperatura.set(self.__temperaturaAnt)
            
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == "F":
            resultado = grados *9/5 +32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        self.temperatura.set(resultado)
        
    
if __name__ == "__main__":
    app = mainApp()
    app.start()





