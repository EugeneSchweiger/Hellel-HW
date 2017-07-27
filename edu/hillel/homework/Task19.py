# res = 0
# b=range(0,10**6)
# for i in b:
#     res= (3**i)+res
#     if res>10**6:
#         break
# print(res)


result = 0
sum_of_results=0
i=0
while True:
    result = (3 ** i)
    i=i+1
    if result<10**6:
        sum_of_results=sum_of_results+result
    if result>10**6:
        break
print(sum_of_results)


