class Person:

    def __init__(self, name):
        self.name = name
        self.spend = 0
        self.give = 0

    def calculate_spend(self, total):
        self.spend = sum(total)

    def report(self):
        print("Name:", self.name)
        print("Spend:", self.spend)
        print("Give/Take:", self.spend-round(self.give))
