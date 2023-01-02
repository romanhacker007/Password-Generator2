import random as r
import time as t
import os

pass_gen = "1234567890"
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

os.system("clear")

otvet = input('В пароле будут символы и буквы(д/н):')

gen = int(input("Количество вариантов пароля:"))
leng = int(input("длина пароля:"))
t.sleep(2)
print(f"PassGen вариантов: {gen}")
print(f"PassGen длина: {leng}")
t.sleep(5)
os.system("clear")

if otvet == "д":
    for n in range(gen):
        password = ' '
        for i in range(leng):
            password += r.choice(chars)
    
        t.perf_counter_ns()
        print(password)
        
if otvet =="н":
    for n in range(gen):
        password = ' '
        for i in range(leng):
            password += r.choice(pass_gen)
    
        t.perf_counter_ns()
        print(password)
        
