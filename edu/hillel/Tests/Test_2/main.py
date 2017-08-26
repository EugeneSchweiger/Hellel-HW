from edu.hillel.Tests.Test_2.libitem import LibItem
from edu.hillel.Tests.Test_2.book import Book
from edu.hillel.Tests.Test_2.magazine import Magazine
from edu.hillel.Tests.Test_2.library import Library
from edu.hillel.Tests.Test_2.visitor import Visitor
from edu.hillel.Tests.Test_2.visitors_report import PeopleReport
from edu.hillel.Tests.Test_2.literature_report import LiteratureReport
def more_reads(B,M):
    if M<B:
        print("Books are much more readible:%s times"%B)
    elif M>B:
        print("Magazines are much more readible:%s times"% M)
    else: print("Books and Magazines take to read equal times")


def delim():
    print(":"*60)
    print(":" * 60)
    print(":" * 60)


book1=Book("War and pease",1900,"Leo Tolstoy")
book2=Book("War and pease2",1900,"Leo Tolstoy")
book3=Book("War and pease3",1900,"Leo Tolstoy")
book4=Book("War and pease4",1900,"Leo Tolstoy")
book5=Book("War and pease5",1900,"Leo Tolstoy")


mag1=Magazine("Arguments and Facts",2003,"100")
mag2=Magazine("Arguments and Facts",2003,"101")
mag3=Magazine("Arguments and Facts",2003,"103")
mag4=Magazine("Arguments and Facts",2003,"104")
mag5=Magazine("Arguments and Facts",2003,"105")


lib1=Library("Our library")
lib1.add_item_to_library(book1)
lib1.add_item_to_library(book2)
lib1.add_item_to_library(book3)
lib1.add_item_to_library(book4)
lib1.add_item_to_library(book5)

lib1.add_item_to_library(mag1)
lib1.add_item_to_library(mag2)
lib1.add_item_to_library(mag3)
lib1.add_item_to_library(mag4)
lib1.add_item_to_library(mag5)

literature=LiteratureReport()
literature.add(book1)
literature.add(book2)
literature.add(book3)
literature.add(book4)
literature.add(book5)
literature.add(mag1)
literature.add(mag2)
literature.add(mag3)
literature.add(mag4)
literature.add(mag5)


# lib1.print_library()
visit1=Visitor("Mark Zukkerberg")
visit2=Visitor("Ilon Mask")
visit3=Visitor("Star Lord")
visit4=Visitor("Kerk Pirr")
visit5=Visitor("Ivan Groznyy")

visitors=PeopleReport()
visitors.add(visit1)
visitors.add(visit2)
visitors.add(visit3)
visitors.add(visit4)
visitors.add(visit5)

# visit1.take_item(book1,lib1)
# visit1.take_item(book2,lib1)
# visit1.take_item(book2,lib1)
# visit1.take_item(mag1,lib1)
# visit2.take_item(book3,lib1)
# visit2.take_item(book4,lib1)
visit2.take_item(book1,lib1)
visit2.take_item(book2,lib1)
visit2.take_item(book2,lib1)
visit2.take_item(mag1,lib1)
visit1.take_item(book3,lib1)
visit1.take_item(book4,lib1)

lib1.print()
visit1.print_info()
delim()
print("RETURNING")
visit2.return_item(book1,lib1,visitors,literature)
visit2.return_item(mag1,lib1,visitors,literature)
visit2.return_item(book2,lib1,visitors,literature)
visit2.return_item(book3,lib1,visitors,literature)
visit1.return_item(book3,lib1,visitors,literature)
visit1.return_item(book4,lib1,visitors,literature)
lib1.print()


visitors.best_reader()
literature.best_readed()
more_reads(Book._total_reads,Magazine._total_reads)
