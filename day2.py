"""year=int(input("enter year:"))
m=year*12
print("month=",m)

month=int(input("enter month:"))
year=month/12
print(year)
"""
#task1
day=int(input("enter number of days:"))
months=day/30
print(months)

#task2
hour=int(input("enter hours:"))
min=hour*60
print(min)

#task3
p=int(input("enter principle amount:"))
n=int(input("enter number of terms:"))
r=int(input("enter rate:"))
I=(p*r*n)/100
print("intrest:",I)

#task4
min=int(input("enter min:"))
hour=min/60
sec=min*60
print("hours:",hour)
print("second:",sec)


#task5
marks=int(input("enter marks:"))
if marks >= 35:
    print("student is pass")
else:
    print("student is fail")

#task6
number=int(input("enter number:"))        
if number > 0:
    print("number is positive")
else:
    print("number is negitive")

#task7
r=int(input("enter radious:"))
pi=3.14
area= pi * r *r
print("area of circle:",area)
