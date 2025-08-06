class FunctionProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        raise NotImplementedError("Must override process() in subclass.")


class DataNormalizer(FunctionProcessor):
    def process(self):
        return (self.data - self.data.mean()) / self.data.std()
