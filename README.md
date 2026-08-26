# SpotifyOn-Sistema_de_Recomendacao
Um sistema de recomendação utilizando o modelo de previsão KNN.  
As informações dos .csvs foram provenientes de um arquivo do kaggle de link:
https://www.kaggle.com/datasets/undefinenull/million-song-dataset-spotify-lastfm/data onde é utilizado apenas os dois arquivos .csv  
A ideia geral é o usuário digitar uma música e o sistema vai dizer se existe uma correspondência e por fim aparecerá músicas recomendadas com base na confirmação da música digitada pelo usuário.  
Para utilizar o sistema: python3 main.py
# Estrutura do Projeto
O repositório está organizado da seguinte forma:  
SpotifyOn/
│
├── dadosspotify/        # Pasta local de dados (não inclusa no GitHub)  
├── modulos/             # Módulos principais do sistema  
│   ├── arquivo.py  
│   ├── consulta.py  
│   ├── filtros.py  
│   └── modelo.py  
│
├── .gitignore           # Arquivos ignorados pelo Git  
├── main.py              # Script principal para execução  
├── main.ipynb           # Notebook de testes/exploração  
├── requirements.txt     # Dependências e bibliotecas do projeto  
└── README.md            # Manual do projeto  
