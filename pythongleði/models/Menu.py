from datetime import date
from MenuItem import MenuItem

class Menu():
    def __init__(self, main_course: MenuItem, vegan_course: MenuItem, soup: MenuItem, menu_date: date = date.today()):
        self.menu_date = menu_date
        self.main_course = main_course
        self.vegan_course = vegan_course
        self.soup = soup

    def __str__(self):
        return f"{self.menu_date}:\n\t{self.main_course}\n\t{self.vegan_course}\n\t{self.soup}\n"

    def __repr__(self):
        return str(self)