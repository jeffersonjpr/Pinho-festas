from src.configs.database import Database


class AluguelDatabase:
    @staticmethod
    def insert(brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id):
        try:
            Database.db_cursor.execute(
                "INSERT INTO aluguel (brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id) VALUES (?, ?, ?, ?, ?)",
                (brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def delete(id):
        try:
            Database.db_cursor.execute(
                "DELETE FROM aluguel WHERE id = ?", (id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def get_all():
        try:
            Database.db_cursor.execute("SELECT * FROM aluguel")
            alugueis = Database.db_cursor.fetchall()
            return alugueis
        except Exception as e:
            print(e)

    @staticmethod
    def get_by_id(id):
        try:
            Database.db_cursor.execute(
                "SELECT * FROM aluguel WHERE id = ?", (id,))
            aluguel = Database.db_cursor.fetchone()
            return aluguel
        except Exception as e:
            print(e)

    @staticmethod
    def update(id, brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id):
        try:
            Database.db_cursor.execute(
                "UPDATE aluguel SET brinquedo_id = ?, data_montagem = ?, data_desmontagem = ?, equipe_montagem_id = ?, equipe_desmontagem_id = ? WHERE id = ?",
                (brinquedo_id, data_montagem, data_desmontagem, equipe_montagem_id, equipe_desmontagem_id, id))
            Database.db_connection.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def get_by_data_montagem(data_montagem):
        try:
            Database.db_cursor.execute(
                "SELECT * FROM aluguel WHERE data_montagem = ?", (data_montagem,))
            aluguel = Database.db_cursor.fetchone()
            return aluguel
        except Exception as e:
            print(e)
    
    @staticmethod
    def get_by_data_desmontagem(data_desmontagem):
        try:
            Database.db_cursor.execute(
                "SELECT * FROM aluguel WHERE data_desmontagem = ?", (data_desmontagem,))
            aluguel = Database.db_cursor.fetchone()
            return aluguel
        except Exception as e:
            print(e)