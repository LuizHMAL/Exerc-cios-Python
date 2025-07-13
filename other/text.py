def Verifica(palavras, texto):
    return palavras in texto



text = "O que é cultura? A resposta envolve uma definição complexa. Trata -se do  deconhecimentos, ideias, costumes e práticas que se tornam características de um grupo."

palavra = "conjunto"

if Verifica(palavra, text):
    print(f"Encontrou")

