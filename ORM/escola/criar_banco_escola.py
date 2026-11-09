from sqlalchemy import create_engine
from sqlalchemy.schema import CreateIndex, CreateTable
from modelos_escola import Base

engine = create_engine("sqlite:///escola.db", echo=True)

Base.metadata.create_all(engine)

print("\n=== DDLs SQL Gerados ===\n")
for tabela in Base.metadata.sorted_tables:
    print(CreateTable(tabela).compile(engine))
    print()
    for indice in sorted(tabela.indexes, key=lambda item: item.name or ""):
        print(CreateIndex(indice).compile(engine))
        print()