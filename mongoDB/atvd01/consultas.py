from conexao import AtlasConnection
from bson.decimal128 import Decimal128
from datetime import datetime, timedelta

def setup_dados_iniciais(db):
    """Insere alguns dados de exemplo para podermos consultar."""
    print("\nLimpando coleção e inserindo dados de teste...")
    collection = db['eletronicos']
    collection.delete_many({}) # Limpa a coleção para garantir um estado inicial limpo
    
    dados = [
        {"item": "Notebook Gamer", "marca": "TechForce", "preco": Decimal128("7500.99"), "qtd": 15, "tags": ["notebook", "gamer", "alto_desempenho"], "data_cadastro": datetime.now() - timedelta(days=10)},
        {"item": "Monitor 24p", "marca": "VisionMax", "preco": Decimal128("999.90"), "qtd": 30, "tags": ["monitor", "full_hd"], "data_cadastro": datetime.now() - timedelta(days=30)},
        {"item": "Webcam Full HD", "marca": "VisionMax", "preco": Decimal128("250.00"), "qtd": 75, "tags": ["periferico", "video"], "desconto_pct": 10, "data_cadastro": datetime.now() - timedelta(days=5)},
        {"item": "Mouse sem Fio", "marca": "Genérica", "preco": Decimal128("120.50"), "qtd": 5, "tags": ["periferico"], "data_cadastro": datetime.now() - timedelta(days=90)},
        {"item": "Teclado Mecânico", "marca": "TechForce", "preco": Decimal128("350.00"), "qtd": 50, "tags": ["periferico", "gamer"], "data_cadastro": datetime.now() - timedelta(days=2)},
    ]
    collection.insert_many(dados)
    print("Dados inseridos.")

def executar_consultas(db):
    """Executa e imprime os resultados de várias consultas de exemplo."""
    collection = db['eletronicos']

    print("\n--- CONSULTA 1: Produtos da marca 'TechForce' ---")
    for doc in collection.find({"marca": "TechForce"}):
        print(f"  -> {doc['item']} (Preço: {doc['preco']})")

    print("\n--- CONSULTA 2: Produtos com preço MAIOR QUE 400 ---")
    for doc in collection.find({"preco": {"$gt": Decimal128("400")}}):
        print(f"  -> {doc['item']} (Preço: {doc['preco']})")
        
    print("\n--- CONSULTA 3: Produtos com estoque baixo (<= 15) OU da marca 'VisionMax' (OR) ---")
    filtro_or = {
        "$or": [
            {"qtd": {"$lte": 15}},
            {"marca": "VisionMax"}
        ]
    }
    for doc in collection.find(filtro_or):
        print(f"  -> {doc['item']} (Marca: {doc['marca']}, Qtd: {doc['qtd']})")

    print("\n--- CONSULTA 4: Produtos que são 'gamer' E da marca 'TechForce' (AND) ---")
    filtro_and = {
        "tags": "gamer",
        "marca": "TechForce"
    }
    for doc in collection.find(filtro_and):
        print(f"  -> {doc['item']}")

    print("\n--- CONSULTA 5: Produtos que POSSUEM campo de desconto ---")
    for doc in collection.find({"desconto_pct": {"$exists": True}}):
        print(f"  -> {doc['item']} (Desconto de {doc['desconto_pct']}%)")


def main():
    """Função principal."""
    db_name = "loja_avancada"
    try:
        with AtlasConnection() as conn:
            db = conn.get_database(db_name)
            setup_dados_iniciais(db)
            executar_consultas(db)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
