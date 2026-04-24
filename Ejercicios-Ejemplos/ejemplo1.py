# Abre o crea un archivo en modo escritura
# objeto recibe (mi_archivo): nombre del archivo, ubicacion, modo de apertura y mas información

mi_archivo = open("saludo.txt","a")
mi_archivo.write("\nEste es un ejemplo de uso de abrir, escribir, editar, cerrar archivos")
mi_archivo.close() # Importante: cierra y guarda el documento 