import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a URI do MongoDB a partir do .env
uri = os.getenv('MONGO_URI')

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Ping! Você se conectou com sucesso ao MongoDB!")
except Exception as e:
    print(f"Erro ao conectar: {e}")
