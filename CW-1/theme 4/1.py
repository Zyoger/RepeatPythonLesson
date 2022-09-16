lis = ["abc", "xyz", "aba", "1221"]
print(len(lis[0]) > 2)
print(len(lis[1]) > 2)
print(len(lis[2]) > 2)
print(len(lis[3]) > 2)
l0 = list(lis[0])
l1 = list(lis[1])
l2 = list(lis[2])
l3 = list(lis[3])
print(l0[0] == l0[len(l0)-1])
print(l1[0] == l1[len(l1)-1])
print(l2[0] == l2[len(l2)-1])
print(l3[0] == l3[len(l3)-1])

