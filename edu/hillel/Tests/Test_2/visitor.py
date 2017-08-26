from edu.hillel.Tests.Test_2.library import Library
class Visitor:
    __LIMIT=3
    def __init__(self,name):
        self.name=name
        self._items_list={}
        self._items_read=0

    def take_item(self,item,library):
        if len(self._items_list)<=Visitor.__LIMIT:
            if item.get_owner()==library.name:
                item.set_owner(self.name)
                self._items_list[item.name]=library.name
                library.give_item_to_visitor(self,item)
            else: print("Not in library")
        else: print("Too much books handing")
    def return_item(self,item,library):
        if item.name in self._items_list:
            del self._items_list[item.name]
            library.return_item_to_library(item)
            self._items_read+=1
            item.set_reads()
    def print_info(self):
        print(self.name,"Items list:", len(self._items_list))
        for i in self._items_list:
            print(i,"owner:", self._items_list[i])