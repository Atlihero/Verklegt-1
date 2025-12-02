# skjal sem ég get átt við sem virkar eins og main.py
# enginn annar er í þessu skjali
from data_layer.data_api import DataAPI
from data_layer.data_api import MenuData
from logic_layer.logic_api import LogicAPI
from ui_layer.menu_ui import MenuUi
from ui_layer.ui_main import UIMain

md = MenuData()
data = DataAPI(md)

#print(*data.read_all_menus(), sep="\n")
# stjarnan tekur allt sem er í listanum og sendir inn í fallið sem sitt eigið item

from logic_layer.menu_logic import MenuLogic

logic = MenuLogic(data)
logicLayer = LogicAPI(logic)

#print(*logicLayer.list_menus(), sep="\n")

ui = MenuUi(logicLayer)
mainMenu = UIMain(ui)

mainMenu.run()