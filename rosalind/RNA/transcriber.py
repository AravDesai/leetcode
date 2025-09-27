output = ""
with open("rosalind_rna.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        output = line.replace("T","U") + "\n"
file.close()
print(output)