from menu_data import MenuData 
from models.Menu import Menu

# erum að tengja úr vrikniklasanum upp í hausinn
class DataAPI():
    def __init__(self, menu_data: MenuData) -> None:
        self.__menu_data = menu_data 

    def read_all_menus(self) -> list[Menu]:
        return self.__menu_data.read_all()

    # TODO save_menu


