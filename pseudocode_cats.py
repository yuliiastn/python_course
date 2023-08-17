Create a list cats with [0] * 100
Introduce a round_number = 1
Loop through the cats in range from 0 till len(cats) using step round_number:
    If cats[i] is 0:
        Change cats[i] to 1
        Otherwise: continue
    Increment the round_number by 1
Print the list cat for cat in cats if cat == 1