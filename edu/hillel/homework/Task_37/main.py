from edu.hillel.homework.Task_37.food import Food
from edu.hillel.homework.Task_37.electronics import Electronics
from edu.hillel.homework.Task_37.clothes import Clothes
from edu.hillel.homework.Task_37.store import Store
from edu.hillel.homework.Task_37.invoice_journal import InvoiceJournal
from edu.hillel.homework.Task_37.sale_invoice import SaleInvoice
from edu.hillel.homework.Task_37.report import Report
import datetime
#
# i=Food("sugar",100,200,"just sugar")
# i2=Food("sugar2",100,200,"just sugar2")
# el1=Electronics("iphone9",1000,50000,"brand new iphone")
# cl1=Clothes("t-shirt",100,300,"casual",50)
# i.print_info()
# storage=Store()
# storage.add_item(i,20)
# storage.add_item(el1,30)
# storage.add_item(cl1,200)
# storage.print_balance()

item1 = Food("sugar",100,200,"just sugar")
item2 = Electronics("iphone9",1000,50000,"brand new iphone")
item3 = Clothes("t-shirt",100,300,"casual",50)
item4=Food("sugar#2",100,200,"just another sugar")


my_store = Store()
my_store.add_item(item1, 100)
my_store.add_item(item2, 200)
my_store.add_item(item3, 300)
my_store.add_item(item4, 300)
# my_store.add_item([item1,100],[item2,200],[item3,300],[item4,300])


invoice2 = SaleInvoice(my_store)
invoice2.add_item(item1, 5)
invoice2.accept()
invoice1 = SaleInvoice(my_store)
invoice1.add_item(item1, 10)
invoice1.add_item(item2, 10)
invoice1.add_item(item2, 5)
invoice1.add_item(item3, 10)
print(invoice1)
print(invoice2)
invoice1.accept()

my_store.print_balance()
invoice1.cancel()
invoice2.cancel()
my_store.print_balance()

journal = InvoiceJournal()
journal.add_invoice(invoice1)
journal.remove_invoice(invoice1)
journal.add_invoice(invoice2)


report = Report(journal, my_store)
report.print_profit_by_item()
report.print_balance(my_store)
print("*"*60)
invcs = journal.get_invoices(datetime.datetime(2017, 8, 25, 23, 59, 59, 999999),
                             datetime.datetime(2017, 8, 26, 23, 59, 59, 999999))
print(invcs[0])
