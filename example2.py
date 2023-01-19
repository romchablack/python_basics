class Table:
    count = 0

    def __init__(self, data=dict()) -> None:
        self.data = data

    def add_data(self, key, val):
        self.data[key] = val

    def remove_data(self, key):
        if key in self.data:
            del self.data[key]

    def check_data(self, key):
        return key in self.data

    @classmethod
    def list_tables(cls):
        return cls.count

    @staticmethod
    def to_lower(str):
        return str.lower()
