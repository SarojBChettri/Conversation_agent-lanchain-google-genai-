class Memory:
    def __init__(self):
        self.history = []

    def add(self, interaction):
        self.history.append(interaction)

    def get_history(self):
        return self.history