import random
import math
from matplotlib import pyplot
import time


def mutacao(rota):
    n1 = random.randint(0,len(rota)-1)
    n2 = random.randint(0,len(rota)-1)
    #muta1 = objeto.rota[n1]
    #muta2 = objeto.rota[n2]
    rota[n1], rota[n2] = rota[n2], rota[n1]
    return rota
    

def cruzamento(objeto1,objeto2):
    planta = random.randint(1,len(objeto1.rota)-1)
    #planta = 3
    rotinha1 = objeto1.rota[:planta]
    rotinha2 = objeto2.rota[:]
    pos1 = -1
    for elemental in rotinha1:
        pos1 += 1
        pos2 = 0
        for ele in rotinha2:
            if elemental == ele:
                rot1 = rotinha2[pos1]
                rot2 = rotinha2[pos2]
                rotinha2[pos1] = rot2
                rotinha2[pos2] = rot1
                break
            else:
                pos2 += 1
    return roteiro(rotinha2)
    #lembrar de chamar duas vezes, (objeto1, objeto2) - (objeto2, objeto1) para ter 2 filhos

def calc_aptidao(dist_normalizada):
    a = math.cos(dist_normalizada*(math.pi/2))
    return a

def distancia_normalizada(dist,menor_dist,maior_dist):
    try:
        a = (dist-menor_dist)/(maior_dist-menor_dist)
    except ZeroDivisionError:
        a = (dist-menor_dist)/0.00000000001
    return a

def calc_distancia(rota):
    distancia = 0
    a = 0
    for ponto in rota:
        if a+2 > len(rota):
            v = (ponto[1][0] - rota[0][1][0])**2 + (ponto[1][1] - rota[0][1][1])**2
            distancia += math.sqrt(v)
            break
        v = (ponto[1][0] - rota[a+1][1][0])**2 + (ponto[1][1] - rota[a+1][1][1])**2

        distancia += math.sqrt(v)
        a += 1
    return distancia


def torneio(lista_pop):
    maior_aptidao = 0
    vencedor = 0
    lista_torneio = []
    for i in range(10):
        n1 = random.randint(0,len(lista_pop)-1)
        if lista_pop[n1].aptidao > maior_aptidao:
            maior_aptidao = lista_pop[n1].aptidao
            vencedor = lista_pop[n1]
    return vencedor
        
            
class roteiro:
    def __init__(self,rota):
        self.rota = rota
        self.distancia = calc_distancia(self.rota)
        self.aptidao = 0

points = [[0,1,0,3],[0,0,2,0],[0,4,0,0],[0,5,0,0],[0,11,0,10],[0,0,9,0],[0,8,0,0],[0,6,0,7]]
lista_pos = []
inicio = time.process_time()
#Recebe por entrada um valor m que representa a quantidade de pontos da entrada
m = input()
e = 0
while e < int(m):
  e += 1
#Recebe por entrada o ponto de entrega e suas respectivas posições nos eixos x e y do plano cartesiano.
  a, b, c = input().split()
  l = [int(a),(float(b),float(c))]
  lista_pos.append(l)


#lista_pos = []
#print(lista_pos)
'''
m = -1
for lista in l:
  m += 1
  n = -1
  for elemento in lista:
    n += 1
    if elemento > 0:
      lista_pos.append([elemento, (n,m)])

'''
#
#print(lista_pos)
lista_pop = [roteiro(lista_pos)]

#gera população e a quantidade de individuos é definida aqui
individuos = 100
for i in range(generations):
    for e in range(int(len(lista_pos)/2)):
        l = mutacao(lista_pos)
    lista_pop.append(roteiro(l[:]))
    
#gerações
    gg = 0
#O número de gerações a serem rodadas é informado no range.
for i in range(1000):
    somatorio = 0
    menor_dist = 1000000000000
    maior_dist = 0
    lista_filhos =[]
    gg += 1
    #Geração de plot gradual aqui. Cada novo or seguido de certa posição gg no número de gerações é um novo plot do melhor individuo atual.
    if gg == 100 or gg == 500:
        menor_distancia = 10000000000
        melhor_rota = []
        for objeto in lista_pop:
            if objeto.distancia < menor_distancia:
                menor_distancia = float(objeto.distancia)
                melhor_rota = objeto.rota[:]

        mapax = []
        mapay = []
        for ponto, pos in melhor_rota:
            mapax.append(pos[0])
            mapay.append(pos[1])
            pyplot.annotate(ponto,(pos[0],pos[1]))
        mapax.append(mapax[0])
        mapay.append(mapay[0])
        pyplot.plot(mapax,mapay)
        fim = time.process_time()
        print(fim-inicio)
        print(menor_distancia)
        pyplot.show()
        
    for objeto in lista_pop:
        #print(objeto)
    #print(objeto.rota, objeto.distancia)
        if menor_dist > objeto.distancia:
            menor_dist = float(objeto.distancia)
        if maior_dist < objeto.distancia:
            maior_dist = float(objeto.distancia)
    menor_distancia = 10000000000
    melhor_rota = []        
    for objeto in lista_pop:
        if objeto.distancia < menor_distancia:
            menor_distancia = float(objeto.distancia)
            melhor_rota = objeto.rota[:]
        dist = objeto.distancia
        dist_norm = distancia_normalizada(dist, menor_dist, maior_dist)
        objeto.aptidao = calc_aptidao(dist_norm)
        #print(objeto.aptidao)
        somatorio += objeto.aptidao
    #Geração de nova população
    for e in range(int(individuos/2)):
        pai1 = torneio(lista_pop)
        pai2 = torneio(lista_pop)
        na = random.randint(0,99)
        if na < 80:
            #cruzamento
            lista_filhos.append(cruzamento(pai1,pai2))
            lista_filhos.append(cruzamento(pai2,pai1))

        else:
            lista_filhos.append(pai1)
            lista_filhos.append(pai2)

        
    lista_pop = lista_filhos[:]
    lista_pop.append(roteiro(melhor_rota[:]))
    
    for mutacoes in range(1):
        lista_pop[na].rota = mutacao(lista_pop[na].rota)

    #print(somatorio)
menor_distancia = 10000000000
melhor_rota = []
for objeto in lista_pop:
    if objeto.distancia < menor_distancia:
        menor_distancia = float(objeto.distancia)
        melhor_rota = objeto.rota[:]
        
fim = time.process_time()
mapax = []
mapay = []
tempo_decorrido = fim - inicio
for ponto, pos in melhor_rota:
    print(ponto)
    mapax.append(pos[0])
    mapay.append(pos[1])
    pyplot.annotate(ponto,(pos[0],pos[1]))
mapax.append(mapax[0])
mapay.append(mapay[0])
pyplot.plot(mapax,mapay)
print(tempo_decorrido)
print(menor_distancia)
pyplot.show()


