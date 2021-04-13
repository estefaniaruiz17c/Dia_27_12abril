# importar las librerías requeridas
import matplotlib.pyplot as plt

# Para acceder al archivo de texto de 'arch1.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
arch1 = open('arch1.txt','r')
texto1lis = arch1.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
arch1.close()

# De la manera como está escrito el archivo, cada dato va acompañado de un '\n', esto debe eliminarse para que los datos puedan entrar en el formato de la gráfica. En este paso eliminaremos estos '\n' de cada dato
print()
print(texto1lis)
print()
dato1 = (texto1lis[1].rstrip('\n'))
dato2 = (texto1lis[2].rstrip('\n'))
dato3 = (texto1lis[3].rstrip('\n'))
dato4 = (texto1lis[4].rstrip('\n'))
dato5 = (texto1lis[5].rstrip('\n'))
dato6 = (texto1lis[6].rstrip('\n'))

# Conversión de los números de string a int
num1 = int(dato1)
num2 = int(dato2)
num3 = int(dato3)
num4 = int(dato4)
num5 = int(dato5)
num6 = int(dato6)

# Creación de las listas con los datos para la gráfica
lista1 =[num1,num2,num3,num4,num5,num6]

# Creación de la gráfica y estilo de la misma
plt.plot(lista1,'r')

# Establecer nombres de los ejes
plt.xlabel ('Semana')
plt.ylabel('Cantidad de lluvias')

# Establecer título de la gráfica
plt.title('Precipitaciones')

# Guardar en formato PNG
plt.savefig("Gráfica precipitaciones.png")

# Cerrar la ejecución de la gráfica
plt.close()

print("--------"*7)

# importar las librerías requeridas
import matplotlib.pyplot as plt

# Apertura del archivo que contiene los datos a utilizar
arch2 = open('arch2.txt','r')
texto2lis = arch2.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
arch2.close()

# De la manera como está escrito el archivo, cada dato va acompañado de un '\n', esto debe eliminarse para que los datos puedan entrar en el formato de la gráfica. En este paso eliminaremos estos '\n' de cada dato
print()
print(texto2lis)
print()
dato1_arch2 = (texto2lis[1].rstrip('\n'))
dato2_arch2 = (texto2lis[2].rstrip('\n'))
dato3_arch2 = (texto2lis[3].rstrip('\n'))
dato4_arch2 = (texto2lis[4].rstrip('\n'))
dato5_arch2 = (texto2lis[5].rstrip('\n'))
dato6_arch2 = (texto2lis[6].rstrip('\n'))
dato7_arch2 = (texto2lis[7].rstrip('\n'))
dato8_arch2 = (texto2lis[8].rstrip('\n'))

# Conversión de los números de string a float
num1_arch2 = float(dato1_arch2)
num2_arch2 = float(dato2_arch2)
num3_arch2 = float(dato3_arch2)
num4_arch2 = float(dato4_arch2)
num5_arch2 = float(dato5_arch2)
num6_arch2 = float(dato6_arch2)
num7_arch2 = float(dato7_arch2)
num8_arch2 = float(dato8_arch2)

# Creación de las listas con los datos para la gráfica
lista1_arch2 = [num1_arch2,num2_arch2,num3_arch2,num4_arch2]
lista2_arch2 = [num5_arch2,num6_arch2,num7_arch2,num8_arch2]

liista = [lista1_arch2,lista2_arch2]

# Creación de la gráfica y estilo de la misma
plt.plot(lista1_arch2,'b--', lista2_arch2, 'g--')

# Establecer nombres de los ejes
plt.xlabel ('Semana')
plt.ylabel('Notas')

# Establecer título de la gráfica
plt.title('Desempeño de los estudiantes. Verde: grupo A. Azul: grupo B')

# Guardar la imagen en PNG
plt.savefig("Desempeño de estudiantes.png")

# Cerrar la ejecución de la gráfica
plt.close()

