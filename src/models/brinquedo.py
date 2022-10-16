brinquedo = """
    CREATE TABLE  IF NOT EXISTS  brinquedo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        largura REAL NOT NULL,
        altura REAL NOT NULL,
        comprimento REAL NOT NULL
    );"""