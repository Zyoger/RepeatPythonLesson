"""
Дано два словаря: {‘Ten’: 10, ‘Twenty’: 20, ‘Thirty’: 30} и {‘Thirty’: 30, ‘Forty’: 40, ‘Fifty’: 50}.
Объедините эти словари в один.
"""
s1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
s2 = {"Thirty": 30, "Forty": 40, "Fifty": 50}
s1.update(s2)
print(s1)
