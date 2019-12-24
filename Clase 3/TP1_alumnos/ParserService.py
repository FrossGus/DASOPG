#ParserService de Gustavo F. Paredes Delaloye
#!/usr/bin/python3

import signal
import socket
import sys
import traceback
import time
import csv
import json
import os #Para poder borrar la pantalla de la consola con os.system ("clear") 

def handler(sig, frame): #Definimos el handler
    os.system ("clear") # Borra la consola
    print (" Hasta Luego !!")
    sys.exit(0)

def LeerConfigTXT():
    archivo = open("/mnt/Shared/GitHub/Repos/DASOPG/Clase 3/TP1_alumnos/config.txt", "r")
    if archivo.readable():
        ruta = archivo.read()
        print("Se leyo config.txt exitosamente")
        archivo.close()

    else:
        print("No se pudo leer config.txt")

    return ruta

def LeerCSV(param_ruta):
    results = []
    with open(param_ruta + "cotizacion.csv","rt",encoding="utf-8") as File:
        reader = csv.DictReader(File, delimiter=',', dialect='excel')

        for fila in reader:
            results.append(fila)

        results_json = json.dumps(results).encode('utf-8')
        EnvioJSON(results_json)

def EnvioJSON(param_JSON):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to {} port {}'.format(server_address[0],server_address[1]))

    sock.connect(server_address)

    try:

        # Send data
        print('Enviando JSON...')
        sent = sock.sendto(param_JSON,server_address)
        print ("JSON Enviado !!")

        # Look for the response
        print('Esperando respuesta...')
        data = sock.recv(1024)
        print("Recibida !!")

    finally:
        print('Cerrando socket')
        sock.close()

signal.signal(signal.SIGINT, handler)

while True:

    os.system ("clear") # Borra la consola

    LeerCSV(LeerConfigTXT())
    time.sleep(24)
    for conteo in [25,26,27,28,29,30]:
        print(conteo)
        time.sleep(1)

