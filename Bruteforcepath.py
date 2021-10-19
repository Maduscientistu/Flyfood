from itertools import permutations
import time
from matplotlib import pyplot

inicio = time.process_time()
def permutar(S,D):
  novoD = []
  novoS = []
  if 0 == D:
      
      print(novoS)
  for element in D:
      novoS.append(element)
      novoD.append(element)
      print(novoD)
      permutar(novoS,novoD)

def permutac(lst):
  l = []
  if len(lst) == 0:
    return []
  if len(lst) == 1:
    return [lst]
  for a in range(len(lst)):
    tmp = lst[a]
    remain = lst[:a] + lst[a+1:]
    for ele in permutac(remain):
      l.append([tmp] + ele)
  return l



points = [[0,"R",0,"B"],[0,0,"A",0],[0,"C",0,0]]
l = []

n, m = input().split()
e = 0
while e < int(m):
  e += 1
  l.append(input().split())
lista_pos = []

alfabeto =["A","B","C","D","E","F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n = -1
m = -1
for lista in l:
  m += 1
  n = -1
  for elemento in lista:
    n += 1
    if elemento in alfabeto:
      lista_pos.append([elemento, (n,m)])
# l = list(permutations(lista_pos))
perm = permutac(lista_pos)
caminho = []
distancia = 10000
for permutacao in perm:
  #print(permutacao)
  e = 0
  distanciatmp = 0
  for letra, local in permutacao:
    e += 1
    if e == len(permutacao):
      break
    distanciatmp += abs(permutacao[e][1][0] - local[0]) + abs(permutacao[e][1][1] - local[1])
  e = e-1
  distanciatmp += abs(permutacao[0][1][0] - permutacao[e][1][0]) + abs(permutacao[0][1][1] - permutacao[e][1][1])

  if distancia > distanciatmp:
    caminho = permutacao
    distancia = distanciatmp
#print(caminho)
mapax = []
mapay = []
fim = time.process_time()
for letra, pos in caminho:
  print(letra)
  mapax.append(pos[0])
  mapay.append(pos[1])
  pyplot.annotate(letra,(pos[0],pos[1]))
mapax.append(mapax[0])
mapay.append(mapay[0])
pyplot.plot(mapax,mapay)

tempo_decorrido = fim - inicio
print(tempo_decorrido)
pyplot.show()
