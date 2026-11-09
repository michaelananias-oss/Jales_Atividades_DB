from conexao_loja import Session
from modelos_loja import Produto

with Session() as sessao:
    print("Produtos em estoque (filter_by):")
    em_estoque = sessao.query(Produto).filter_by(em_estoque=True).all()
    for p in em_estoque:
        print(f"  {p.nome} - R$ {p.preco:.2f}")

    print("\nProdutos Gamer acima de R$ 100,00 (filter + ilike):")
    gamers = sessao.query(Produto).filter(
        Produto.preco > 100,
        Produto.nome.ilike('%Gamer%')
    ).all()
    for p in gamers:
        print(f"  {p.nome} - R$ {p.preco:.2f}")