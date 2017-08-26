from edu.hillel.Tests.Test_2.lib_item import Lib_item
class Book(Lib_item):
    _total_reads=0
    def __init__(self, name, year, writer):
        super().__init__(name,year)
        self.writer=writer
        self.__readed_times=0
        self.__owner = None
    def set_owner(self,owner):
        self.__owner=owner
    def get_owner(self):
        return self.__owner
    def get_reads(self):
        return self.__readed_times
    def set_reads(self):
        self.__readed_times+=1
        Book._total_reads+=1
    # def read_count(self):
    #     return Book._total_reads