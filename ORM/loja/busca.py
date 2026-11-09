from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos_loja import Base, Produto

engine = create_engine('sqlite:///loja_virtual.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

with Session() as sessao:

    print("Produtos em estoque:")
    em_estoque = sessao.query(Produto).filter_by(em_estoque=True).all()
    for p in em_estoque:
        print(f"  {p.nome} - R$ {p.preco:.2f}")

    print("\nProdutos Gamer acima de R$ 100,00:")
    gamers = sessao.query(Produto).filter(
        Produto.preco > 100,
        Produto.nome.ilike('%Gamer%')
    ).all()
    for p in gamers:
        print(f"  {p.nome} - R$ {p.preco:.2f}")