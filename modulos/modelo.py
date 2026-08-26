def modelo_knn(musicas_sparse):
    #Importar o algoritmo KNN que calcula com base na distância
    #do pacote SciKit Learn
    from sklearn.neighbors import NearestNeighbors

    #Criando e treinando modelo preditivo
    modelo = NearestNeighbors(algorithm="brute")
    modelo.fit(musicas_sparse)
    return modelo