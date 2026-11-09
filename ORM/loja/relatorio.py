from sqlalchemy import func
from conexao_loja import Session
from modelos_loja import Produto, Categoria

with Session() as sessao:
    print("Relatório gerencial por categoria:")
    print(f"{'Categoria':<15} {'Preço médio':>15} {'Qtd produtos':>15}")

    relatorio = (
        sessao.query(
            Categoria.nome,
            func.avg(Produto.preco).label('preco_medio'),
            func.count(Produto.id).label('qtd_produtos'),
        )
        .join(Produto, Produto.categoria_id == Categoria.id)
        .group_by(Categoria.id)
        .having(func.avg(Produto.preco) > 250)
        .all()
    )

    for nome, preco_medio, qtd in relatorio:
        print(f"{nome:<15} R$ {preco_medio:>10.2f} {qtd:>15}")