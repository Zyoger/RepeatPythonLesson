matrix = []
with open("matrix.txt", "r") as file:
    for i in file.readlines():
        matrix.append(list(map(int, i.split())))
print(matrix)


def get_max_min_elem_index(mat, mode=True):
    max_index = [0, 0]
    min_index = [0, 0]
    max_elem = mat[0][0]
    min_elem = mat[0][0]
    for k in range(len(mat)):
        for m in range(len(mat[k])):
            if mat[k][m] > max_elem:
                max_elem = mat[k][m]
                max_index[0], max_index[1] = k, m
            elif mat[k][m] < min_elem:
                min_elem = mat[k][m]
                min_index[0], min_index[1] = k, m
    if mode:
        return max_index
    else:
        return min_index


def check_prime_number(num):
    for j in range(2, num - 1):
        if num % j == 0:
            return False
    return True


def get_max_prime_number_index(mat):
    index = [0, 0]
    max_prime_number = 0
    for l in range(len(mat)):
        for m in range(len(mat[l])):
            if check_prime_number(mat[l][m]) and mat[l][m] > max_prime_number:
                max_prime_number = mat[l][m]
                index[0], index[1] = l, m
    return index


def get_str(x):
    x = map(str, x)
    return " ".join(x)


k_prime, l_prime = get_max_prime_number_index(matrix)
k_min, l_min = get_max_min_elem_index(matrix, mode=False)
matrix[k_prime][l_prime] = matrix[k_min][l_min]
print(matrix)
k_prime, l_prime = get_max_prime_number_index(matrix)
k_max, l_max = get_max_min_elem_index(matrix)
matrix[k_prime][l_prime] = matrix[k_max][l_max]
print(matrix)


with open("result.txt", "w") as new_file:
    for i in matrix:
        new_file.writelines(get_str(i)+"\n")
    print("Done")
