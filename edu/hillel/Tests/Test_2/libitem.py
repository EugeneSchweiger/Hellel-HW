class LibItem:
    __QUOTE="\""
    __id = 0
    def __init__(self,name,year):
        LibItem.__id+=1
        self.id=LibItem.__id
        self.name= LibItem.__QUOTE + name + LibItem.__QUOTE
        self.year=year
        self.__owner = None
        self.__readed_times = 0
    def set_reads_plus(self):
        pass

    def set_reads(self):
        self.__readed_times += 1
        self.set_reads_plus()

    def get_reads(self):
        return self.__readed_times

    def set_owner(self, owner):
            self.__owner = owner

    def get_owner(self):
            return self.__owner

