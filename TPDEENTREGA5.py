# 1. Escriba una función redondear() que permita redondear un número
# decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
# entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
# anterior (3)
"""while True: 
    n= float(input("Ingresa un numero decimal: "))
    print(round(n))"""
# 2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
# módulo que esté fuera de ese paquete, cree una función de suma de
# decimales que redondee el resultado haciendo uso de la función
# redondear() del paquete recién creado.
"""n= float(input("Ingresa un numero decimal: "))
cont=n
while n != 0: 
    n= float(input("Ingresa un numero decimal: "))
    cont=cont+n   
print(round(cont))"""
# 3. Usando el módulo datetime, escribe un programa que muestre la fecha
# y hora actuales del sistema.
"""import datetime
print(datetime.datetime.now().hour,end=":")
print(datetime.datetime.now().minute,end=":")
print(datetime.datetime.now().second,end=":")
print(datetime.datetime.now().microsecond)"""
# 4. Escriba un programa que devuelva un número par al azar entre 2 y 10
# (pista: para comprobar si se pueden generar todos los números, pruebe
# ejecutar el programa dentro de un ciclo infinito).
"""import random
for num in range(20):
    num=random.randint(1,10)
    if num%2==0:
        print(num)"""
# 5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
# para la adivinación o para buscar consejo. Su mecanismo es muy simple:
# ante una pregunta del usuario, la bola responde con una de 8 posibles
# respuestas:
# - Es seguro que sí
# - Las chances son buenas
# - Puedes contar con ello
# - Pregúntame de nuevo más tarde
# - Concéntrate y pregunta de nuevo
# - No veo con claridad, intenta de nuevo
# - Mi respuesta es no
# - Mis fuentes me dicen que no
# Escriba una función en Python para simular la bola mágica.
"""import random
pregunta= input(": ")
num=random.randint(1,8)
if num == 1:
    print("Es seguro que sí")
elif num == 2:
    print("Las chances son buenas")
elif num == 3: 
    print("Puedes contar con ello")
elif num == 4:
    print("Pregúntame de nuevo más tarde")
elif num == 5: 
    print("Concéntrate y pregunta de nuevo")
elif num == 6: 
    print("No veo con claridad, intenta de nuevo")
elif num == 7: 
    print("Mi respuesta es no")
elif num == 8: 
    print("Mis fuentes me dicen que no")"""
# 6. Encuentre el tiempo de ejecución de los programas de los ejercicios
# anteriores (pista: use el módulo time)
"""import time 
inicio= """
# 7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
# toman uno o más papeles al azar de un pozo para elegir los ganadores.
"""lista=["gaston","franco","fede","marcelo","nico","sebastian"]
import random
n= random.randint(1,6)
print(lista[n])"""
# 8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
# nacimiento y sea capaz de devolver la cantidad de días desde su
# nacimiento hasta hoy.

# 9. (Opcional) Implemente el programa del ejercicio 6 usando un diccionario.