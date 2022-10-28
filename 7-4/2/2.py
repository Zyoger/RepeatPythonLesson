import os
import os.path

with open("../1/TEST/Test4.txt", "w") as file:
    file.writelines("It just involves finding the python executable and setting it to run as administrator every time."
                    "\n",)
    print("done")

size = os.path.getsize("../1/TEST/Test4.txt")
print(size)
os.truncate("../1/TEST/Test4.txt", round(size*0.1))

with open("../1/TEST/Test4.txt", "r") as file:
    print(file.readlines())
