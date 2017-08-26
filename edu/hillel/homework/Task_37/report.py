
from edu.hillel.homework.Task_37.invoice_journal import InvoiceJournal
from edu.hillel.homework.Task_37.sale_invoice import SaleInvoice
from edu.hillel.homework.Task_37.item import Item
from edu.hillel.homework.Task_37.store import Store


class Report(object):

    #----------------------------------------------------------------
    def __init__(self, journal, store):
        self.journal = journal
        self.store = store

    def report_format(self, name,value):
        name_format = name + Item._DELIM
        return Item._FORMAT % (name_format, value)

    #----------------------------------------------------------------
    def print_profit_by_item(self, date1=None, date2=None):

        items_profit = {}
        for invoice in self.journal.get_invoices(date1, date2):
            for record in invoice:
                profit = record.qty*(record.item.sale_price-record.item.purchase_price)
                items_profit[record.item] = items_profit.get(record.item, 0) + profit

        print("\nProfit by item:")
        for item in sorted(items_profit, key=items_profit.get):
            print(self.report_format(item.name, items_profit[item]))

    # ----------------------------------------------------------------
    def print_profit_by_date(self, date1, date2):
        items_profit = {}
        for invoice in self.journal.get_invoices(date1, date2):
            for record in invoice:
                profit = record.qty * (record.item.sale_price - record.item.purchase_price)
                items_profit[record.item] = items_profit.get(record.item, 0) + profit

        print("\nProfit by item:")
        print("between %s and %s"%(date1,date2))
        for item in sorted(items_profit, key=items_profit.get):
            print(self.report_format(item.name, items_profit[item]))

    # ----------------------------------------------------------------
    def print_gross_by_item(self, date1=None, date2=None):

        items_gross = {}
        for invoice in self.journal.get_invoices(date1, date2):
            for record in invoice:
                gross = record.qty*(record.item.sale_price)
                items_gross[record.item] = items_gross.get(record.item, 0) + gross

        print("\nGross by item:")
        for item in sorted(items_gross, key=items_gross.get):
            print(self.report_format(item.name, items_gross[item]))

    # ----------------------------------------------------------------
    def print_gross_by_date(self, date1=None, date2=None):
        items_gross = {}
        for invoice in self.journal.get_invoices(date1, date2):
            for record in invoice:
                gross = record.qty*(record.item.sale_price)
                items_gross[record.item] = items_gross.get(record.item, 0) + gross

        print("\nGross by item:")
        print("between %s and %s"%(date1,date2))
        for item in sorted(items_gross, key=items_gross.get):
            print(self.report_format(item.name, items_gross[item]))

    # ----------------------------------------------------------------
    def print_balance(self, store):
        return store.print_balance()