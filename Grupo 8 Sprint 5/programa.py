"""Instalar previamente las librerias que estan en requirements.txt y luego ejecutar este programa"""


from funciones import *
from clases import *
import os

def main():
    os.system("cls")
    rechazo = []
    nombreJSON = input("Ingrese el nombre del archivo (por ejemplo 'eventos.json'): ")
    tps = leerJSON(nombreJSON)
    cliente = handlerTipoCliente(tps["tipo"] ,tps)
    
    for transaccion in cliente.transacciones:
        if transaccion["estado"] == "RECHAZADA":
            rechazo.append(handlerTipoTransaccion(transaccion, cliente))
        else:
            rechazo.append("-")

    generarHTML(tps, rechazo) #Se genera un archivo html llamado reporte


main()


