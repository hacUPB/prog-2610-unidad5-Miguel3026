import csv
peso_total = 0
with open (".\\CSV archivos\\Lista_Aviones.csv","r") as csvfile:
    lector = csv.reader(csvfile, delimiter = ";")
    encabezado = next(lector) #Lee la primera fila y la guarda en el encabezado
    for fila in lector:
        peso_total += int(fila[4])
        print(fila)

print(f"Peso total de los aviones: {peso_total} kg")