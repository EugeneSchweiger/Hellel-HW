class Lib_item:
    __QUOTE="\""
    __id = 0
    def __init__(self,name,year):
        Lib_item.__id+=1
        self.id=Lib_item.__id
        self.name=Lib_item.__QUOTE+name+Lib_item.__QUOTE
        self.year=year
