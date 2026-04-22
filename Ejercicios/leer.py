fp = open(".\\archivos texto\\ejercicio1.txt","r")
datos_1 = fp.readline()
print("Primera lectura: ", datos_1)

datos_2 = fp.read(5)
print("Segunda lectura: ", datos_2)  

datos_3 = fp.read()
print("tercera lectura: ", datos_3)
fp.close()
