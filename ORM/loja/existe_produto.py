from sqlalchemy import exists
from conexao_loja import Session
from modelos_loja import Produto

def categoria_tem_produtos(sessao, categoria_id: int) -> bool:
    return bool(
        sessao.query(exists().where(Produto.categoria_id == categoria_id)).scalar()
    )

with Session() as sessao:
    for categoria_id in [1, 2, 3, 99]:
        tem = categoria_tem_produtos(sessao, categoria_id)
        if tem:
            print(f"Categoria {categoria_id}: POSSUI produtos associados.")
        else:
            print(f"Categoria {categoria_id}: NÃO possui produtos associados.")