#Integer
customer_age = 90
print("Integer: ", customer_age)

#Float
pie = 3.142
print("Float: ", pie)

#Character
char = 'A'
print("Character: ", char)

#Boolean (true or false)
isTrue = True
print("Boolean: ", isTrue)

isFalse = False
print("Boolean: ", isFalse)

#list
fruits = [10, 20, 40, 50]
print("Fruits: ", fruits)

fruits.append(50)
fruits.append(60)
fruits[0] = 250
fruits.remove(250)
print("Fruits Mutable: ", fruits)

#Tuple
my_tuple = (10, 20, 30)

#Dictionary
my_dictionary = {"name": "alinafe", "course": "python", "age": 1}
print("Dictionary: ", my_dictionary)

#Set
my_set = {1, 2, 3}
print("Set: ", my_set)

#None
my_results = None
print("None: ", my_results)

#bytes
a = b"Hellow World"
print("Bytes: ", a[1])

#Bytearray
my_byte_array = bytearray(a)

#Memoryview
memory_view = memoryview(my_byte_array)