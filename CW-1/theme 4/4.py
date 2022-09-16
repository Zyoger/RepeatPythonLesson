guest = ["Adela", "Fleda", "Goga", "Owen", "May", "Mona", "Gilbert", "Ford"]
n = len(guest)
if guest.index("May") == n/2:
    print("в меру")
elif n/2 < guest.index("May") < n:
    print("Средние")
else:
    print("Последний")

