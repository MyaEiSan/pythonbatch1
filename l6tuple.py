
# List Vs Tuple 
# 1. Mutablity . mutable (changable) and immutable (not changable)
# 2 Performance 
    # list: Generally slower than tuples 
    # tuple: Faster and more-efficient . because they are immutable and have a fixed size

# 3. Use Cases 
     # list: need to change, user lists, shopping carts 
     # tuple: geographic coordinates, settings, database records 
# 4. Methods 
    # list: many built-in methods for modifying list. .append(), .remove(), .pop(), .sort() 
    # tuple: fewer built-in methods. cannot be modified. only can use .count(), .index()



print(type([1,2,3])) #<class 'list'>
print(type((1,2,3))) #<class 'tuple'>

# Create a tuple with parentheses 
tuple1 = (1,2,3,4,5) 

# Create a tuple without parentheses 
tuple2 = 10,20,30,40,50 

print(tuple1) #(1, 2, 3, 4, 5)
print(tuple2) #(10, 20, 30, 40, 50)

print(tuple1[0])  #1
print(tuple1[2])  #3

print(tuple2[3])  #30
print(tuple2[4])  #50


# tuple1[0] = 100  #TypeError: 'tuple' object does not support item assignment
# tuple2[0] = 100  #TypeError: 'tuple' object does not support item assignment

print(tuple1.count(1)) # 1
print(tuple1.count(10)) # 0

print(tuple2.count(20)) # 1
print(tuple2.count(100)) # 0


print(tuple1.index(4)) # 3

print(tuple2.index(20)) #1 
print(tuple2.index(50)) #4 

# Tuple Unpacking 
students = ("aung aung", "su su") 

boy,girl = students 
print(boy) #aung aung
print(girl) #su su

# Nested Tuples 
numbers = (1,(2,3),(4,5,6,7)) 
print(numbers) #(1, (2, 3), (4, 5, 6, 7))
print(numbers[1]) # (2, 3)
print(numbers[2][3]) #7

