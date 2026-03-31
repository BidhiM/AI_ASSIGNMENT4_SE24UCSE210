from itertools import permutations

def solve_cryptarithm():
    letters = ('S','E','N','D','M','O','R','Y')
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))

        if assign['S'] == 0 or assign['M'] == 0:
            continue

        SEND = 1000*assign['S'] + 100*assign['E'] + 10*assign['N'] + assign['D']
        MORE = 1000*assign['M'] + 100*assign['O'] + 10*assign['R'] + assign['E']
        MONEY = (10000*assign['M'] + 1000*assign['O'] +
                 100*assign['N'] + 10*assign['E'] + assign['Y'])

        if SEND + MORE == MONEY:
            print("Solution Found:\n")
            print(f"S={assign['S']} E={assign['E']} N={assign['N']} D={assign['D']}")
            print(f"M={assign['M']} O={assign['O']} R={assign['R']} Y={assign['Y']}")
            print("\nVerification:")
            print(f"{SEND} + {MORE} = {MONEY}")
            return

    print("No solution found")

solve_cryptarithm()