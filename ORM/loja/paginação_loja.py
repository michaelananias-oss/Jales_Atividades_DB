from conexao_loja import Session
from modelos_loja import Produto, Categoria

TAMANHO_PAGINA = 5
PAGINA_ATUAL = 2

with Session() as sessao:
    total = sessao.query(Produto).count()
    print(f"Total de produtos cadastrados: {total}")

    categorias_distintas = sessao.query(Categoria.nome) \
        .join(Produto, Produto.categoria_id == Categoria.id) \
        .distinct().all()
    print("\nCategorias distintas presentes nos produtos:")
    for (nome,) in categorias_distintas:
        print(" ", nome)

    offset = (PAGINA_ATUAL - 1) * TAMANHO_PAGINA
    pagina = (
        sessao.query(Produto)
        .order_by(Produto.preco.desc())
        .limit(TAMANHO_PAGINA)
        .offset(offset)
        .all()
    )

    print(f"\nPágina {PAGINA_ATUAL} (tamanho {TAMANHO_PAGINA}):")
    for p in pagina:
        print(f"  {p.nome} - R$ {p.preco:.2f}")