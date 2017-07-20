string=input("enter text")
def reverse_no_slice_and_cycle(str):
    lst=list(str)
    lst.reverse()
    reverced="".join(lst)
    return reverced
print(reverse_no_slice_and_cycle(string))