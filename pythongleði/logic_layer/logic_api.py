from models.Menu import Menu
from menu_logic import MenuLogic


class LogicAPI():
    def __init__(self, menu_logic: MenuLogic) -> None:
        self.__menu_logic = menu_logic

    def list_menus(self) -> list[Menu]:
        return self.__menu_logic.list_menus()
    
    #def create_menu(self, main: MenuItem, vegan: MenuItem, soup: MenuItem):
