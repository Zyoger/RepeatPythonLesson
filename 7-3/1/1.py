open_file = open("nums.txt", "r+")
line = open_file.read()
line = list(line.split())
line = list(map(int, line))
line = sorted(line)


def get_str(x):
    x = map(str, x)
    return " ".join(x)


open_file.write(get_str(line))
open_file.close()
