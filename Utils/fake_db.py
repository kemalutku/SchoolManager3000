class FakeDB:
    def cursor(self):
        return None

    def commit(self):
        pass

    def rollback(self):
        pass