DNA= input("Enter a DNA sequence: ")
def gc_content(sequence):

    g = sequence.count("G")
    c = sequence.count("C")

    gc = ((g + c) / len(sequence)) * 100
    return gc
result = gc_content(DNA)
print("GC Content:", round(result, 2))
if result > 60:
    print("The DNA sequence is GC-rich.")
elif result == 50:
    print("The DNA sequence has a normal GC content.")
else:
    print("The DNA sequence is AT-rich.")

def length_sequence(sequence):
    print(len(sequence))
length_sequence(DNA)

def nucleotide_count(sequence):
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    print("A:", a)
    print("T:", t)
    print("G:", g)
    print("C:", c)
nucleotide_count(DNA)

