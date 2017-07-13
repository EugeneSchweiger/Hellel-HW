print("___________________________________")
print("Task9")
print("___________________________________")
print("Input text block")
txt1=input()
print("You have entered:", txt1)
txt2 = txt1.split(" ")
txt3=txt2.pop(1)
txt2.insert(1,txt3.upper())
str=" ".join(txt2)
print("Result of this task is:" ,str) #И вообще я ленивый и не буду ничего переделывать
#Да,можно было бы конечно выделить второй элемент списка,создать усливие заммены всех
#букв с прописных на заглавные по номерам юникода,но зачем?!
#Всё и так работает :-)
