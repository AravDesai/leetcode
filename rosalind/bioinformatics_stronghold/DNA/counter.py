a = 0
c = 0
g = 0
t = 0
with open("rosalind_dna.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        a = a + line.count("A")
        c = c + line.count("C")
        g = g + line.count("G")
        t = t + line.count("T")
file.close()
print(f"{a} {c} {g} {t}")
