from conexao_loja import engine
from modelos_loja import Base

Base.metadata.create_all(engine)
print("Banco de dados loja_virtual.db criado com sucesso!")