from conexao import AtlasConnection
db_name = 'produtos'


try:
    with AtlasConnection() as conexao:
        # 1. SOLICITANDO O BANCO DE DADOS
        # A classe retorna o objeto do banco de dados que queremos.
        db = conexao.get_database(db_name)
        collection = db['produtos']

        # --- Usando delete_one ---
        # Deletar o produto "Mouse sem Fio"
        resultado = collection.delete_one({"nome": "Mouse sem Fio"})
        print(f"\nDocumentos deletados com delete_one: {resultado.deleted_count}")

        # --- Usando delete_many ---
        # Deletar TODOS os produtos que estiverem em promoção
        # CUIDADO: Esta operação é destrutiva!
        # resultado = collection.delete_many({"em_promocao": True})
        # print(f"Documentos deletados com delete_many: {resultado.deleted_count}")
except (ValueError, ConnectionError) as e:
        # Captura erros de configuração ou conexão levantados pela nossa classe
        print(f"\nUm erro impediu a execução do programa: {e}")
except Exception as e:
    # Captura outros erros inesperados
    print(f"\nOcorreu um erro inesperado: {e}")