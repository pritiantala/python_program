from itertools import count
unique_list=[]
count=0
for i in range(12):
    list=int(input("enter number:"))
    if count<=12:
        if list not in unique_list:
            unique_list.append(list)
            count+=1
print(unique_list)
"""

a=[]
print(a)
status = True
count=1
while status:
    num = int(input('enter number: '))
    if count<=12:
        #a.append(num) 
        if num not in a:
            a.append(num) 
            count+=1
    else:
        status = False
        
print(a)"""