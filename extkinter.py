from tkinter import *
from tkinter import ttk
# es la forma que té tkinter per crear la finestra
#root = Tk() tk es una finestra
# ací li donem el format, normalment es fica root.... però com que treballem en objectes canviem a mainWindow
# finestra antes de mofificar, per nosaltres tindre el control i ser més estetica la canviem
#class mainApp():
    #atributs
    #size = "640x480"
    
    #def __init__(self):
        #self.root = Tk()

        #self.root.geometry(self.size)
        #self.root.title("La meua finestra")
        #self.root.configure(bg = "orange")
        
class mainApp(Tk):
    #atributs
    size = "640x480"
    
    def __init__(self):
        Tk.__init__(self)

        self.geometry(self.size)
        self.title("La meua finestra")
        self.configure(bg = "orange")
        
    def start(self):
        self.mainloop()
    
if __name__ == "__main__":
    app = mainApp()
    app.start()




