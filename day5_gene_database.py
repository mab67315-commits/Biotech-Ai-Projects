gene_database = {
    "BRCA1": "DNA Repair",
    "TP53": "Tumor Suppressor",
    "EGFR": "Cell Growth",
    "KRAS": "Signal Transduction",
    "MYC": "Cell Cycle Regulation"
}

for gene, function in gene_database.items():
    print(gene, "--------->", function)

gene= input("Enter a gene name to find its function: ")
if gene in gene_database:
    print(gene, "--------->", gene_database[gene])
else:
    print("Gene not found.")