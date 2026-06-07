dna = input("Enter DNA sequence: ").upper()
print(dna)

print("\nDNA Analysis Report")
print("-------------------")

print("Length:", len(dna))

print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))

gc = ((dna.count("G") + dna.count("C")) / len(dna)) * 100

print("GC Content:", round(gc, 2), "%")
if gc>50:
    print("This DNA is GC-rich.")
else:    print("This DNA is AT-rich.")