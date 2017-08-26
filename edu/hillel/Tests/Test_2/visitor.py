from edu.hillel.Tests.Test_2.library import Library
class Visitor:
    __LIMIT=2
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
                print("*"*30)
                print("Item %s has been taken by %s"%(item.name,self.name))
            else:
                print("*"*30)
                print("%sNot in library"%item.name)
        else:
            print("*"*30)
            print("Too much books handing by %s"%self.name)
    def return_item(self,item,library,people,lit):
        if item.name in self._items_list:
            del self._items_list[item.name]
            library.return_item(item)
            self._items_read+=1
            item.set_reads()
            people.update(self)
            lit.update(item)
    def print_info(self):
        print("*"*60)
        print(self.name,"Items list:", len(self._items_list))
        for i in self._items_list:
            print(i,"Original owner:", self._items_list[i])
        print("*"*60)