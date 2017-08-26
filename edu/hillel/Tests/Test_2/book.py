from edu.hillel.Tests.Test_2.libitem import LibItem
class Book(LibItem):
    _total_reads=0
    def __init__(self, name, year, writer):
        super().__init__(name,year)
        self.writer=writer
    def set_reads_plus(self):
        Book._total_reads+=1

