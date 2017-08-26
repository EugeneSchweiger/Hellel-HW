from edu.hillel.Tests.Test_2.lib_item import Lib_item
from edu.hillel.Tests.Test_2.book import Book
from edu.hillel.Tests.Test_2.magazine import Magazine
from edu.hillel.Tests.Test_2.library import Library
from edu.hillel.Tests.Test_2.visitor import Visitor
from edu.hillel.Tests.Test_2.visitors import People
from edu.hillel.Tests.Test_2.literature import Literature
def more_reads(B,M):
    if M<B:
        print("Books are much more readible:%s times"%B)
    elif M>B:
        print("Magazines are much more readible:%s times"% M)
    else: print("Books and Magazines take to read equal times")


book1=Book("War and pease",1900,"Leo Tolstoy")
book2=Book("War and pease2",1900,"Leo Tolstoy")
mag1=Magazine("Arguments and Facts",2003,"100")
mag2=Magazine("Arguments and Facts",2003,"101")
lib1=Library("Our library")
lib1.add_item_to_library(book1)
lib1.add_item_to_library(book2)
lib1.add_item_to_library(mag1)
lib1.add_item_to_library(mag2)
# lib1.print_library()
visit1=Visitor("Mike")
visit2=Visitor("Jack")
visit1.take_item(book1,lib1)
visit1.take_item(book1,lib1)
visit1.take_item(mag1,lib1)
lib1.print_library()
visit1.return_item(book1,lib1)
lib1.print_library()
visit1.print_info()
p1=People()
p1.add(visit1)
p1.best_reader()
lit=Literature()
lit.add(book1)
lit.best_readed()

more_reads(Book._total_reads,Magazine._total_reads)
