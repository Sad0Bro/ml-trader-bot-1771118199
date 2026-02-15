class MLTrader:
    def __init__(self):
        self.model = None
        self.data = None

    def load_data(self):
        pass

    def train_model(self):
        pass

    def make_predictions(self):
        pass

    def execute_trades(self):
        pass

class Data:
    def __init__(self):
        self Training_Data = []
        self.Testing_Data = []

class Model:
    def __init__(self):
        self.type = None
        self.parameters = None

def main():
    trader = MLTrader()
    data = Data()
    model = Model()

if __name__ == "__main__":
    main()