from conexao import AtlasConnection
db_name = 'produtos'


try:
    with AtlasConnection() as conexao:
        # 1. SOLICITANDO O BANCO DE DADOS
        # A classe retorna o objeto do banco de dados que queremos.
        db = conexao.get_database(db_name)
        collection = db['produtos']

        # --- Usando update_one ---
        # Aumentar o preço do Teclado Mecânico em 10%
        filtro_one = {"nome": "Teclado Mecânico"}
        # $inc incrementa o valor do campo. $mul multiplicaria.
        atualizacao_one = {"$inc": {"preco": 35.00}}
        resultado = collection.update_one(filtro_one, atualizacao_one)
        print(f"\nDocumentos modificados com update_one: {resultado.modified_count}")

        # --- Usando update_many ---
        # Adicionar um campo "em_promocao: true" para todos os produtos da marca "VisionMax"
        filtro_many = {"marca": "VisionMax"}
        atualizacao_many = {"$set": {"em_promocao": True}}
        resultado = collection.update_many(filtro_many, atualizacao_many)
        print(f"Documentos modificados com update_many: {resultado.modified_count}")
except (ValueError, ConnectionError) as e:
        # Captura erros de configuração ou conexão levantados pela nossa classe
        print(f"\nUm erro impediu a execução do programa: {e}")
except Exception as e:
    # Captura outros erros inesperados
    print(f"\nOcorreu um erro inesperado: {e}")