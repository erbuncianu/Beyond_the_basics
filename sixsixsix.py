cuvant = "numerologie"

def find(i, s, target):
    if(i >= len(cuvant)):
        return
    if target == 666:  # or 666 - len(s) // 2 if you want to add the number of letters to the final result
        print(s)
    find(i + 1, s + f"+{cuvant[i]}", target + (ord(cuvant[i]) - ord('a') + 1))
    find(i + 1, s + f"-{cuvant[i]}", target - (ord(cuvant[i]) - ord('a') + 1))
    find(i + 1, s + f"*{cuvant[i]}", target * (ord(cuvant[i]) - ord('a') + 1))
    find(i + 1, s + f"/{cuvant[i]}", target // (ord(cuvant[i]) - ord('a') + 1))

find(0, "", 0)
print(list((ord(c) - ord('a') + 1) for c in cuvant))