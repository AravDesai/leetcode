output = ""
with open("rosalind_revc.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        reversed = line[::-1].translate(str.maketrans("ACGT","TGCA"))
        output = output + str(reversed) + "\n"
file.close()
print(output)