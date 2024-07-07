class Move:
    def __init__(self, name, type, power, accuracy, category, effect=None):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.effect = effect

    def apply_effect(self, target):
        if self.effect:
            print(f"{self.name} had an additional effect on {target.name}!")
            self.effect(target)
