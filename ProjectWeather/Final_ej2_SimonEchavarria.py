#Simon Echavarria
import random

def calcular_promedios(dias_promedios):
    promedios = []
    if dias_promedios > len(matriz):
          print("No hay suficientes elementos en la matriz")
    promedio_max = round(temp_max_total / dias_promedios,1)
    promedio_min = round(temp_min_total / dias_promedios,1)
    promedio_precipitacion = round(precipitacion_total / dias_promedios,1)
    promedios = [promedio_max, promedio_min, promedio_precipitacion]
    print("El promedio de los primeros",dias_promedios, " dias es: ", promedios )
    return promedios

matriz = []
temp_max_total = 0
temp_min_total = 0
precipitacion_total = 0
n=int(input("Ingrese el numero de dias: "))
for i in range(1,n + 1):
    dia_n = "Dia " + str(i)
    #Tomado de: https://www.w3schools.com/python/ref_random_uniform.asp
    temperatura_max = round(random.uniform(15,28),1)
    temp_max_total += temperatura_max
    temperatura_min = round(random.uniform(15,28),1)
    while temperatura_min > temperatura_max:
            temperatura_min = round(random.uniform(15,28),1)
    temp_min_total += temperatura_min
    precipitacion = round(random.uniform(0,15),2)
    precipitacion_total += precipitacion
    dia = [dia_n,temperatura_max,temperatura_min,precipitacion]
    matriz.append(dia)
    




titulos = ["# Dia", "Max", "Min", "Precipitacion (MM)"]

print(titulos)
for dia in matriz:
      print(dia)

dias_promedios = int(input("Ingrese la cantidad de dias para calcular los promedios: "))

calcular_promedios(dias_promedios)
