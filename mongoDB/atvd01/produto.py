class Produto:
    """
    Classe que representa um produto.
    Fornece métodos `to_dict` e `from_dict` para conversão.
    """

    def __init__(
        self,
        id: str | None,
        nome: str,
        preco: float,
        quantidade: int = 0,
        categorias: list[str] | None = None,
        ativo: bool = True,
    ):
        self.id = id
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = int(quantidade)
        self.categorias = categorias or []
        self.ativo = bool(ativo)

    def to_dict(self):
        """
        Converte o objeto `Produto` para um dicionário pronto para armazenamento.
        Usa a chave `_id` se `id` estiver presente (útil para MongoDB).
        """
        data: dict[str, object] = {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "categorias": list(self.categorias),
            "ativo": self.ativo,
        }
        if self.id is not None:
            data["_id"] = self.id
        return data

    @classmethod
    def from_dict(cls, data: dict[str, object]):
        """
        Cria uma instância de `Produto` a partir de um dicionário.
        Aceita tanto `_id` quanto `id` como identificador.
        """
        id_val = data.get("_id", data.get("id"))
        if id_val is not None:
            try:
                id_val = str(id_val)
            except Exception:
                pass

        return cls(
            id=id_val,
            nome=data.get("nome", ""),
            preco=float(data.get("preco", 0.0)),
            quantidade=int(data.get("quantidade", 0)),
            categorias=list(data.get("categorias", [])),
            ativo=bool(data.get("ativo", True)),
        )

    def __repr__(self):
        return (
            f"Produto(id={self.id!r}, nome={self.nome!r}, preco={self.preco!r}, "
            f"quantidade={self.quantidade!r}, categorias={self.categorias!r}, ativo={self.ativo!r})"
        )
