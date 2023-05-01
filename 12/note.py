import datetime

class Note():
    def __init__(self, id: int, title: str, body: str, date: datetime):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__date = date

    def getId(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getBody(self):
        return self.__body

    def getDate(self):
        return self.__date

    def setTitle(self, title: str):
        self.__title = title

    def setBody(self, body: str):
        self.__body = body

    def setDate(self, date: datetime):
        self.__date = date