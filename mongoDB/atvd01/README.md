# Testes com MongoDB Atlas (Python)

Este repositório contém scripts simples para testar conexão e operações CRUD no MongoDB Atlas usando Python.

## Requisitos

- Python 3.10+
- Conta no MongoDB Atlas
- Usuário de banco criado no Atlas
- IP liberado no Atlas para acesso ao cluster

## Dependências

Instale as dependências do projeto:

	pip install -r requirements.txt

Pacotes usados:
- pymongo[srv]
- python-dotenv

## Configuração do MongoDB Atlas

1. No painel do Atlas, abra seu cluster.
2. Clique em Connect e depois em Drivers.
3. Copie a connection string no formato mongodb+srv://...
4. Substitua <username> e <password> pelos dados do seu usuário.

Exemplo de URI (modelo):

	mongodb+srv://SEU_USUARIO:SUA_SENHA@seu-cluster.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=seu-cluster

## Variáveis de ambiente (.env)

Crie um arquivo .env na raiz do projeto com:

Modelo de .env:

```env
MONGO_URI=mongodb+srv://SEU_USUARIO:SUA_SENHA@seu-cluster.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=seu-cluster
```

Por que usar .env?
- Evita deixar credenciais sensíveis no código-fonte.
- Facilita trocar ambiente sem alterar os scripts.
- Reduz risco de vazamento de senha ao versionar código.

## Lembrete importante (Atlas)

Antes de rodar os scripts, confirme no Atlas:
- Database Access: usuário e senha criados.
- Network Access: IP liberado.

Para testes locais, normalmente usa-se 0.0.0.0/0 temporariamente.
Use isso apenas como lembrete para ambiente de teste, não como configuração definitiva de produção.

## Como executar

Com o .env configurado, rode os scripts individualmente:

	python teste.py
	python insert.py
	python find.py
	python update.py
	python delete.py
	python crud.py
	python consultas.py

## O que cada script faz

- teste.py: valida conexão (ping no cluster Atlas).
- conexao.py: classe AtlasConnection com gerenciador de contexto.
- insert.py: insere documentos no banco produtos, coleção produtos.
- find.py: consulta documentos no banco produtos, coleção produtos.
- update.py: atualiza documentos no banco produtos, coleção produtos.
- delete.py: remove documentos no banco produtos, coleção produtos.
- crud.py: fluxo CRUD em banco loja_online, coleção produtos.
- consultas.py: consultas avançadas em banco loja_avancada, coleção eletronicos.

## Sobre os bancos usados

O projeto usa bancos diferentes em alguns arquivos:
- produtos
- loja_online
- loja_avancada

Isso faz sentido para isolar cenários de teste.

## Problemas comuns

- Erro de autenticação: revise usuário/senha na URI.
- Falha de conexão: verifique IP liberado no Atlas.
- MONGO_URI não encontrada: confirme se o arquivo .env está na raiz e com o nome correto da variável.