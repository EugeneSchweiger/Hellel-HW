from edu.hillel.homework.Task_37.item import Item


class Store(object):
    def __init__(self):
        self.__items_balance = {}

    def add_item(self, item, qty):
        self.__items_balance[item] = self.__items_balance.get(item, 0) + qty

    # def add_item(self, *items):
    #     for item in items:
    #         self.__items_balance[item[0]] = self.__items_balance.get(item[0], 0) + item[1]

    def withdraw_item(self, item, qty):
        if item in self.__items_balance:
            if self.__items_balance[item] >= qty:
                self.__items_balance[item] -= qty

    def balance(self, item):
        return self.__items_balance.get(item, 0)

    # print(my_store.balance(item1))

    def balance_format(self, name,value):
        name_format = name + Item._DELIM
        return Item._FORMAT % (name_format, value)

    def print_balance(self):
        print("\nStorage list:")
        for item in sorted(self.__items_balance, key=lambda item : item.name):
            print (self.balance_format(item.name, self.__items_balance[item]))