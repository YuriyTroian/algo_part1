list1 = [1, 7, 4, 5]
list2 = [3, 2, 4, 5, 6]
list3 = []
def differ():
    for el1 in list1:
        for el2 in list2:
            if list1.index(el1) == list2.index(el2):
                list3.append(el1 - el2)
    return list3
print(differ())
print("Done")

a1 = [1, 2, 3, 4, 5]
b1 = [3, 4]
a2 = [1, 2, 3, 4]
b2 = [4, 3, 5]

def func2(a, b):
    a_result = []
    b_result = b.copy()
    i = 0
    for el in a:
        if i < len(b_result) and el == b_result[i]:
            i += 1
        else:
            a_result.append(el)

    b_result = b_result[i:]
    return a_result, b_result

a_res1, b_res1 = func2(a1, b1)
a_res2, b_res2 = func2(a2, b2)

print("Список a1:", a_res1)
print("Список b1:", b_res1)
print("Список a2:", a_res2)
print("Список b2:", b_res2)

