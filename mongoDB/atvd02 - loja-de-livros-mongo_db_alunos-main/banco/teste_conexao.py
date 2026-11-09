import os
import sys
from pathlib import Path

from dotenv import load_dotenv
import pymongo

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

MONGO_URI = os.getenv('MONGO_URI')
if not MONGO_URI:
    print("Erro: MONGO_URI não encontrada no arquivo .env do projeto.")
    sys.exit(1)

client = None
try:
    client = pymongo.MongoClient(MONGO_URI)
    client.admin.command("ping")
    print("Conectado ao MongoDB Atlas com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB Atlas: {e}")
    sys.exit(1)
finally:
    if client is not None:
        client.close()
