maths_winners = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
physics_winners = {"Максим", "Матвей", "Александр"}
maths_winners.remove("Максим")
maths_winners.remove("Наталья")
all_winners = physics_winners | maths_winners
print(all_winners)
top_winners = maths_winners & physics_winners
print(top_winners)
physics_winners.clear()
print(physics_winners)
