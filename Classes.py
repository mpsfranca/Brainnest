# I still need to do three tasks: -> Countdown App
#                                 -> Weather App
#                                 -> Personal Budgeting App
# This python file was created to store any loose code I've had to do.

# def feeling_func():
#     times = ["morning","afternoon","evening"]
#     for i in range(len(times)):
#         print(f"Good {times[i]}")
#         feeling = input("How are you feeling?\n")
#         print(f"I am happy to hear that you are feeling {feeling}.")

# feeling_func()

# def get_access():
#     name = password = ""
#     while name != "Matheus" or password != "password":
#         if name != "Matheus":
#             name = input("Type in your name:\n")
#         if name == "Matheus" and password != "password":
#             password = input("Type in your password:\n")
#     print("Access granted!")

# get_access()

# from statistics import mean

# def get_num():
#     inp = ""
#     total = []

#     while True:
#         try:
#             inp = input("Enter a number:\n")
#             if inp == "done":
#                 break
#             else:
#                 total.append(int(inp))
#         except:
#             print("Invalid input.")
    
#     print(f"{sum(total)} {len(total)} {mean(total)}")

# def get_num_max_min():
#     inp = ""
#     total = []

#     while True:
#         try:
#             inp = input("Enter a number:\n")
#             if inp == "done":
#                 break
#             else:
#                 total.append(int(inp))
#         except:
#             print("Invalid input.")
#     print(f"Max:{max(total)}\nMin:{min(total)}")

# get_num_max_min()

# def most_common(t):
#     occurences = {}
#     for element in t:
#         if element not in occurences:
#             occurences[element] = 1
#         else:
#             occurences[element] += 1
#     return list(occurences.keys())[list(occurences.values()).index(max(occurences.values()))]

# t = ("a","b","c","a","a","c","c","c","c","b")
# print(most_common(t))

# def palindrome_checker(t):
#     return t == t[::-1]

# print(palindrome_checker(("m","a","d","a","m")))

# def most_common(t):
#     occurences = {}
#     for element in t:
#         if element not in occurences:
#             occurences[element] = 1
#         else:
#             occurences[element] += 1
#     return occurences

# t = ("a","b","c","a","a","c","c","c","c","b")
# print(most_common(t))

# def get_even(t):
#     result = []
#     for element in t:
#         if element % 2 == 0:
#             result.append(element)
#     result = tuple(result)
#     return result

# t = (1,2,3,4,5,6,7,8,9,10)
# print(get_even(t))

# def repeated(t):
#     seen = []
#     result = []
#     for element in t:
#         if element not in seen:
#             seen.append(element)
#         else:
#             if element not in result:
#                 result.append(element)
#     return result

# t = (1,2,3,1,1,4,3,2,1)
# print(repeated(t))

# def get_senders():
#     FILENAME = "mbox-short.txt"
#     senders = []
#     try:
#         with open(FILENAME,"r") as rf:
#             for line in rf.readlines():
#                 if line.startswith("From"):
#                     splitted_line = line.split(" ")
#                     if len(splitted_line) > 3:
#                         senders.append(line.split(" ")[1])
#         for sender in senders:
#             print(f"Sender: {sender}")
#         print(f"Total number of lines: {len(senders)}")
#     except FileNotFoundError as fnfe:
#         print(fnfe)

# get_senders()

# def get_days():
#     FILENAME = "mbox-short.txt"
#     days_dict = {}
#     try:
#         with open(FILENAME, "r") as rf:
#             for line in rf.readlines():
#                 if line.startswith("From"):
#                     splitted_line = line.split(" ")
#                     # Minimum len of the line containing sender and week day
#                     if len(splitted_line) > 3:
#                         if splitted_line[2] not in days_dict:
#                             days_dict[splitted_line[2]] = 1
#                         else:
#                             days_dict[splitted_line[2]] += 1
#             return days_dict
#     except FileNotFoundError as fnfe:
#         print(fnfe)

# print(get_days())

# def quantity_senders():
#     FILENAME = "mbox-short.txt"
#     d = dict()
#     try:
#         with open(FILENAME) as rf:
#             for line in rf.readlines():
#                 if line.startswith("From "):
#                     aux = line.split(" ")[1]
#                     if aux not in d:
#                         d[aux] = 1
#                     else:
#                         d[aux] += 1
#         return d
#     except FileNotFoundError as e:
#         print(e)

# print(quantity_senders())

# a = {1,2,3}
# b = {0,2,3}
# print(a.symmetric_difference(b))

# def is_prime(n):
#     for i in range(2,n):
#         if n % i == 0 or n == 1:
#             return False
#     return n != 1

# def prime_set(l):
#     prime = set()
#     for number in l:
#         if is_prime(number):
#             prime.add(number)
#     return prime
# l = [1,2,3,4,5,6,7,8,9,10]
# print(prime_set(l))

# def decor1(func):
#     def inner():
#         x = func()
#         return x*x
#     return inner

# def decor2(func):
#     def inner():
#         x = func()
#         return 2*x
#     return inner

# @decor1
# @decor2
# def num():
#     return 2

# @decor2
# @decor1
# def num2():
#     return 2

# print(num())
# print(num2())

# def greet(func):
#     def aux(*args):
#         print("Inside aux")
#         result = func(*args)
#         return result
#     return aux

# @greet
# def say_hello():
#     print("Hello")

# say_hello()

# import random
# def authorize(func):
#     def wrapper(*args):
#         if check_authorization():
#             return func(*args)
#         return "Unauthorized access"
#     return wrapper

# def check_authorization():
#     return random.choice([True,False])

# @authorize
# def secret_data():
#     return "This is confidential data"

# print(secret_data())

# def validate(func):
#     def wrapper(*args):
#         for arg in args:
#             if not isinstance(arg,int):
#                 return "Invalid type"
#         return func(*args)
#     return wrapper

# @validate
# def add(a,b):
#     return a+b

# print(add(1,2))
# print(add(0,"a"))

# def is_prime(n):
#     for i in range(2,n):
#         if n % i == 0 or n == 1:
#             return False
#     return n != 1

# def ten_primes():
#     count = 0
#     num = 2
#     while count < 10:
#         if is_prime(num):
#             count += 1
#             yield num
#         num += 1

# print(list(ten_primes()))

# def exists_in_file(path,word):
#     with open(path) as rf:
#         for line in rf.readlines():
#             if word in line:
#                 yield line
    
# print(list(exists_in_file("mbox-short.txt","From")))

# lists = [[1,2,3],[4,5,6],[7,8,9]]

# result = [num for inner in lists for num in inner]
# print(result)

# ld = [{"key1":"value1","key2":"value2","key3":"value3"},{"key2":"value2"},{"key3":"value3","key5":"value5"}]

# key3 = [(key,value) for d in ld for key,value in d.items() if key == "key3"]
# print(key3)

# list1 = [1,2,3]
# list2 = ["a","b","c"]

# cartesian = [(a,b) for a in list1 for b in list2]
# print(cartesian)

# import re
# pattern = re.compile("^\d{2}/{1}\d{2}/{1}\d{4}$")
# print(pattern.search("01/01/2021"))

# import re
# pattern = re.compile("^\d{3}-\d{3}-\d{4}$")
# print(pattern.search("123-456-7890"))

# import re
# pattern = re.compile("^\w+\s{1}\w+$")
# print(pattern.search("hello world"))

# import re
# pattern = re.compile("^\d+\.{1}\d{2}$")
# print(pattern.search("123.11"))

# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"Hi, my name is {self.name} and I'm {self.age} years old."

#     def greet(self):
#         return f"Hello, nice to meet you!!"

# class Student(Person):
#     def __init__(self,name,age,university):
#         super().__init__(name,age)
#         self.university = university

#     def introduce(self):
#         return f"{super().introduce()} I study at {self.university}."

# p = Person("João",22)
# print(p.introduce())

# s = Student("Matheus",23,"UFBA")
# print(s.introduce())

# class Pet:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         return "I'm a Pet!!"

# class Dog(Pet):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return "I'm a dog!!"

# class Cat(Pet):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return "I'm a cat!!"

# p = Pet("Spike")
# print(p.speak())

# d = Dog("Spot")
# print(d.speak())

# c = Cat("Whiskers")
# print(c.speak())

# class BankAccount:
#     bank_name = "Millennium"

#     def __init__(self,account_holder_name,balance=0.0):
#         self.account_holder_name = account_holder_name
#         self.__balance = balance

#     def deposit(self,ammount):
#         self.__balance += ammount

#     def withdraw(self,ammount):
#         self.__balance -= ammount

#     def get_balance(self):
#         return self.__balance

#     def __str__(self):
#         return f"Account Holder: {self.account_holder_name}; Balance: {self.__balance}; Bank Name: {self.bank_name}"

# ba1 = BankAccount("João",1000)
# print(ba1)
# ba1.deposit(100)
# print(ba1)
# ba1.withdraw(350)
# print(ba1)
# ba2 = BankAccount("Matheus",500)
# print(ba2)

# l = [-1,0,2,5,0,-7]
# result = list(filter(lambda n: n > 0,l))
# print(result)

# d = [{"name":"Bruno","age":40},{"name":"Matheus","age":23},{"name":"João","age":22}]
# result = list(sorted(d,key=lambda x: x["age"]))
# print(result)

# string = "it was a pleasure doing this course!"

# result = " ".join(map(lambda x: x.capitalize(), string.split()))

# print(result)
