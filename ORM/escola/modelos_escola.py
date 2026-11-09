from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Turma(Base):
    __tablename__ = 'turmas'

    id = Column(Integer, primary_key=True)
    nome_turma = Column(String(50), nullable=False)
    ano_letivo = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Turma(id={self.id}, nome_turma='{self.nome_turma}', ano_letivo={self.ano_letivo})>"

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True)
    matricula = Column(String(20), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True)
    data_nascimento = Column(Date)
    turma_id = Column(Integer, ForeignKey('turmas.id'), nullable=True)
    
    def __repr__(self):
        return f"<Aluno(matricula='{self.matricula}', nome='{self.nome}')>"