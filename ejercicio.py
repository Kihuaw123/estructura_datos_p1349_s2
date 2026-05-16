import time
matriz = list(range(1,1_000_001))
tiempo_inicial = time.perf_counter()

num_buscado = 999

def busqueda_lineal(lista,valor):
     for i in range(len(lista)):
          if lista[i] == valor:
               return i
          return -1
     
def busqueda_binaria(lista,valor):
     izquierda = 0
     derecha = len(lista) -1

     while izquierda <= derecha:
          medio = (izquierda + derecha) // 2

          if lista[medio] == valor:
               return medio
          elif lista[medio] < valor:
               izquierda = medio + 1
          else:
               derecha = medio - 1
     return -1 
tiempo_final = time.perf_counter()
tiempo_total = tiempo_final - tiempo_inicial


print("Lineal:", busqueda_lineal(matriz, num_buscado))
print("Binaria:", busqueda_binaria(matriz, num_buscado))
print(f"Tiempo:{tiempo_total:.8f}")
