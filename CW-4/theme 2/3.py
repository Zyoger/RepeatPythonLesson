c = (2, 123.4567, 10000, 12345.67)
print("File_00{}:\t{:6.2f},\t{:6.2e},\t{:6.2e}".format(c[0], c[1], c[2], c[3]))
template = "File_00{}:\t{:.2f},\t{:.2e},\t{:.2e}"
print(template.format(*c))
