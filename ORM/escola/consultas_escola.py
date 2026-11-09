from sqlalchemy import select

from database_escola import Session
from modelos_escola import Aluno

with Session() as sessao:
    aluno = sessao.get(Aluno, 1)
    if aluno is None:
        print("Aluno de id=1 não encontrado.")
    else:
        print(f"Aluno encontrado: matrícula {aluno.matricula}, nome {aluno.nome}")

    print("\nTodos os alunos (session.query(...).all()):")
    alunos = sessao.query(Aluno).all()
    if not alunos:
        print("Nenhum aluno cadastrado.")
    for item in alunos:
        print(f"  {item}")

    print("\nRetorno sem scalars(): cada linha é uma tupla/Row com o aluno.")
    linhas = sessao.execute(select(Aluno)).all()
    for linha in linhas:
        print(f"  {linha!r}")

    print("\nRetorno com scalars(): cada item é diretamente um objeto Aluno.")
    objetos = sessao.execute(select(Aluno)).scalars().all()
    for item in objetos:
        print(f"  {item}")
