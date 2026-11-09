import os
from produto import Produto


def demo_mongodb():
    """
    Demonstração de inserção/recuperação em MongoDB.
    Executa somente se a variável de ambiente MONGO_URI estiver definida
    e se `conexao.AtlasConnection` puder ser importado corretamente.
    """
    if not os.getenv("MONGO_URI"):
        print("MONGO_URI não encontrada — pulando demo MongoDB.")
        return

    try:
        from conexao import AtlasConnection
    except Exception as e:
        print("Não foi possível importar AtlasConnection:", e)
        return

    try:
        with AtlasConnection() as conn:
            db = conn.get_database("teste")
            colecao = db["produtos"]

            prod = Produto(None, "Biscoito", 4.5, 20, ["salgado"])
            res = colecao.insert_one(prod.to_dict())
            print("Inserido _id:", res.inserted_id)

            fetched = colecao.find_one({"_id": res.inserted_id})
            prod_from_db = Produto.from_dict(fetched)
            print("Lido do DB:", prod_from_db)

            colecao.delete_one({"_id": res.inserted_id})
            print("Removido o documento de demonstração.")
    except Exception as e:
        print("Erro durante demo MongoDB:", e)


if __name__ == "__main__":
    demo_mongodb()
