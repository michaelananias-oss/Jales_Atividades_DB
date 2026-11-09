from conexao_loja import Session
from modelos_loja import Produto

with Session() as sessao:
    consulta = (
        sessao.query(Produto)
        .filter_by(em_estoque=True)
        .add_columns((Produto.preco * 0.85).label("preco_promocional"))
    )
    resultados = consulta.all()

print("Produtos em estoque com desconto de Black Friday (15%):")
if not resultados:
    print("  Nenhum produto em estoque.")
for produto, preco_promocional in resultados:
    print(
        f"  {produto.nome}: original R$ {produto.preco:.2f}; "
        f"promocional R$ {preco_promocional:.2f}"
    )
