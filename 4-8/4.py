"""
Дан словарь {‘class’: {‘student’: {‘name’: ‘Mike’, ‘marks’: {‘physics’: 70, ‘history’: 80}}}}.
Выведите на экран имя студента и его оценку по истории.
"""
s = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
print(((s.get("class")).get("student")).get("name"))
print((((s.get("class")).get("student")).get("marks")).get("history"))
