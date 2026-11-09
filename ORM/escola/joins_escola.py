from sqlalchemy import or_

from database_escola import Session
from modelos_escola import Aluno, Turma

with Session() as sessao:
    print("Alunos e suas turmas (LEFT JOIN):")
    alunos_turmas = (
        sessao.query(Aluno, Turma.nome_turma)
        .outerjoin(Turma, Aluno.turma_id == Turma.id)
        .all()
    )
    if not alunos_turmas:
        print("  Nenhum aluno cadastrado.")
    for aluno, nome_turma in alunos_turmas:
        print(f"  {aluno.nome} - {nome_turma or 'Sem turma'}")

    print("\nAlunos sem turma vinculada ou sem turma correspondente:")
    sem_turma = (
        sessao.query(Aluno)
        .outerjoin(Turma, Aluno.turma_id == Turma.id)
        .filter(or_(Aluno.turma_id.is_(None), Turma.id.is_(None)))
        .all()
    )
    if not sem_turma:
        print("  Todos os alunos estão vinculados a uma turma.")
    for aluno in sem_turma:
        print(f"  {aluno.nome} (turma_id={aluno.turma_id})")
