def filtrar_dataframes(musicas, reproducoes):
    # Filtrando somente as colunas necessárias
    # Seleciona somente as variaveis que iremos utilizar
    musicas = musicas[["track_id", "name", "artist", "year"]]
    musicas.rename (columns = {"track_id":"id_musica", "name":"nome_musica", "artist":"artista", "year":"ano"}, inplace = True)

    # Filtrando somente as colunas necessárias
    # Seleciona somente as variaveis que iremos utilizar
    reproducoes.rename(columns={"track_id":"id_musica", "user_id":"id_usuario", "playcount":"qtd_reproducoes"}, inplace=True)

    # Cria um filtro para utilizarmos apenas usuarios que escutaram mais de 80 músicas
    qt_reproducao = reproducoes['id_usuario'].value_counts() > 80
    y = qt_reproducao[qt_reproducao].index

    # Filtro para atualizar o dataframe apenas com o que satisfazem a condição
    reproducoes = reproducoes[reproducoes["id_usuario"].isin(y)]

    # Concatenando os dataframes
    reproducoes_e_musica = reproducoes.merge(musicas, on = "id_musica")

    # Apagar duplicados de mesmo usuário para a mesma música
    reproducoes_e_musica.drop_duplicates(["id_musica", "id_usuario"], inplace = True)

    # Apagar a variável id_filme pois não será utilizada
    del reproducoes_e_musica['id_musica']
    return reproducoes_e_musica


def criacao_pivot(reproducoes_e_musica):
    # Quero que cada id_usuario seja uma variavel com o respectivo valor de nota 
    # para cada filme avaliado
    musicas_pivot = reproducoes_e_musica.pivot_table(columns = "id_usuario", index = "nome_musica", values = "qtd_reproducoes")

    # Substitui os valores nulos por 0
    musicas_pivot.fillna(0, inplace = True)
    return musicas_pivot


def criacao_matrizsparsa(musicas_pivot):
    #importar csr_matriz do pacote SciPy
    #possibilita a criação de matrizes sparsas
    from scipy.sparse import csr_matrix

    #Transformar o dataset em uma matriz sparsa
    musicas_sparse = csr_matrix(musicas_pivot)
    return musicas_sparse