from logic_layer.logic_api import LogicAPI
from ui_layer.menu_ui import MenuUi

class UIMain():
    def __init__(self, menu_ui: MenuUi) -> None:
        self.__menu_ui = menu_ui
        self.current_menu = "MAIN_MENU"

    def run(self) -> None:
        while True:
            if self.current_menu == "MAIN_MENU":
                action = self.__menu_ui.show_main_menu()
                if action == "LIST":
                    self.current_menu = "MENU_LIST"
                if action == "CREATE":
                    self.current_menu = "MENU_CREATE"
                if action == "QUIT":
                    self.current_menu = "QUIT"
                    break

            if self.current_menu == "MENU_LIST":
                action = self.__menu_ui.show_main_menu()
            if self.current_menu == "MENU_CREATE":
                print("NOT IMPLEMENTED!")
                raise NotImplementedError # forritið crashar ef það er ekki implementað rétt
        

# welcome screen sem spyr þig hver þú ert í verkefninu