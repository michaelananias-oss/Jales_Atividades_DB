from datetime import date

from sqlalchemy import case

from database_escola import Session
from modelos_escola import Aluno

TURMA_ID = 1
status_data_nascimento = case(
    (Aluno.data_nascimento.is_(None), "Data não informada"),
    (Aluno.data_nascimento > date(2005, 12, 31), "Nascido após 2005"),
    else_="Nascido até 2005",
).label("status_data_nascimento")

with Session() as sessao:
    consulta = (
        sessao.query(Aluno)
        .filter_by(turma_id=TURMA_ID)
        .add_columns(status_data_nascimento)
    )
    resultados = consulta.all()

print(f"Alunos da turma {TURMA_ID} e status calculado:")
if not resultados:
    print("  Nenhum aluno encontrado.")
for aluno, status in resultados:
    print(f"  {aluno.nome} - matrícula {aluno.matricula} - {status}")
