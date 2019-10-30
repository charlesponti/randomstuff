
class Database():
    def __init__(self, *args, **kwargs):
        self.tables = {}

    def add_table(self, name: str):
        self.tables[name] = []

    def add_to_table(self, name: str, record):
        self.tables[name].append(record)
        return record

    def get_table(self, name: str):
        return self.tables[name]

