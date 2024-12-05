lady = {"name": "Yadanar", "age": 30} 

print(lady) # {'name': 'Yadanar', 'age': 30}
print(lady.get('name')) # Yadanar 
print(lady.get('gender')) # None 
print(lady.get('gender','Not Defined')) # Not Defined

print(lady.keys()) # dict_keys(['name', 'age'])
print(list(lady.keys())) # ['name', 'age']
print(list(lady.keys())[0]) # name
print(list(lady.keys())[1]) # age 

print(lady.values()) # dict_values(['Yadanar', 30])
print(list(lady.values())) # ['Yadanar', 30]
print(list(lady.values())[0]) # Yadanar
print(list(lady.values())[1]) # 30 

print(lady.items()) # dict_items([('name', 'Yadanar'), ('age', 30)])
print(list(lady.items())) # [('name', 'Yadanar'), ('age', 30)]
print(list(lady.items())[0]) # ('name', 'Yadanar')
print(list(lady.items())[1]) # ('age', 30)
print(list(lady.items())[0][0]) # name
print(list(lady.items())[0][1]) # Yadanar
print(list(lady.items())[1][0]) # age
print(list(lady.items())[1][1]) # 30

lady.update({"age": 20})
print(lady) # {'name': 'Yadanar', 'age': 20}

# delete defined key 
lady.pop('age')
print(lady) # {'name': 'Yadanar'}

lady.clear() 
print(lady) # {}

# boy = {'name': 'Zaw Zaw', 'city': 'Yangon'} 
# boy.pop() 
# print(boy) # error 

girl = {'name': 'Yadanar', 'age': 30, 'city': "Mawlamyine"}
# delete last item 
item = girl.popitem()
print(item) # ('city', 'Mawlamyine')
print(item[0]) # city
print(item[1]) # Mawlamyine

print(girl) # {'name': 'Yadanar', 'age': 30}

woman = girl.copy() 
print(woman) # {'name': 'Yadanar', 'age': 30}




