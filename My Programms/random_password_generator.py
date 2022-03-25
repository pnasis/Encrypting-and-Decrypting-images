import random 
 
# The sets we are using to generate the password 
lower = "abcdefghijklmnopqrstuvwxyz" 
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
numbers = "0123456789" 
symbols = "[]*/-_$#@!%" 
 
all = lower + upper + numbers + symbols  #Universal Set 
length = 12   #You can change the length of the password. 
password = "".join(random.sample(all, length)) 
print(password)