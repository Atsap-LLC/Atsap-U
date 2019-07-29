f = open("totalHRs.txt", "r")
results = [45-int(n) for n in f]

f = open("HRsLeft.txt", "a")
for HR in results:
    f.write(str(HR) + "\n")
f.close()