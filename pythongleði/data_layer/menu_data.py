import csv # csv stendur fyrir comma seperated values
from datetime import date
from models.Menu import Menu
from models.MenuItem import MenuItem


DATA_PATH = "./_data/menus.csv"

class MenuData():
    def __init__(self) -> None:
        pass

    def read_all(self) -> list[Menu]: # er typeint og segir okkur hvað fallið skilar
        menus: list[Menu] = []
        
        with open(DATA_PATH, mode="r", encoding="utf-8") as data_file: # fáum séríslenska stafi rétt inn með því að nota utf-8
            reader: csv.DictReader = csv.DictReader(data_file, delimiter = ";") # skilgreinuum variable reader
            # tekur inn skjalið data_file og gerir split fyrir okkur og notar efstu línuna og býr til dict úr henni
            # default er ; 
            
            for line in reader:
                menu_date: date = date.fromisoformat(line.get("date", "")) # afþví dagsetningin er í ISO formati í skjalinu
                main: MenuItem = MenuItem(line.get("main", ""), MenuItem.MealType.main) # erum að skilgreina hvað er að koma inn í línuna
                vegan: MenuItem = MenuItem(line.get("vegan", ""), MenuItem.MealType.vegan)
                soup: MenuItem = MenuItem(line.get("soup", ""), MenuItem.MealType.soup)
                menu: Menu = Menu(main, vegan, soup, menu_date)
                menus.append(menu)

        return menus

#TODO W