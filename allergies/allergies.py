class Allergies:
    items = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return self.score & self.items[item] != 0

    @property
    def lst(self):
        return [i for i in self.items if self.allergic_to(i)]

