from src.configs.database import Database


class AluguelDatabase:
    database = Database()

    @staticmethod
    def insert(brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id):
        try:
            AluguelDatabase.database.db_cursor.execute(
                "INSERT INTO aluguel (brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id) VALUES (?, ?, ?, ?, ?)",
                (brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id))
            AluguelDatabase.database.db_connection.commit()
        except Exception as e:
            print("AluguelDatabase", e)

    @staticmethod
    def delete(id):
        try:
            AluguelDatabase.database.db_cursor.execute(
                "DELETE FROM aluguel WHERE id = ?", (id))
            AluguelDatabase.database.db_connection.commit()
        except Exception as e:
            print("AluguelDatabase", e)

    @staticmethod
    def get_all():
        try:
            AluguelDatabase.database.db_cursor.execute("SELECT * FROM aluguel")
            alugueis = AluguelDatabase.database.db_cursor.fetchall()
            return alugueis
        except Exception as e:
            print("AluguelDatabase", e)

    @staticmethod
    def get_by_id(id):
        try:
            AluguelDatabase.database.db_cursor.execute(
                "SELECT * FROM aluguel WHERE id = ?", (id,))
            aluguel = AluguelDatabase.database.db_cursor.fetchone()
            return aluguel
        except Exception as e:
            print("AluguelDatabase", e)

    @staticmethod
    def update(id, brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id):
        try:
            AluguelDatabase.database.db_cursor.execute(
                "UPDATE aluguel SET brinquedo_id = ?, data_montagem = ?, data_desmontagem = ?, equipe_montagem_id = ?, equipe_desmontagem_id = ? WHERE id = ?",
                (brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id, id))
            AluguelDatabase.database.db_connection.commit()
        except Exception as e:
            print("AluguelDatabase", e)

    @staticmethod
    def get_by_equipe_and_data_montagem(equipe_id, data_inicio, data_fim):
        try:
            AluguelDatabase.database.db_cursor.execute(
                "SELECT * FROM aluguel WHERE equipe_montagem_id = ? AND data_montagem BETWEEN ? AND ?", (equipe_id, data_inicio, data_fim))
            alugueis = AluguelDatabase.database.db_cursor.fetchall()
            return alugueis
        except Exception as e:
            print("AluguelDatabase", e)
    
    @staticmethod
    def get_by_equipe_data_desmontagem(equipe_id, data_inicio, data_fim):
        try:
            AluguelDatabase.database.db_cursor.execute(
                "SELECT * FROM aluguel WHERE equipe_desmontagem_id = ? AND data_desmontagem BETWEEN ? AND ?", (equipe_id, data_inicio, data_fim))
            alugueis = AluguelDatabase.database.db_cursor.fetchall()
            return alugueis
        except Exception as e:
            print("AluguelDatabase", e)
    
    @staticmethod
    def get_by_brinquedo_datas(brinquedo_id, data_montagem, data_desmontagem):
        try:
            AluguelDatabase.database.db_cursor.execute(
                "SELECT * FROM aluguel WHERE brinquedo_id = ? AND data_montagem BETWEEN ? AND ?", (brinquedo_id, data_montagem, data_desmontagem))
            alugueis = AluguelDatabase.database.db_cursor.fetchall()
            return alugueis
        except Exception as e:
            print("AluguelDatabase", e)
