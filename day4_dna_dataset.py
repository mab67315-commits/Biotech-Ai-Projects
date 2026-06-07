dna_samples = [
    "ATGCGCTA",
    "GGGCCC",
    "ATATATAT",
    "CGCGCGCGCG"
]

print("DNA Dataset Analysis")
print("-------------------")

total_length = 0
longest = ""
gc_count = 0

for dna in dna_samples:

    print("Sequence:", dna)
    print("Length:", len(dna))


    total_length += len(dna)

    # Count G and C nucleotides
    gc_count += dna.count('G') + dna.count('C')
    gc_content = (gc_count / total_length) * 100 if total_length > 0 else 0

    if len(dna) > len(longest):
        longest = dna

average = total_length / len(dna_samples)

print("\nResults")
print("Longest Sequence:", longest)
print("Average Length:", average)
print("GC Content:", gc_count)
print("GC Content (%):", gc_content)