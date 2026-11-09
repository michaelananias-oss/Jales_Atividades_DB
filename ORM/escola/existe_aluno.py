from sqlalchemy import exists, select

from database_escola import Session
from modelos_escola import Aluno

TURMA_ID = 5

with Session() as sessao:
    ha_alunos = sessao.scalar(
        select(exists().where(Aluno.turma_id == TURMA_ID))
    )

if ha_alunos:
    print(f"Sim, há alunos matriculados na turma {TURMA_ID}.")
else:
    print(f"Não há alunos matriculados na turma {TURMA_ID}.")
