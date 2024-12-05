# =>Type of Argument in Python 
# Positional Arguments 
# Keyword Arguments 
# Default Arguments 
# Variable-length Arguments (*args) (Non-keyword Variable Arguments)
# Variable-length Arguments (**keywordargs) (Keyword Variable Arguments)



# Positional Arguments  (Parameter မှာ position လွဲပြီးပေးလို့မရဘူး)
def greeting(name, age): 
    print(f"Hello friend! my name is {name}, i am {age} years old.")

greeting("Su Su",23) # Hello friend! my name is Su Su, i am 23 years old. 
greeting(25, "Nu Nu") # Hello friend! my name is 25, i am Nu Nu years old.


# Keyword Arguments (Parameter ပေးတဲ့အခါ keyword သတ်မှတ်ပြီးပေးတာဖြစ်လို့ သက်ဆိုင်ရာအတိုင်းအလုပ်လုပ်သွားမှာ လွဲတာမျိုးတွေမရှိတော့ဘူး)

def hifi(name,age): 
    print(f"Hello friend! my name is {name}, i am {age} years old.")

hifi(name="Min Min",age=25) # Hello friend! my name is Min Min, i am 25 years old.
hifi(age=25,name="Min Min") # Hello friend! my name is Min Min, i am 25 years old.


# Default Arguments 
def hime(name,age=18):
    print(f"Hello friend! my name is {name}, i am {age} years old.")

hime("Yamin") # Hello friend! my name is Yamin, i am 18 years old.
hime("Thuzar",20) # Hello friend! my name is Thuzar, i am 20 years old.



# Variable-length Arguments (*args) (Non-keyword Variable Arguments)
def boys(*args): 
    print(args) 

boys("aung aung") # ('aung aung',)
boys("aung aung","kyaw kyaw") # ('aung aung', 'kyaw kyaw')
boys("aung aung","kyaw kyaw","zaw zaw","tun tun") # ('aung aung', 'kyaw kyaw', 'zaw zaw', 'tun tun')
# boys("aung aung",args="kyaw kyaw") # error when including Keyword Arguments 


# Note:: Non-keyword and Keyword Variable arguments function name တွေကို plural ပေးသင့်တယ် arguments က တစ်ခုထပ်ပိုလို့ 

def sumresults(*numbers): 
    total = sum(numbers) 
    print(f"Sum result is {total}")

sumresults(1,2,3) # Sum result is 6
sumresults(10,20,30,40,50) # Sum result is 150


def myfunone(num,*nums): 
    print(num) # 1
    print(nums) # (2, 3, 4, 5)

myfunone(1,2,3,4,5)

# ERROR 
# def myfuntwo(*nums,num): 
#     print(num) # 1
#     print(nums) # (2, 3, 4, 5)

# myfuntwo(1,2,3,4,5)


# Variable-length Arguments (**keywordargs) (Keyword Variable Arguments)

def personinfos(**kwargs): 
    for key,value in kwargs.items(): 
        print(f"{key} = {value}")

personinfos(name="Thuzar",age=25,city="Mandalay")
personinfos(name="Kaung Kaung",professional="Engineer",city="Yangon")


# Exercise ( Combining Different Type of Arguments )

def emailsender(address, *messages,**files): 
    print(f"Address = {address}")
    if messages: 
        for message in messages: 
            print(f"Message = {message}")
    if files: 
        for key, value in files.items(): 
            print(f"{key} = {value}") 

emailsender("dataland@gmail.com","Hello admin","i want to record vdo records",lesson="Phtyon B1",classdate="25/Nov/2024")

def studentinfos(name,age=18,*hobbies,**infos): 
    print(f"Name = {name}") 
    print(f"Age = {age}")
    if hobbies: 
        for hobby in hobbies: 
            print(f"Hobbies = {hobby}") 
    if infos: 
        for key, value in infos.items(): 
            print(f"{key} = {value}") 

studentinfos("Nandar") 
studentinfos("Maung Maumg",25) 
studentinfos("Aung Kyaw",25,'reading','travelling') 
studentinfos("Kyaw Kyaw",25,'reading','travelling',city="Bago",profession="Engineer")


def staffinfos(name,age=18,*hobbies,**infos): 
    print(f"Name = {name}") 
    print(f"Age = {age}")
    if hobbies: 
        # print(f"Hobbies = {hobbies}") # Hobbies = ('reading', 'travelling')
        print(f"Hobbies = {','.join(hobbies)}") # Hobbies = reading,travelling
    if infos: 
        for key, value in infos.items(): 
            print(f"{key} = {value}") 

staffinfos("Ni Lar",20,'reading','travelling',city="Yangon",profession="Engineer")
