fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange ')
fruits.remove('apple')
fruits.discard('lemon')
fruits.pop()
print(len(fruits))
print(fruits)

A = {1,2,3,4,5,6,9,2,3}
B = {8,9,7,6,5,4,3,2,1}
print(A|B)
print(A-B)
print(A^B)
print(A&B)