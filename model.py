'''
Student ID: u3301989
Assignment: 1, Part5
Date Created: April 11, 2026
Last Updated: April 15, 2026
'''

class Product:
    def __init__(self, name, price, description):
        self.__name = name
        self.__price = price
        self.__description = description

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return self.__name