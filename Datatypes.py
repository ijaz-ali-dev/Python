# Booleans
string = 'this is my string';
print(len(string))

len(string) ==17
if len(string) == 17:
    print("this is vaild string")
else:
    print("this is not vaild string")

# Numbers (int, float, and complex, type(),  isinstance() ,“j” imaginary
num = 2 
print("this is",num,"is type",type(num))
print(" ",num,"", type(num))
numq = 3.0
print("this is second number ",numq," its type", type(numq))
number= 3+5j
print("The number ", number, " is of type", type(number))

# Strings
print (type("python string of the name show in"))
str= "learn pyhton and find the indexing of the string"
first_str = str[0:4]
fst_str = str[4:]
print(fst_str)
print(first_str)
print (str[-2:])

# Bytes
empty_object = bytes(16)
print(type(empty_object))

# Lists
str = [True, False, 1, 1.1, (1+2j), 'Learn', b'Python']
print(str)
str_1 = str[4]
print(str_1);

complex_string = ['Learn', 'Python', '2']
print(complex_string)

print("nesting inside the a list")
nested = [[1,1,1], [2,2,2], [3,3,3]]
for i in nested:
    for number in i:
        print(number, end=" ")

nested =[[1,1,1], [2,2,2]]
for i in nested:
    print( i, end=" ")
    for numner in i:
        print( numner, end=" ")

print("slicing a list")
languages = ['C', 'C++', 'Python', 'Java', 'Go', 'Angular']
print("languages")
print('languages[0:3] = ', languages[0:3])

print ("add the item in the nested list")
languages = ['C', 'C++', 'Python', 'Java', 'Go', 'Angular']
print(languages)
# languages.append('ijaz ali')
L = ['C', 'C++', ['Python'], 'Java', 'Go', 'Angular']
L[2].append('xx')
print(L)
lit=[1,2,4]
lit.append(5)
print(lit)

list = ["ijaz ali", "session", 2, 56]
list.append("string")
# Tuples

# Sets
# Dictionaries

