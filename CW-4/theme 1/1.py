name = input("Name: ")
age = input("Age: ")
city = input("City: ")
sex = input("he/she: ")
if sex == "he":
    print(f"This is {name}.\nHe is {age} years old.\nHe lives in {city}.")
elif sex == "she":
    print(f"This is {name}.\nShe is {age} years old.\nShe lives in {city}.")
else:
    print("error")
    