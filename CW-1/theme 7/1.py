s = "All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; " \
    "and one man in his time plays many parts."
s = s.lower()
print(s)
new_s = set(s)
print(new_s)
new_s = sorted(new_s)
print(new_s)
print(len(new_s))
print(new_s[0])
print(new_s[-1])
print(max(new_s))
