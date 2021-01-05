#distâncias entre as cidades
distancias = [
   [0, 29, 20, 21, 16, 31, 100, 12, 4, 31, 18],
   [29, 0, 15, 29, 28, 40, 72, 21, 29, 41, 12],
   [20, 15, 0, 15, 14, 25, 81, 9, 23, 27, 13],
   [21, 29, 15, 0, 4, 12, 92, 12, 25, 13, 25],
   [16, 28, 14, 4, 0, 16, 94, 9, 20, 16, 22],
   [31, 40, 25, 12, 16, 0, 95, 24, 36, 3, 37],
   [100, 72, 81, 92, 94, 95, 0, 90, 101, 99, 84],
   [12, 21, 9, 12, 9, 24, 90, 0, 15, 25, 13],
   [4, 29, 23, 25, 20, 36, 101, 15, 0, 35, 18],
   [31, 41, 27, 13, 16, 3, 99, 25, 35, 0, 38],
   [18, 12, 13, 25, 22, 37, 84, 13, 18, 38, 0]
 ]

def insercao(ciclo):
    novo_vertice = 0
    maior_dist = 0
    
    #Percorre o grafo e encontra a maior distância
    for i in range(len(distancias)):
        for j in range(len(distancias)):
            
            if i in ciclo and j not in ciclo:
                if distancias[i][j] > maior_dist:
                    novo_vertice = j 
                maior_dist = max(distancias[i][j], maior_dist)               
                           
    #Encontra a aresta (Vx, Vy) do ciclo tal que (Cxk + Cky - Cxy) seja minimo
    dists = {}
    for aux in range(len(ciclo)): 
        if aux < len(ciclo) - 1:
            dists.update({aux: distancias[ciclo[aux]][novo_vertice] + distancias[novo_vertice][ciclo[aux + 1]] 
            - distancias[ciclo[aux]][ciclo[aux + 1]]})
        else:
            dists.update({aux: distancias[ciclo[-1]][novo_vertice] + distancias[novo_vertice][ciclo[0]] - 
            distancias[ciclo[-1]][ciclo[0]] })

    #Insere nova aresta no ciclo
    insere = sorted(dists, key = dists.get)  
    ciclo.insert(insere[0] + 1, novo_vertice)

    #Verfica se existe mais arestar para serem inseridas no ciclo
    print(ciclo)
    if len(ciclo) < (len(distancias)):
         insercao(ciclo)
    return ciclo    

insercao([0,1,2])

