import math as m
#tabl1
x=1
while x<=10:
    if x<3:
        func1=m.sqrt(x**4+m.log(x))
        print(f"Функція №1:{func1}")
    elif 3<=x<6:
        func2=abs(m.log(x))**5
        print(f"Функція №2:{func2}")
    elif x>=6:
        func3=(m.cos(x))**x
        print(f"Функція №3:{func3}")
    x+=0.15


#tabl2
y=0

while y<=1:
    sum_value = 0
    k = 1
    elem = (k*(y)**2)*m.sin(k*y)
    sum_value += elem
    print(f"Функція k = {k}, y = {round(y, 2)}, elem = {elem}")


    while elem>10**(-5):
        k+=1
        elem = (k*(y)**2)*m.sin(k*y)
        sum_value += elem

        print(f"Функція k = {k}, y = {y}, elem = {elem}")
        print(f"Сума к = {k}, y = {y}, Sum = {y + sum_value}")
    y += 0.05
    y = round(y, 2)
























