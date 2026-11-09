from database_escola import Session
from modelos_escola import Aluno

PAGINA_ATUAL = 3
TAMANHO_PAGINA = 10
OFFSET = (PAGINA_ATUAL - 1) * TAMANHO_PAGINA

with Session() as sessao:
    total = sessao.query(Aluno).count()
    print(f"Total de alunos matriculados: {total}")

    print("\nAlunos em ordem alfabética:")
    ordenados = sessao.query(Aluno).order_by(Aluno.nome.asc()).all()
    for aluno in ordenados:
        print(f"  {aluno.nome} (matrícula {aluno.matricula})")

    pagina = (
        sessao.query(Aluno)
        .order_by(Aluno.nome.asc())
        .offset(OFFSET)
        .limit(TAMANHO_PAGINA)
        .all()
    )
    print(f"\nPágina {PAGINA_ATUAL} (offset {OFFSET}, limite {TAMANHO_PAGINA}):")
    for aluno in pagina:
        print(f"  {aluno.nome} (matrícula {aluno.matricula})")
