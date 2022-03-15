from card import Card
from enum import Enum


class UserType(Enum):
    HUMAN = 1
    COMPUTER = 2


class UserStatus(Enum):
    WIN = 1
    LOST = 2


class User:
    def __init__(self, user_type, user_name):
        self.__user_name = user_name
        self.__user_type = user_type
        self.__card = Card(user_name)
        self.__status = None

    @property
    def type(self):
        return self.__user_type

    @property
    def name(self):
        return self.__user_name

    @property
    def status(self):
        return self.__status

    def show_card(self):
        print(self.__card)

    def strike_out(self, number):
        if self.__user_type == UserType.HUMAN:
            if not self.__card.strike_out(number):
                self.__status = UserStatus.LOST
                return
        else:
            self.__card.strike_out(number)

        if self.__card.get_win_status():
            self.__status = UserStatus.WIN
