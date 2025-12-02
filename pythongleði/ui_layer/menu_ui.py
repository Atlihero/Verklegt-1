from logic_layer.logic_api import LogicAPI

class MenuUi():
    def __init__(self, logic_layer: LogicAPI) -> None:
        self.__logic_api = logic_layer
        
    def _prompt_choice(self, valid_choices: list[str]):
        valid_lower = [c.lower() for c in valid_choices]

        while True:
            choice = input("> ").strip().lower()

            if choice in valid_lower:
                return choice
            # allur kóði eftir á er ef choice er ógilt

            print(f"Invalid choice: options are {" ". join(valid_lower)}")
            # ef hann velur vitlaust þá keyrir loopan aftur

    def show_main_menu(self) -> str:
        ''' Prints main menu! '''
        # TODO handle dynamic choice
        print("\n=== Main Menu ===")
        print("1. Show menus")
        print("2. Create menu")
        print("q. Quit")

        choice = self.__prompt_choice(["1", "2", "q"]) # getum bara fengið 1 af þessum 3 valkostum til baka
        if choice == "1":
            return "LIST" #self.__logic_api.list_menus()
        if choice == "2":
            return "CREATE"
        # if choice == "q": 
        return "QUIT"

def show_menu_list_flow(self) -> str:
        ''' Prints main menu! '''
        # TODO handle dynamic choice
        print("\n=== Food Menus ===")
        print(*self.__logic_api.list_menus(), sep="\n")

        print("b. Back")
        print("q. Quit")

        choice = self.__prompt_choice(["b""q"]) # getum bara fengið 1 af þessum 3 valkostum til baka
        if choice == "b":
            return "LIST" #self.__logic_api.list_menus()
        if choice == "q": 
            return "MAIN_MENU"
        
        return "QUIT"


