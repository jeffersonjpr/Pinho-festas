pessoa_equipe = """
    CREATE TABLE  IF NOT EXISTS pessoa_equipe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pessoa_id INTEGER NOT NULL,
        equipe_id INTEGER NOT NULL,
        FOREIGN KEY (pessoa_id) REFERENCES pessoa(id),
        FOREIGN KEY (equipe_id) REFERENCES equipe(id)
    );"""