import random


def generar_exoplanetas(N):
    matriz = []
    for i in range(1, N + 1):
        codigo = "EXPL " + str(i)
        masa = round(random.uniform(25, 50), 2)
        indices = []
        for i in range(5):
            indice = round(random.uniform(0, 10), 2)
            indices.append(indice)
        exoplaneta = [codigo, masa] + indices
        matriz.append(exoplaneta)
    return matriz

def calcular_promedios(matriz):
    promedios = []
    for j in range(2, 7):
        suma = sum(fila[j] for fila in matriz)
        promedio = round(suma / len(matriz), 2)
        promedios.append(promedio)
    matriz.append(["Promedios indices"] + promedios)
    return matriz

def calcular_ipevp(matriz):
    for i in range(len(matriz)):
        ipevp = round(sum(matriz[i][2:]) / len(matriz[i][2:]), 2)
        matriz[i] = matriz[i] + [ipevp]
    return matriz

def ordenar_promedios(promedios):
    for i in range(1, len(promedios)):
        j = i
        while j > 0 and promedios[j-1] < promedios[j]:  
            promedios[j-1], promedios[j] = promedios[j], promedios[j-1]
            j -= 1


def buscar_exoplaneta_por_codigo(matriz, codigo):
    for exoplaneta in matriz:
        if exoplaneta[0] == codigo:
            return exoplaneta
        
def ordenar_tres_mayores_ipevp(matriz_exoplanetas):
    tres_mayores = []
    tres_mayores = matriz_exoplanetas
    n = len(matriz_exoplanetas)
    for i in range(1, n):
        j = i
        while j > 0 and tres_mayores[j][-1] > tres_mayores[j - 1][-1]:
            tres_mayores[j], tres_mayores[j - 1] = tres_mayores[j - 1], tres_mayores[j]
            j -= 1
    return tres_mayores[:3]

N = int(input("Ingrese el numero de exoplanetas: "))
matriz_exoplanetas = generar_exoplanetas(N)

matriz_exoplanetas = calcular_ipevp(matriz_exoplanetas)

print("Los tres exoplanetas con el mayor IPEVP son:")

tres_mayores = matriz_exoplanetas

tres_mayores = ordenar_tres_mayores_ipevp(tres_mayores)

matriz_exoplanetas = calcular_promedios(matriz_exoplanetas)

for exoplaneta in tres_mayores:
    print(exoplaneta)

print("Matriz de Exoplanetas:")

for exoplaneta in matriz_exoplanetas:
    print(exoplaneta)

promedios = matriz_exoplanetas[-1][1:]

ordenar_promedios(promedios)

print("Promedios ordenados:", promedios)

codigo = input("Ingrese el codigo a buscar" "(Ejemplo: EXPL 4):")

exoplaneta_encontrado = buscar_exoplaneta_por_codigo(matriz_exoplanetas, codigo)

if exoplaneta_encontrado:
    print("Información de exoplaneta", codigo,":", exoplaneta_encontrado)
else:
    print("No se encontró el exoplaneta con código", codigo)