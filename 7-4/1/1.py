import os
print(os.getcwd())
os.makedirs("./TEST/A/A1")
os.makedirs("./TEST/A/A2")
os.makedirs("./TEST/C")
os.makedirs("./TEST/B")
with open("./TEST/A/A1/Test1.txt", "w") as file:
    file.write("Test1.txt!!!")
    print("Done")
with open("./TEST/A/A2/Test2.txt", "w") as file:
    file.write("Test2.txt!!!")
    print("Done")
with open("./TEST/B/Test3.txt", "w") as file:
    file.write("Test3.txt!!!")
    print("Done")
with open("./TEST/Test4.txt", "w") as file:
    file.write("Test4.txt!!!\n")
    print("Done")

for root, dirs, files in os.walk("Test", topdown=True):
    print(f"Root: {root}")
    print(f"Subdirs: {dirs}")
    print(f"Files: {files}")
    print("-"*30)
