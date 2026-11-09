from datetime import date

from sqlalchemy import or_

from database_escola import Session
from modelos_escola import Aluno, Turma

with Session() as sessao:
    turma = sessao.query(Turma).filter_by(nome_turma="3º Ano A").first()
    if turma is None:
        print("Turma '3º Ano A' não encontrada.")
    else:
        print(f"Turma encontrada: {turma}")

    print("\nAlunos nascidos após 2005 ou com e-mail @escola.com:")
    alunos = (
        sessao.query(Aluno)
        .filter(
            or_(
                Aluno.data_nascimento > date(2005, 12, 31),
                Aluno.email.endswith("@escola.com"),
            )
        )
        .all()
    )
    if not alunos:
        print("Nenhum aluno corresponde ao filtro.")
    for aluno in alunos:
        print(f"  {aluno} - {aluno.email}")
