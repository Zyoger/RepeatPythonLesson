"""
Известно, что в классе 5 учеников (Костя, Маша, Данила, Ваня и Егор) увлекаются историей, и 7 учеников
 (Света, Ваня, Сергей, Марина, Костя, Маша и Антон) интересуются биологией. Кроме этого 2 ученика
  (Антон и Николай) активно занимаются спортом. Найдите, кто из учеников увлекается и историей, и
   биологией одновременно? Есть ли в классе ученики, которые преуспели во всех трех дисциплинах? Кто
    из спортсменов также интересуется биологией? Сколько всего учеников занято на дополнительных
    занятиях? Выведите их имена в алфавитном порядке.

"""
history = {"Костя", "Маша", "Данила", "Ваня", "Егор"}
biology = {"Света", "Ваня", "Сергей", "Марина", "Костя", "Маша", "Артур"}
sport = {"Антон", "Николай"}
HiB = history.intersection(biology)
print(HiB)
HiBiS = history.intersection(sport, biology)
print(HiBiS)
SiB = sport.intersection(biology)
print(SiB)
uni = history.union(biology, sport)
print(sorted(uni))


