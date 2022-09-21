s = "Th$e *ly-ri cs; i!s >no>t *th&at$ p=oo+r!$"
arr = bytearray(s.encode())
print(arr)
del arr[2::3]
print(arr)
