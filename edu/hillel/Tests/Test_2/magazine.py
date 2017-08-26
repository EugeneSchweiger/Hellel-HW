from edu.hillel.Tests.Test_2.libitem import LibItem
class Magazine(LibItem):
    __NUMBER=" №"
    _total_reads=0
    def __init__(self, name, year, mag_number):
        super().__init__(name,year)
        self.number = mag_number
        self.name = self.name + Magazine.__NUMBER + self.number
    def set_reads_plus(self):
        Magazine._total_reads+=1
