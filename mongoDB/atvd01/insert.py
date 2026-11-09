from conexao import AtlasConnection
db_name = 'produtos'


try:
    with AtlasConnection() as conexao:
        # 1. SOLICITANDO O BANCO DE DADOS
        # A classe retorna o objeto do banco de dados que queremos.
        db = conexao.get_database(db_name)
        collection = db['produtos']

        # --- Usando insert_one ---
        produto_unico = {"nome": "Mouse sem Fio", "preco": 120.50, "qtd": 200, "marca": "Genérica"}
        resultado_one = collection.insert_one(produto_unico)
        print(f"Documento único inserido com o ID: {resultado_one.inserted_id}")

        # --- Usando insert_many ---
        lista_produtos = [
            {"nome": "Teclado Mecânico", "preco": 350.00, "qtd": 50, "marca": "TechForce"},
            {"nome": "Monitor 24 polegadas", "preco": 999.90, "qtd": 30, "marca": "VisionMax"},
            {"nome": "Webcam Full HD", "preco": 250.00, "qtd": 75, "marca": "VisionMax"}
        ]
        resultado_many = collection.insert_many(lista_produtos)
        print(f"IDs dos documentos inseridos: {resultado_many.inserted_ids}")
except (ValueError, ConnectionError) as e:
        # Captura erros de configuração ou conexão levantados pela nossa classe
        print(f"\nUm erro impediu a execução do programa: {e}")
except Exception as e:
    # Captura outros erros inesperados
    print(f"\nOcorreu um erro inesperado: {e}")