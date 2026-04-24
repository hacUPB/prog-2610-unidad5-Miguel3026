'''
1. Leer el nuevo archivo
2. Leer todo el archivo en forma de lista
3. Imprimir la primera letra de cada linea

'''
aleatorio = open(".\\archivos texto\\texto_aleatorio.txt","r")
fp = aleatorio.readlines()

for i in fp:
    print(i[0])
    aleatorio.close()
    