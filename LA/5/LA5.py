class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.name} is a {self.role} hero."


layla = Hero("Layla", "marksman")
print(layla.describe())
