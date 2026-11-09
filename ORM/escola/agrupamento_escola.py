from sqlalchemy import func

from database_escola import Session
from modelos_escola import Aluno

with Session() as sessao:
    relatorio = (
        sessao.query(Aluno.turma_id, func.count(Aluno.id).label("total_alunos"))
        .group_by(Aluno.turma_id)
        .having(func.count(Aluno.id) > 30)
        .all()
    )

print("Turmas com mais de 30 alunos:")
if not relatorio:
    print("  Nenhuma turma atende ao critério.")
for turma_id, total_alunos in relatorio:
    print(f"  Turma {turma_id}: {total_alunos} alunos")
