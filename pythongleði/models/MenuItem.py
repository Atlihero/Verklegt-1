from enum import StrEnum

class MenuItem(object):
    class MealType(StrEnum):
        main = "MAIN"
        vegan = "VEGAN"
        soup = "SOUP"

    def __init__(self, name: str, meal_type: MealType):
        self.name = name
        self.meal_type = meal_type

    def __str__(self):
        return f"{self.meal_type}: {self.name}"
    
    def __repr__(self):
        return str(self)