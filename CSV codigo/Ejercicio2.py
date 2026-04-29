import csv
dias_promedio = 0
with open (".\\CSV archivos\\datos_espacio.csv","r") as csvfile:
    lector = csv.reader(csvfile, delimiter = ";")
    encabezado = next(lector) #Lee la primera fila y la guarda en el encabezado
    for fila in lector:
        dias_promedio += int(fila[3])
        print(fila)
    promedio_total = dias_promedio / 7
    print("Los dias promedio de las misiones en el espacio fue de: {promedio_total} dias")