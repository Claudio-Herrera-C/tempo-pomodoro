#import
import time
import os

#code 
run = input("Comienzan los 25 minutos de focus... [y/n]")
mins=0   

def _borrar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')




if(run== "y"):
    _borrar_pantalla()
    print("para salir usa Contol + C")
    try:
        while mins !=25:
            print(">"*35 + "{}".format(mins))
            time.sleep(60)
            mins += 1   

    except KeyboardInterrupt:
        _borrar_pantalla()