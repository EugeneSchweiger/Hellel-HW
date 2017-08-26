from edu.hillel.homework.Task_37 import item


class Electronics(item.Item):
    __count = 0

    def __init__(self, name, purchase_price, sale_price, description=None, energy_class=None):
        Electronics.__count+=1
        super().__init__(name, purchase_price, sale_price, description)
        self.energy_class = energy_class

    def print_info_ex(self):
        print(self.format("Energy class", self.energy_class))

