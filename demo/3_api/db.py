class DB:
    index = 1
    database = {}

    def insert(self, row):
        row.id = self.index
        self.database[self.index] = row
        self.index += 1
        return row

    def get(self, id):
        return self.database[id]

    def get_all(self):
        return [x for x in self.database.values()]

    def update(self, id, row):
        self.database[id] = row
        return row

    def delete(self, id):
        row = self.database.pop(id)
        return row
