matrix = [
    [34, -8, 27, 7, 12],
    [-5, 23, 45, 67, -2],
    [13, -12, 34, -3, 25],
    [17, 56, -6, 17, 21,],
    [0, 15, 4, 9, -14]
]

def sort(func):
    def sort_matrix(matrix):
        n1 = len(matrix)
        for row in range(n1):
            n2 = len(matrix[row])
            for run in range(n2-1):
                for el in range(n2-1):
                    if matrix[row][el] > matrix[row][el+1]:
                        matrix[row][el], matrix[row][el+1] = (
                            matrix[row][el+1], matrix[row][el]
                        )
        return func(matrix)

    return sort_matrix



def calculate_fi(matrix):
    num_columns = len(matrix[0])
    fi_values = []
    for col in range(num_columns):
        min_value = matrix[0][col]
        for row in range(1, len(matrix)):
            if matrix[row][col] < min_value:
                min_value = matrix[row][col]
        fi_values.append(min_value)
    return fi_values



def calculate_F(fi_values):
    result = 1
    for value in fi_values:
        result *= value
    return result



@sort
def process_matrix(matrix):
    print("Відсортована матриця:")
    for row in matrix:
        print(row)

    fi_values = calculate_fi(matrix)

    print("\nЗначення fi(aij) для кожного стовпця:")
    print(fi_values)

    F_value = calculate_F(fi_values)

    print("\nЗначення F(fi(aij)):", F_value)

process_matrix(matrix)






















# Повторити сортування для кожного елемента
#         for j in range(0, n - i - 1):  # Перевірити кожну пару елементів
#             print(f"Матриця перед бульбашкою: {matrix}")
#             if matrix[j] > matrix[j + 1]:  # Порівняння поточного і наступного елемента
#                 matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]  # Заміна
#             print(f"Матриця після бульбашки: {matrix}")
#
# sort_matrix(matrix)











#         for j in range((len(matrix))-1):
#             if matrix[i] < matrix[i-1]:
#                 matrix[i], matrix[i-1] = matrix[i-1], matrix[i]
#             print(matrix)
#     # print(matrix)
# sort_matrix(matrix)




