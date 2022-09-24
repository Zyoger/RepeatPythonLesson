line = "Python else loop"
letters = "aoe"
for i in range(0, len(line)):
    if line[i] == "l" and letters.count(line[i+1]):
        print(line[i], " ", line[i+1])
        break
else:
    print("Искомые комбинации не найдены")
