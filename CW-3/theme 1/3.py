"""3. Написать функцию, которая принимает в качестве аргумента строку и подсчитывает в ней количество символов
 в верхнем и нижнем регистре."""

line = "Каждый подход, как это и водится, имеет свои плюсы и минусы. Где-то можно выиграть в оптимизации, но потерять" \
       " в живых читателях. Где-то можно приобрести живых читателей, но придется жертвовать показателями и," \
       " возможно, по этой причине отставать от конкурентов."

template_upper = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
                  "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
template_lower = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                  "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def get(li):
    """*****"""
    counter_upper = 0
    counter_lower = 0
    for i in li:
        if i.isupper():
            counter_upper += 1
        elif i.islower():
            counter_lower += 1
    return print(f"Upper: {counter_upper}, lower: {counter_lower}")


get(line)