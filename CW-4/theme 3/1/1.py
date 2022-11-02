path_file = "students.txt"


def file_read(path=path_file):
    list_students = []
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        name, surname = line.split(" ")
        list_students.append({"name": name, "surname": surname.strip()})
    return list_students


def file_write(students, path=path_file):
    students_sorted = sorted(students, key=lambda st: st["name"])
    with open(path, "w", encoding="utf-8") as file:
        for i in students_sorted:
            file.write(str(f"{i['name']} {i['surname']}\n"))


def add_new_student(name, surname):
    students = file_read()
    students.append({"name": name, "surname": surname.strip()})
    file_write(students)


def find_student(surname, name=None):
    students = file_read()
    if name is None:
        pass
    else:
        pass


# add_new_student(name="Слава", surname="Боровиков")
