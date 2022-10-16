aluguel = """
    CREATE TABLE  IF NOT EXISTS aluguel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brinquedo_id INTEGER NOT NULL,
        data_montagem INTEGER NOT NULL,
        data_desmontagem INTEGER NOT NULL,
        equipe_montagem_id INTEGER NOT NULL,
        equipe_desmontagem_id INTEGER NOT NULL,
        FOREIGN KEY (brinquedo_id) REFERENCES brinquedo(id),
        FOREIGN KEY (equipe_montagem_id) REFERENCES equipe(id),
        FOREIGN KEY (equipe_desmontagem_id) REFERENCES equipe(id)
    );"""