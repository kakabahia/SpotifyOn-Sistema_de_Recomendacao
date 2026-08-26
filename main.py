#importando os pacotes a serem utilizados
from modulos.arquivo import importar_arquivos
import modulos.filtros as filtros
from modulos.modelo import modelo_knn
import modulos.consulta as consulta


def menu_titulo():
    print("="*40)
    x = "RECOMENDAÇÃO SPOTIFY"
    print("{:^40}".format(x))
    print("="*40)


def menu(reproducoes_e_musica, musicas_pivot, modelo):
    #Vamos fazer um menu com previsões e sugestões de músicas com base na escolha do usuário
    escolha = 1
    while(escolha == 1):
        escolha = consulta.buscar_musica_inteligente(reproducoes_e_musica, "nome_musica")
        if(escolha == 1):
            escolha = int(input("Para digitar outro termo (1), para parar de digitar (0) "))
            if(escolha == 0):
                break
            else:
                continue
        choice = int(input("""Digite (1) para caso tenha encontrado a música que deseja; 
        (2) caso não e queira procurar novamente;
        (3) caso não queira mais procurar. """))
        if(choice == 1):
            escolha = str(input("Digite a música desejada exatamente igual ao menu apresentado acima: "))
            for musica in reproducoes_e_musica["nome_musica"]:
                if(escolha == musica):
                    consulta.procura_aproximacao(escolha, musicas_pivot, modelo)
                    escolha = int(input("Para procurar outra música (1), para parar de procurar (0) "))
                    break
            else:
                print("Digitação incorreta.")
                escolha = 1
        elif(choice == 2):
            escolha = 1
        elif(choice == 3):
            escolha = 0



musicas, reproducoes = importar_arquivos()
reproducoes_e_musicas = filtros.filtrar_dataframes(musicas, reproducoes)
musicas_pivot = filtros.criacao_pivot(reproducoes_e_musicas)
musicas_sparse = filtros.criacao_matrizsparsa(musicas_pivot)
modelo = modelo_knn(musicas_sparse)
menu_titulo()
menu(reproducoes_e_musicas, musicas_pivot, modelo)
