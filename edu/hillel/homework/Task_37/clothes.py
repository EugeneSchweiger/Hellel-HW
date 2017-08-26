from edu.hillel.homework.Task_37 import item

class Clothes(item.Item):
        __count=0
        def __init__  (self, name, purchase_price, sale_price,description=None, clothes_size=42):
            Clothes.__count+=1
            super().__init__(name, purchase_price, sale_price,description)
            self.clothes_size = clothes_size



        def print_info_ex(self):
            print(self.format("Expire date", self.clothes_size))