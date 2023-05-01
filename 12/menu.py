class Menu():
    def __init__(self, menu: list, name: str):
        self.__menu = menu
        self.__name = name

    def getName(self):
        return self.__name

    def getMenu(self):
        return self.__menu

    def getLength(self):
        return len(self.__menu)