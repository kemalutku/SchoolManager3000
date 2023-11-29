class FakeDB:
    def cursor(self):
        return None

    def commit(self):
        pass

    def rollback(self):
        pass

    def next_result(self):
        pass