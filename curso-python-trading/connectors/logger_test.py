import tkinter as tk
import logging 
from binance_futures import writte_log

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

writte_log()

if __name__ == '__main__':
    logger.info('This is logged only if we execute the main.py file')
    root = tk.Tk()
    #es un eventloop, este loop espera por acciones del usuario como clicks o tecleo
    root.mainloop()