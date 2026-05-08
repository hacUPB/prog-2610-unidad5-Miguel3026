import csv
with open(".\\CSV archivos\\Lista_Aviones.csv","r", encoding = "utf-8") as archivo:
    lector = csv.DictReader(archivo,delimiter=";")

    for fila in lector:
        modelo = fila ["Marca"]
        peso = int(fila["Peso"])

    print(f"El avion {modelo} pesa {peso} kg.")