import pandas as pd

def importar_arquivos():
    # Importar os arquivos com as músicas e ver as primeiras linhas
    musicas = pd.read_csv("dadosspotify/Music Info.csv", low_memory=False)

    # Importar o arquivo de quantidade de reproduções por usuário e ver as primeiras linhas
    reproducoes = pd.read_csv("dadosspotify/User Listening History.csv", low_memory=False)
    return musicas, reproducoes