from sqlalchemy import select
from conexao_loja import Session
from modelos_loja import Produto

with Session() as sessao:
    produto = sessao.get(Produto, 1)
    if produto:
        print(f"Produto encontrado: {produto}")
    else:
        print("Produto não encontrado.")

    primeiro = sessao.query(Produto).first()
    if primeiro:
        print(f"\nPrimeiro produto cadastrado: {primeiro}")
    else:
        print("\nNenhum produto cadastrado.")

    resultado = sessao.execute(select(Produto))
    produtos = resultado.scalars().all()

    print("\nLista de produtos (via scalars):")
    for p in produtos:
        print(" ", p)