import tkinter as tk
import logging 
#from binance_futures import write_log
from bitmex import get_contracts

logger = logging.getLogger()

#Seteamos en minimo logging level a Info por lo que solo mensajes de Info, Warning y Error se mostrarán
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter  = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug("This message is important only when debugging the program")
logger.info("This message just show basic information")
logger.warning("This message is about something you should pay attention to")
logger.error("This message helps to debug an error that occurred in your program")

#write_log()

if __name__ == '__main__':
    bitmex_contracts = get_contracts()
    #logger.info('This is logged only if we execute the main.py file')
    root = tk.Tk()
    #también le podemos colocar un color fondo a la ventana
    root.configure(bg="gray12")

    i=0
    j=0

    #creamos una fuente
    calibri_font = ("Calibri", 11, "normal")
    
    for contract in bitmex_contracts:
        #(ventana principal del widget, texto del label)
        label_widget = tk.Label(root, text=contract, borderwidth=1, relief=tk.SOLID, width=13, bg='gray12', fg='SteelBlue1', font=calibri_font)
        #es como una tabla a la que podemos pasar las columnas y las filas
        #grid()
        #posiciona los labels relativamente al anterior, es bueno si tenemos pocos elementos
        #pack()
        #los pocionamos verticalmente iniciando desde arriba
        #label_widget.pack(side=tk.TOP)
        #label_widget.pack(side=tk.LEFT)

        label_widget.grid(row=i, column=j, sticky='ew')
        if i == 4:
            j+=1
            i=0
        else:
            i+=1

    #es un eventloop, este loop espera por acciones del usuario como clicks o tecleo
    root.mainloop()