def print_information(**kwargs):
    """***"""
    if "name" not in kwargs or "lastname" not in kwargs:
        print("Enter name!!!")
        return None
    print("Name:", kwargs["name"])
    print("Last Name: ", kwargs["lastname"])
    if len(kwargs) > 2:
        print()
        keys = list(kwargs.keys())[::2]
        keys.sort()
        for key in keys:
            print(key, ":", kwargs[key])
    print("-"*30)


print_information(name="Egor", lastname="Tarakanov", age="35", phone="891787575")
