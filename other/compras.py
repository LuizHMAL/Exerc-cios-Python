compras = [
    {"id": "01", "nome": "Fabricio", "data": "20/02/2021"},
    {"id": "02", "nome": "Virgilio", "data": "01/04/2022"},
    {"id": "03", "nome": "Sergio", "data": "05/03/2021"},
    {"id": "04", "nome": "Thales", "data": "05/03/2022"},
    {"id": "05", "nome": "Dirceu", "data": "28/04/2022"},
]

for compra in compras:
    if compra["data"].endswith("2022"):
        print(f"{compra["id"]} {compra["data"]} {compra["nome"]}")