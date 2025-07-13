realeza = [
    {"id": 1, "nome": "Rainha Elizabeth II", "conjuge": None, "pai": None, "mae": None},
    {"id": 2, "nome": "Príncipe Philip", "conjuge": 1, "pai": None, "mae": None},
    {"id": 3, "nome": "Príncipe Charles", "conjuge": None, "pai": 2, "mae": 1},
    {"id": 4, "nome": "Princesa Diana", "conjuge": None, "pai": None, "mae": None},
    {"id": 5, "nome": "Príncipe William", "conjuge": None, "pai": 3, "mae": 4},
    {"id": 6, "nome": "Kate Middleton", "conjuge": 4, "pai": None, "mae": None},
    {"id": 7, "nome": "Príncipe Harry", "conjuge": None, "pai": 3, "mae": 4},
    {"id": 8, "nome": "Meghan Markle", "conjuge": 7, "pai": None, "mae": None},
    {"id": 9, "nome": "Camila Rosamaria Shand", "conjuge": 3, "pai": None, "mae": None},
    {"id": 10, "nome": "Príncipe George de Cambridge", "conjuge": None, "pai": 5, "mae": 6},
    {"id": 11, "nome": "Princesa Charlotte de Cambridge", "conjuge": None, "pai": 5, "mae": 6},
    {"id": 12, "nome": "Príncipe Louis de Cambridge", "conjuge": None, "pai": 5, "mae": 6},
    {"id": 13, "nome": "Archie Harrison", "conjuge": None, "pai": 7, "mae": 8},
]


qtd = 0
for pessoa in realeza:
    if pessoa.get("conjuge") is not None:
        qtd += 1
    else:
        pessoa["conjuje"] = -1
        print(f"Não casados: {pessoa["nome"]}")
print(f"Qtd: {qtd}")

for pessoa in realeza:
    if pessoa.get("pai") is not None:
        pessoa["pai"] = pessoa["pai"] * 10
        print(f"Pessoa Pai: {pessoa["pai"]}")
    
    if pessoa.get("mae") is not None and pessoa["mae"] >=4:
        pessoa["mae"] += 1
        print(f"Pessoa Mae: {pessoa["mae"]}")
