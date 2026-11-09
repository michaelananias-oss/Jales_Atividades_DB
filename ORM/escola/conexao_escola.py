from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:")

with engine.connect() as conexao:
    resultado = conexao.execute(text("SELECT sqlite_version()")).scalar()
    print(f"Versão do SQLite: {resultado}")