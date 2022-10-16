from ast import Delete
from src.configs.database import Database
from src.database.pessoa_database import PessoaDatabase

database = Database()

print(database.db_cursor)

PessoaDatabase.insert("João", "123456789", "123456789")
PessoaDatabase.insert("Maria", "987654321", "987654321")
print(PessoaDatabase.get_all())
