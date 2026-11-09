from conexao_loja import Session
from modelos_loja import Produto, Categoria

with Session() as sessao:
    # 1) INNER JOIN: nome do produto + nome da categoria
    print("Inner Join - Produto x Categoria:")
    resultado = (
        sessao.query(Produto.nome, Categoria.nome)
        .join(Categoria, Produto.categoria_id == Categoria.id)
        .all()
    )
    for nome_produto, nome_categoria in resultado:
        print(f"  {nome_produto} → {nome_categoria}")

    # 2) LEFT ANTI-JOIN: categorias sem produtos (órfãs)
    print("\nLeft Anti-Join - Categorias sem produtos:")
    orfas = (
        sessao.query(Categoria)
        .outerjoin(Produto, Categoria.id == Produto.categoria_id)
        .filter(Produto.id.is_(None))
        .all()
    )
    if orfas:
        for c in orfas:
            print(f"  {c.nome} (id={c.id})")
    else:
        print("  Nenhuma categoria órfã encontrada.")