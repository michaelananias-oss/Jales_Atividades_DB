import os
import pymongo
from dotenv import load_dotenv
from pymongo.server_api import ServerApi

class AtlasConnection:
    """
    Uma classe para gerenciar a conexão com o MongoDB Atlas de forma segura e eficiente.
    
    Esta classe usa um gerenciador de contexto (with ... as ...) para garantir
    que a conexão seja aberta e fechada corretamente.
    """
    
    def __init__(self):
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()
        
        # Busca a URI do arquivo .env. Se não encontrar, lança um erro.
        self.uri = os.getenv("MONGO_URI")
        if not self.uri:
            raise ValueError("A variável de ambiente MONGO_URI não foi encontrada.")
            
        self.client = None

    def __enter__(self):
        """
        Método chamado ao entrar no bloco 'with'.
        Estabelece a conexão com o banco de dados.
        """
        try:
            self.client = pymongo.MongoClient(self.uri, server_api=ServerApi('1'))
            # O comando 'ping' força a conexão e verifica se o servidor está acessível.
            self.client.admin.command('ping')
            print("✅ Conexão com o MongoDB Atlas estabelecida com sucesso.")
            return self
        except pymongo.errors.ConfigurationError as e:
            print(f"❌ Erro de configuração: Verifique sua Connection String. Detalhes: {e}")
            raise
        except pymongo.errors.ConnectionFailure as e:
            print(f"❌ Falha na conexão com o Atlas. Verifique sua rede ou as configurações de IP. Detalhes: {e}")
            raise

    def get_database(self, db_name: str):
        """
        Retorna um objeto de banco de dados a partir do cliente conectado.

        :param db_name: O nome do banco de dados que você quer acessar.
        :return: Um objeto de banco de dados do PyMongo.
        """
        if self.client:
            return self.client[db_name]
        else:
            raise ConnectionError("O cliente não está conectado. Use dentro de um bloco 'with'.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método chamado ao sair do bloco 'with'.
        Fecha a conexão com o banco de dados.
        """
        if self.client:
            self.client.close()
            print("🔌 Conexão com o MongoDB Atlas fechada.")