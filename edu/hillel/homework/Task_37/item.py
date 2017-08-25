
class Item(object):
    _BACKSPACE = "%-20s"
    _DELIM = ":"
    _SPACE = "%40s"
    _FORMAT = _BACKSPACE + _SPACE
    __total_count = 0
    def __init__(self, name, purchase_price=0, sale_price=0,description=None):
        Item.__total_count += 1
        self.id = Item.__total_count
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.description=description

    def format(self, name, value):
        name_format = name + Item._DELIM
        return Item._FORMAT % (name_format, value)

    def print_info(self):
        print()
        print("-----------------------------")
        print(self.format("ID", self.id))
        print(self.format("Name", self.name))
        print(self.format("Description", self.description))
        print(self.format("Income price", self.purchase_price))
        print(self.format("Outcome price", self.sale_price))
        self.print_info_ex()

    def print_info_ex(self):
        pass
