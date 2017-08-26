class Library:
    _BACKSPACE = "%-10s"
    _DELIM = ":"
    _SPACE = "%40s"
    _FORMAT = _BACKSPACE + _SPACE
    def __init__(self,name):
        self.library={}
        self.name=name
    def format(self, name, value):
        name_format = name + Library._DELIM
        return Library._FORMAT % (name_format, value)

    def add_item_to_library(self, item):
        self.library[item] = self.name
        item.set_owner(self.name)

    def print_library(self):
        # for item in sorted(self.library, key=lambda item: item.name):
        print(self.name,"Items are:")
        for item in self.library:
            # print("Item:%s  Owner:%s"%(item.name,self.name))
            print(self.format("Item", item.name))
            print(self.format("Owner",item.get_owner()))
            print("_"*60)
    def give_item_to_visitor(self,visitor,item):
        item.set_owner(visitor.name)
        self.library[item] = self.library.get(item, visitor.name)
    def return_item_to_library(self,item):
        if item.get_owner()!=self.name:
            item.set_owner(self.name)
            self.library[item] = self.library.get(item, self.name)