dna="ATCGATTGTCAAGTCTAGATACAGATACAGAT"
print("The length of the DNA sequence is:", len(dna))
gc_count = dna.count("G") + dna.count("C")
gc_content = (gc_count / len(dna)) * 100
print("The GC content of the DNA sequence is:", gc_content, "%")
print("The DNA sequence is:", dna)
print("A count:", dna.count("A"))
print("T count:", dna.count("T"))
print("G count:", dna.count("G"))
print("C count:", dna.count("C"))
reverse_complement = dna[::-1].translate(str.maketrans("ATCG", "TAGC"))
print("The reverse complement of the DNA sequence is:", reverse_complement)
