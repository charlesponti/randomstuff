from typing import Dict

class DuplicateTableError(ValueError):
    def __init__(self, ofcorrecttype):
        super().__init__(ofcorrecttype)

class Database():
    tables: Dict[str, Dict]

    def __init__(self, *args, **kwargs):
        self.tables = {}

    def add_table(self, name: str):
        if name not in self.tables.keys():
            self.tables[name] = []
        else:
            raise DuplicateTableError

    def add_to_table(self, name: str, record):
        self.tables[name].append(record)
        return record

    def get_table(self, name: str):
        return self.tables[name]

