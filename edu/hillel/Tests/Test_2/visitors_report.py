from edu.hillel.Tests.Test_2.visitor import Visitor
class PeopleReport:
    def __init__(self):
        self.__pepole_list={}
    def add(self,visitor):
        self.__pepole_list[visitor.name]=visitor._items_read
    def get_people_list(self):
        for i in self.__pepole_list:
            print(i,self.__pepole_list[i])

    def update(self,visitor):
        self.__pepole_list[visitor.name] = visitor._items_read

    def best_reader(self):
        for key in sorted(self.__pepole_list, key=self.__pepole_list.get, reverse=True):
            print("Reader:%s\t readed %s items" % (key, self.__pepole_list[key]))


