cliente = """
    CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            cep TEXT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            endereco TEXT NOT NULL
        );
    """
