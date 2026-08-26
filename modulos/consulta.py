def buscar_musica_inteligente(df, coluna):
    cont = 0
    termo = str(input("Digite o nome da música que você procura: "))
    
    # Tenta a busca por trecho (Pandas)
    resultado = df[df[coluna].str.contains(termo, case=False, na=False)]
    resultado = resultado.drop_duplicates(subset=[coluna])

    i = 0
    if not resultado.empty:
        print(f"\nEncontramos {len(resultado)} resultado(s) direto(s):")
        for musica in resultado[coluna]:
            i += 1
            print("[{}] {}".format(i, musica))
        
    else:
        print("\nNenhuma música encontrada com esse termo exato.")
        from difflib import get_close_matches
        # 2. Se não achou nada, usa a aproximação (Difflib)
        lista_opcoes = df[coluna].drop_duplicates().dropna().astype(str).tolist()
        sugestoes = get_close_matches(termo, lista_opcoes, n=10, cutoff=0.4)
        
        if sugestoes:
            print("Você quis dizer alguma destas?\n")
            for i, opcao in enumerate(sugestoes, 1):
                print(f"[{i}] {opcao}")
        else:
            cont += 1
            print("Não encontramos nada nem parecido. Tente outro termo.")
    return cont
    

def procura_aproximacao(escolha, musicas_pivot, modelo):
    distances, sugestions = modelo.kneighbors(musicas_pivot.filter(items = [escolha], axis=0).values.reshape(1, -1))
    for i in range(len(sugestions)):
        print(musicas_pivot.index[sugestions[i]])
