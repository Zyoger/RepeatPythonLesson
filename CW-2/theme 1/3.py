line = [10, 20, 30, 4, 5, 6, 2, 8, 9]
average = 0
min_element = min(line)
max_element = max(line)
number_elements = line.index(max_element) - line.index(min_element) - 1
if line.index(min_element) < line.index(max_element):
    average = (sum(line[line.index(min_element)+1:line.index(max_element)]))/number_elements
    print(average)
else:
    average = (min_element + max_element)/2
    line[line.index(max_element)] = line[line.index(min_element)] = average

print(line)
