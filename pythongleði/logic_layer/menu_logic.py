# TODO import dataapi
from data_layer.data_api import DataAPI

class MenuLogic():
    def __init__(self, data_layer: DataAPI) -> None:
        self.__data_api = data_layer

    def list_menus(self):
        return self.__data_api.read_all_menus()