# => Data Containers 

#list
mylist = [1,2,3,4,5] 
print(type(mylist)) # <class 'list'>

# tuple 
mytuple = (1,2,3,4,5)
print(type(mytuple)) # <class 'tuple'>

# dict
mydict = {"a":1, "b":2, "c": 3}
print(type(mydict)) # <class 'dict'> 

# set 
myset = {1,2,3,4,5} 
print(myset) # {1, 2, 3, 4, 5}
print(type(myset)) # <class 'set'>

dict1 = {} 
print(type(dict1)) # <class 'dict'>

set1 = {} 
print(type(set1)) # <class 'dict'>

# create an empty set 
set2 = set() 
print(type(set2)) #<class 'set'>

# list = order list 
# set = unordered list , always dynamic 

colors = {"red","green","blue","white","black"} 
print(colors)

for color in colors: 
    print(color)

print("green" in colors) # True 
print("steelblue" in colors) # False 

fruits = {"apple","orange"} 
print(fruits) # {'apple', 'orange'}

# Adding a Single Element 
fruits.add("cherry") 
print(fruits) # {'cherry', 'orange', 'apple'}

# Adding Multiple Element [] 
fruits.update(["mango","grape"]) 
print(fruits) # {'orange', 'mango', 'apple', 'grape', 'cherry'}

# Remove Elements 
fruits.remove("orange") # if no element exists ! will show an error 
print(fruits) # {'grape', 'mango', 'apple', 'cherry'}

# Remove Elements (using discard())
fruits.discard("red") # if no element exists ! no error 

fruits.discard("apple") 
print(fruits) # {'cherry', 'mango', 'grape'}

# Clear Elements 
fruits.clear() 
print(fruits) # set()

# Frozenset (Immutable of set) 
fornumbers = frozenset([10,20,30,40]) 
# fornumbers.add(50) # error 
# fornumbers.remove(40) #error 
print(fornumbers) # frozenset({40, 10, 20, 30})
print(20 in fornumbers) # True 
print(50 in fornumbers) # False 

set3 = {1,2,3,6,7} 
set4 = {3,4,6,5} 

# Union Combines ( | ) 
print(set3 | set4) # {1, 2, 3, 4, 5, 6, 7}

# Intersection ( & ) 
print(set3 & set4) # {3, 6}

# Difference ( - ) 
print(set3 - set4) # {1, 2, 7}
print(set3.difference(set4)) # {1, 2, 7}

print(set4 - set3) # {4,5} 
print(set4.difference(set3)) # {4,5}

# Symmetric Difference ( ^ ) 
print(set3 ^ set4) # {1, 2, 4, 5, 7}
print(set3.symmetric_difference(set4)) # {1, 2, 4, 5, 7}


# 1ST
