import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Importa a biblioteca do PyMongo
import pymongo

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a URI do MongoDB a partir do .env
uri = os.getenv('MONGO_URI')

# Crie um novo cliente e conecte ao servidor
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

# Envia um ping para confirmar uma conexão bem-sucedida
try:
    client.admin.command('ping')
    print("Ping no seu cluster realizado com sucesso! Você está conectado ao MongoDB Atlas.")
except Exception as e:
    print(e)
    exit() # Encerra o script se a conexão falhar

# --- A partir daqui, podemos executar operações CRUD ---

# 1. Definindo o banco de dados e a coleção
db = client['loja_online']
collection = db['produtos']

# 2. CREATE: Inserindo um documento
novo_produto = {
    "nome": "Notebook Gamer",
    "preco": 7500.00,
    "estoque": 15,
    "tags": ["informatica", "gamer", "notebook"]
}
result = collection.insert_one(novo_produto)
print(f"Produto inserido com o ID: {result.inserted_id}")

# 3. READ: Buscando um documento
produto_encontrado = collection.find_one({"nome": "Notebook Gamer"})
print(f"Produto encontrado: {produto_encontrado}")

# 4. UPDATE: Atualizando um documento
query = {"_id": result.inserted_id}
nova_info = {"$set": {"preco": 7299.90, "estoque": 14}}
collection.update_one(query, nova_info)
print("Produto atualizado.")

# 5. DELETE: Deletando o documento
# collection.delete_one({"_id": result.inserted_id})
# print("Produto deletado.")


# É importante fechar a conexão
client.close()