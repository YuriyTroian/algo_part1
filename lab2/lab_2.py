import math as m
#tabl1
x=1
while x<=10:
    if x<3:
        func1=m.sqrt(x**4+m.log(x))
        print("Функція №1:", func1)
    elif 3<=x<6:
        func2=abs(m.log(x))**5
        print("Функція №2:", func2)
    elif x>=6:
        func3=(m.cos(x))**x
        print("Функція №3:", func3)
    x+=0.15


#tabl2
y=-0.05
while y<=1:
    k=1
    y += 0.05
    sum_value = (k*(y)**2)*m.sin(k*y)
    print(k, round(y,2), y + sum_value)

    while sum_value>10**(-5):
        k+=1
        sum_value=(k*(y)**2)*m.sin(k*y)
        print(k, round(y,2), y + sum_value)




















