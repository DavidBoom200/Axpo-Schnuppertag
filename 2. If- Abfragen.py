numbers = [357,867,529]
sorted_numbers = sorted(numbers)
sorted_numbers = max(numbers)       #bestimmt die grösste Zahl
print(sorted_numbers)


year = 2008

def ist_schaltjahr(year):

    durch_4_teilbar = year % 4 == 0

    durch_100_teilbar = year % 100 == 0

    durch_400_teilbar = year % 400 == 0

    ist_schaltjahr = (durch_4_teilbar and not durch_100_teilbar) or durch_400_teilbar

    return ist_schaltjahr

# Beispiel
if ist_schaltjahr(year):
    print(f"{year} ist ein Schaltjahr.")
else:
    print(f"{year} ist kein Schaltjahr.")