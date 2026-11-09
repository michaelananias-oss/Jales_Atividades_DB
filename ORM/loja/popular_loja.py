from conexao_loja import Session
from modelos_loja import Categoria, Produto

with Session() as sessao:
    # Evita duplicar se rodar mais de uma vez
    if sessao.query(Categoria).count() == 0:
        categorias = [
            Categoria(nome="Informática"),
            Categoria(nome="Games"),
            Categoria(nome="Acessórios"),
            Categoria(nome="Escritório"),
            Categoria(nome="Áudio"),
        ]
        sessao.add_all(categorias)
        sessao.commit()

        # Recupera IDs
        cat = {c.nome: c.id for c in sessao.query(Categoria).all()}

        produtos = [
            Produto(nome="Notebook Gamer X", codigo_barras="1000000000001",
                    preco=4500.00, em_estoque=True, categoria_id=cat["Games"]),
            Produto(nome="Mouse Gamer RGB", codigo_barras="1000000000002",
                    preco=150.00, em_estoque=True, categoria_id=cat["Games"]),
            Produto(nome="Teclado Gamer Mecânico", codigo_barras="1000000000003",
                    preco=320.00, em_estoque=True, categoria_id=cat["Games"]),
            Produto(nome="Headset Gamer 7.1", codigo_barras="1000000000004",
                    preco=280.00, em_estoque=False, categoria_id=cat["Áudio"]),
            Produto(nome="Monitor 144Hz", codigo_barras="1000000000005",
                    preco=1200.00, em_estoque=True, categoria_id=cat["Informática"]),
            Produto(nome="Cadeira Gamer Pro", codigo_barras="1000000000006",
                    preco=890.00, em_estoque=True, categoria_id=cat["Acessórios"]),
            Produto(nome="Mousepad XL", codigo_barras="1000000000007",
                    preco=45.00, em_estoque=True, categoria_id=cat["Acessórios"]),
            Produto(nome="Webcam Full HD", codigo_barras="1000000000008",
                    preco=210.00, em_estoque=True, categoria_id=cat["Informática"]),
            Produto(nome="Caneta Esferográfica", codigo_barras="1000000000009",
                    preco=3.50, em_estoque=True, categoria_id=cat["Escritório"]),
            Produto(nome="Papel A4 (500 folhas)", codigo_barras="1000000000010",
                    preco=25.00, em_estoque=True, categoria_id=cat["Escritório"]),
            Produto(nome="SSD 1TB NVMe", codigo_barras="1000000000011",
                    preco=550.00, em_estoque=True, categoria_id=cat["Informática"]),
            Produto(nome="Controle Sem Fio", codigo_barras="1000000000012",
                    preco=380.00, em_estoque=True, categoria_id=cat["Games"]),
        ]
        sessao.add_all(produtos)
        sessao.commit()
        print(f"{len(categorias)} categorias e {len(produtos)} produtos cadastrados.")
    else:
        print("Banco já possui dados. Nada foi inserido.")