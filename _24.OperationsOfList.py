#Working With List
numbers=[5,2,1,5,7,4]

#Add Element At Last Index
numbers.append(20)
print(numbers)

#Add Element At Specific Index Exisiting Element Doesn't Remove It Shifts Postions.
numbers.insert(0,10)
print(numbers)

#Remove Element Value That is Provided In Parameter
numbers.remove(5)
print(numbers)

#Remove Element From Last Postions
numbers.pop()
print(numbers)

#Find Element Index That Is Provided By Parameter
print(numbers.index(5))

#Count The Element Occurences That Value Is Provided By Parameter
print(numbers.count(5))

#Sort The List In Asscending Order
numbers.sort()
print(numbers)

#Sorth The List In Descending Order
numbers.reverse()
print(numbers)

#Copy From One Array To Another.
numbers2=numbers.copy()
numbers2.append(20)
print(numbers2)
