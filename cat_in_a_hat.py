cats = [0] * 100
round_number = 1
for i in range(0, len(cats), round_number):
    if cats[i] == 0:
        cats[i] += 1
    else:
        continue
    round_number+=1
print([cat for cat in cats if cat == 1])



