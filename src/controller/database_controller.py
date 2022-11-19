import json

path_to_file = 'src/config.json'


class DatabaseController:
    @staticmethod
    def get_database_name():
        with open(path_to_file) as json_file:
            data = json.load(json_file)
            return data['database_name']

    @staticmethod
    def set_database_name(database_name):
        with open(path_to_file) as json_file:
            data = json.load(json_file)
            data['database_name'] = database_name

        with open(path_to_file, 'w') as outfile:
            json.dump(data, outfile)
