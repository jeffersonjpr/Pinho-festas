import os
import unittest

from src.controller.database_controller import DatabaseController
from src.controller.pessoa_controller import PessoaController


def remove_db():
    if os.path.exists("test.db"):
        os.remove("test.db")


class TestPessoaController(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        DatabaseController.set_database_name('test.db')

        if os.path.exists('teste.db'):
            os.remove('test.db')

    @classmethod
    def tearDownClass(cls):

        if os.path.exists('test.db'):
            os.remove('test.db')

    def test_database_name(self):
        self.assertEqual(DatabaseController.get_database_name(), 'test.db')
        print(DatabaseController.get_database_name())

    def test_insert(self):
        self.assertIsInstance(
            PessoaController.insert("João", "123", "123"), int)

    def test_insert_cpf_exists(self):
        self.assertIsInstance(PessoaController.insert(
            "Maria", "4321", "321"), int)
        with self.assertRaises(Exception):
            PessoaController.insert("Maria", "4321", "321")

    def test_delete(self):
        pessoa_id = PessoaController.insert("João", "1233", "123")
        self.assertIsNone(PessoaController.delete(pessoa_id))

    def test_delete_not_exists(self):
        with self.assertRaises(Exception):
            PessoaController.delete(123323)

    def test_get_by_id(self):
        pessoa_id = PessoaController.insert("João", "123333", "123")
        self.assertIsInstance(PessoaController.get_by_id(pessoa_id), tuple)

    def test_get_by_id_not_exists(self):
        with self.assertRaises(Exception):
            PessoaController.get_by_id(1233323)

    def test_get_all(self):
        PessoaController.insert("João", "32132", "123")
        PessoaController.insert("Maria", "33213", "123")
        self.assertIsInstance(PessoaController.get_all(), list)

    def test_update(self):
        pessoa_id = PessoaController.insert("João", "1233", "123")
        self.assertIsNone(PessoaController.update(
            pessoa_id, "João2", "12333", "123"))
        pessoa = PessoaController.get_by_id(pessoa_id)
        self.assertEqual(pessoa[1], "João2")


if __name__ == '__main__':
    unittest.main()
