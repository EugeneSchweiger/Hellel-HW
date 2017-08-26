from edu.hillel.Tests.Test_2.visitor import Visitor
class Literature:
    def __init__(self):
        self.__books_list={}
    def add(self,book):
        self.__books_list[book.name]=book.get_reads()

    def best_readed(self):
        for key in sorted(self.__books_list, key=self.__books_list.get, reverse=True):
            print("%s has been readed \t %s times" % (key, self.__books_list[key]))


