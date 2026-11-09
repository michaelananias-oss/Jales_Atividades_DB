from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///loja_virtual.db", echo=True)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    with engine.connect() as conexao:
        resultado = conexao.execute(
            text("SELECT 'Sistema de Loja Virtual Conectado com Sucesso!'")
        )
        print(resultado.scalar())