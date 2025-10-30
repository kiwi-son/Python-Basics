for i in range(1, 15):
    print(i)
    if i == 10:
        break
for i in range(11, 16):
    if i == 13:
        continue # skip the rest of the code and go to next iteration
    print(i)

for i in range(16, 21):
    print(i)
    if i == 18:
        pass # do nothing and continue