import math
import heapq
from geopy.distance import distance

# Cálculo da função heurística
def distancia_entre_cidades(cidade1, cidade2):
    latitudes_longitudes = {
        'Vitória': (-20.3194, -40.3378),
        'Vila Velha': (-20.3297, -40.2922),
        'Cariacica': (-20.2635, -40.4165),
        'Serra': (-20.1211, -40.3074),
        'Guarapari': (-20.6693, -40.4973),
        'Linhares': (-19.3959, -40.0642),
        'Colatina': (-19.5396, -40.626),
        'Aracruz': (-19.819, -40.2768),
        'Cachoeiro de Itapemirim': (-20.8477, -41.1126),
        'Nova Venécia': (-18.7151, -40.4058),
        'São Mateus': (-18.7213, -39.8576),
        'Barra de São Francisco': (-18.7552, -40.8979),
        'Santa Teresa': (-19.9366, -40.5979),
        'Venda Nova do Imigrante': (-20.3264, -41.1356),
        'Santa Maria de Jetibá': (-20.025669892220293, -40.74327676550917),
        'Santa Leopoldina': (-20.10056796652768, -40.52775994730116)
    }
    coord1 = latitudes_longitudes[cidade1]
    coord2 = latitudes_longitudes[cidade2]
    return distance(coord1, coord2).km

def calcula_heuristica(destino):
    heuristica = {}
    for cidade in grafo:
        heuristica[cidade] = distancia_entre_cidades(cidade, destino)
    return heuristica

# Algoritmo A*
def a_estrela(cidade_inicial, destino, grafo):
    if destino not in grafo:
        raise ValueError(f"A cidade de destino '{destino}' não está no grafo.")
    
    fila_de_prioridade = [(0, cidade_inicial)]
    distancia = {cidade_inicial: 0}
    antecessor = {cidade_inicial: None}

    heuristica = calcula_heuristica(destino)

    while fila_de_prioridade:
        (dist, cidade_atual) = heapq.heappop(fila_de_prioridade)
        if cidade_atual == destino:
            break

        for (cidade_adjacente, peso) in grafo[cidade_atual]:
            dist_candidata = dist + peso
            if cidade_adjacente not in distancia or dist_candidata < distancia[cidade_adjacente]:
                distancia[cidade_adjacente] = dist_candidata
                prioridade = dist_candidata + heuristica[cidade_adjacente]
                heapq.heappush(fila_de_prioridade, (prioridade, cidade_adjacente))
                antecessor[cidade_adjacente] = cidade_atual

    # Cálculo da distância percorrida e da rota
    distancia_percorrida = distancia[destino]
    rota = [destino]
    cidade = destino
    while antecessor[cidade]:
        rota.append(antecessor[cidade])
        cidade = antecessor[cidade]
    rota.reverse()

    return distancia_percorrida, rota

# Definição do grafo
grafo = {
    'Vitória': [('Vila Velha', 10), ('Cariacica', 5), ('Serra', 12)],
    'Vila Velha': [('Vitória', 10), ('Cariacica', 8), ('Guarapari', 50), ('Santa Leopoldina', 36)],
    'Cariacica': [('Vitória', 5), ('Vila Velha', 8), ('Serra', 15)],
    'Serra': [('Vitória', 12), ('Cariacica', 15), ('Linhares', 140)],
    'Guarapari': [('Vila Velha', 50), ('Linhares', 30)],
    'Linhares': [('Serra', 140), ('Guarapari', 30), ('Colatina', 70)],
    'Colatina': [('Linhares', 70), ('Aracruz', 90), ('Cachoeiro de Itapemirim', 130)],
    'Aracruz': [('Colatina', 90), ('Nova Venécia', 80), ('Cachoeiro de Itapemirim', 167)],
    'Cachoeiro de Itapemirim': [('Colatina', 130), ('Nova Venécia', 200), ('São Mateus', 180), ('Venda Nova do Imigrante', 118), ('Aracruz', 167)],
    'Nova Venécia': [('Aracruz', 80), ('Cachoeiro de Itapemirim', 200)],
    'São Mateus': [('Cachoeiro de Itapemirim', 180), ('Barra de São Francisco', 75)],
    'Barra de São Francisco': [('São Mateus', 75), ('Santa Teresa', 50)],
    'Santa Teresa': [('Barra de São Francisco', 50), ('Venda Nova do Imigrante', 60), ('Santa Maria de Jetibá', 19), ('Santa Leopoldina', 20)],
    'Venda Nova do Imigrante': [('Santa Teresa', 60), ('Santa Maria de Jetibá', 35), ('Cachoeiro de Itapemirim', 118)],
    'Santa Maria de Jetibá': [('Venda Nova do Imigrante', 35), ('Santa Leopoldina', 40), ('Santa Teresa', 19)],
    'Santa Leopoldina': [('Santa Maria de Jetibá', 40), ('Vila Velha', 36), ('Santa Teresa', 20)]
}

# Entrada de dados do usuário
cidade_inicial = input("Digite a cidade inicial: ")
destino = input("Digite a cidade de destino: ")

# Aplicação do algoritmo A*
distancia_percorrida, rota = a_estrela(cidade_inicial, destino, grafo)

# Exibição dos resultados
print(f'Distância percorrida: {round(distancia_percorrida, 2)} Km')
print("Rota:", rota)
