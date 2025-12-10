from ui_layer.mainUI import Uimain

def start_() -> Uimain:
    main: Uimain = Uimain()
    return main

def main() -> None:
    main: Uimain = start_()
    main.start()



if __name__ == "__main__":
    main()