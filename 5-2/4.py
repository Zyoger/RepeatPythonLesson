sw = 600
ps = 450
mp = 400
cash = 1300

if (sw + ps >= 1000 and (sw + ps + (mp*0.7)) < 1300) or (ps + mp >= 1000 and (ps + mp + (sw*0.7)) < 1300) or (sw + mp >= 1000 and (sw + mp + (ps*0.7)) < 1300):
    print("Deal success")
else:
    print("Deal dont success")
