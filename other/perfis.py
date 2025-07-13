perfis = [

    {"Nome": "Alan", "sexo": "M", "cidade": "BH"},
    {"Nome": "Antonio", "sexo": "M", "cidade": "BH"},
    {"Nome": "Bruna", "sexo": "F", "cidade": "SP"},
    {"Nome": "Brena", "sexo": "F", "cidade": "RJ"},
    {"Nome": "Beto", "sexo": "M", "cidade": "BH"},
    {"Nome": "Leonardo", "sexo": "M", "cidade": "SP"},
    {"Nome": "Leandro", "sexo": "M", "cidade": "RJ"},
    {"Nome": "Lucia", "sexo": "F", "cidade": "SP"},
    {"Nome": "Ludimila", "sexo": "F", "cidade": "BH"},
    {"Nome": "Pedro", "sexo": "M", "cidade": "BH"},
]
for perfil in perfis:
    if perfil["cidade"] == "BH" and perfil["sexo"] == "F":
        print(f"Nome: {perfil['Nome']}")

