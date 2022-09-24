names = ["Rose", "Nina", "Phillip", "Alex", "Jimmy", "Max"]
for name in names:
    if len(name) <= 4:
        print("Hello", name)
    if name.count("x"):
        break
