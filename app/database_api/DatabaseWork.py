import json


class WorkWithDataBase:
    @staticmethod
    def write_data_to_database(user_id: str, field: str, get_data: str, path_to_database: str):
        user_id = str(user_id)
        write_structure = json.load(open(path_to_database, encoding="utf-8"))
        if not user_id in write_structure:
            write_structure[user_id] = {}
        write_structure[user_id][field] = get_data
        with open(path_to_database, "w", encoding="utf-8") as f:
            json.dump(write_structure, f, indent=4, ensure_ascii=False)
    
    @staticmethod
    def read_data_from_database(user_id: str, field: str, path_to_database: str):
        with open(path_to_database, "r", encoding="utf-8") as f:
            user_id = str(user_id)
            read_structure = json.load(f)[user_id][field]
        return read_structure
    
    @staticmethod
    def clear_database_user(user_id: str, path_to_database: str):
        user_id = str(user_id)
        new_struct = json.load(open(path_to_database, encoding="utf-8"))
        if user_id in new_struct:
            del new_struct[user_id]
            with open(path_to_database, "w", encoding="utf-8") as f:
                json.dump(new_struct, f, indent=4, ensure_ascii=False)
        return
