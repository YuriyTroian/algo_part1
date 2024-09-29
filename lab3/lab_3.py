list1 = [3, 4, 5, 6, 7, 8]
list2 = [1, 5, 7, 4, 6]

def differ():
    return [el1-el2 for el1 in list1 for el2 in list2 if list1.index(el1) == list2.index(el2)]
print(differ())


def func2():
    for el1 in list1[:]:
        if el1 in list2:
            list1.remove(el1)
            list2.remove(el1)
    print(list1)
    print(list2)
func2()