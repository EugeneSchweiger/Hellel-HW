from edu.hillel.homework.Task_37 import item

class Food(item.Item):
        __count=0
        def __init__  (self, name, purchase_price, sale_price,description=None, expire_date="42 years"):
            Food.__count+=1
            super().__init__(name, purchase_price, sale_price,description)
            self.expire_date = expire_date



        def print_info_ex(self):
            print(self.format("Expire date", self.expire_date))

