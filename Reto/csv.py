import csv
import statistics
import matplotlib.pyplot as plt

def vista_previa_de_datos():
   import csv
datos = []
ruta_archivo = input("Ingrese la ruta del archivo:")
with open (ruta_archivo, "r", encoding= "utf-8") as csvfile:
  lector = csv.DictReader(csvfile)

  for fila in lector:
     datos.append(fila)

print("\n--PRIMERAS 1O FILAS--")

for fila in datos[:10]:
        print(fila)

print("\n--ÚLTIMAS 5 FILAS --")

for fila in datos[-5:]:
        print(fila)



    