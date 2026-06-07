def length_sequence(sequence):
    return len(sequence)

def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")

    gc = ((g + c) / len(sequence)) * 100
    return gc

def reverse_complement(sequence):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reverse_comp = "".join(complement[base] for base in reversed(sequence))
    return reverse_comp

def translate_dna_to_protein(dna_sequence):
    codon_table = {
        "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
        "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
        "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
        "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
        # ... (complete the codon table)
    }
    protein_sequence = ""
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        protein_sequence += codon_table.get(codon, "?")  # Use '?' for unknown codons
    return protein_sequence

def count_motif(sequence, motif):
    count = 0
    motif_length = len(motif)
    for i in range(len(sequence) - motif_length + 1):
        if sequence[i:i+motif_length] == motif:
            count += 1
    return count

def find_motif_positions(sequence, motif):
    positions = []
    motif_length = len(motif)
    for i in range(len(sequence) - motif_length + 1):
        if sequence[i:i+motif_length] == motif:
            positions.append(i + 1)  # 1-based indexing
    return positions

def calculate_melting_temperature(sequence):
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    
    tm = 2 * (a + t) + 4 * (g + c)
    return tm

def find_orfs(dna_sequence):
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    orfs = []
    
    for i in range(len(dna_sequence) - 2):
        codon = dna_sequence[i:i+3]
        if codon == start_codon:
            for j in range(i + 3, len(dna_sequence) - 2, 3):
                stop_codon = dna_sequence[j:j+3]
                if stop_codon in stop_codons:
                    orfs.append(dna_sequence[i:j+3])
                    break
    return orfs

def calculate_nucleotide_frequencies(sequence):
    frequencies = {
        "A": sequence.count("A") / len(sequence),
        "T": sequence.count("T") / len(sequence),
        "C": sequence.count("C") / len(sequence),
        "G": sequence.count("G") / len(sequence)
    }
    return frequencies

def calculate_codon_usage(dna_sequence):
    codon_table = {
        "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
        "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
        "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
        "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
        # ... (complete the codon table)
    }
    codon_usage = {codon: 0 for codon in codon_table.keys()}
    
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        if codon in codon_usage:
            codon_usage[codon] += 1
            
    return codon_usage

def calculate_protein_molecular_weight(protein_sequence):
    amino_acid_weights = {
        "A": 89.09, "R": 174.20, "N": 132.12, "D": 133.10,
        "C": 121.15, "E": 147.13, "Q": 146.15, "G": 75.07,
        "H": 155.16, "I": 131.17, "L": 131.17, "K": 146.19,
        "M": 149.21, "F": 165.19, "P": 115.13, "S": 105.09,
        "T": 119.12, "W": 204.23, "Y": 181.19, "V": 117.15
    }
    molecular_weight = sum(amino_acid_weights.get(aa, 0) for aa in protein_sequence)
    return molecular_weight

def calculate_protein_isoelectric_point(protein_sequence):
    amino_acid_pI = {
        "A": 6.00, "R": 10.76, "N": 5.41, "D": 2.77,
        "C": 5.07, "E": 3.22, "Q": 5.65, "G": 5.97,
        "H": 7.59, "I": 6.02, "L": 6.02, "K": 9.74,
        "M": 5.74, "F": 5.48, "P": 6.30, "S": 5.68,
        "T": 5.60, "W": 5.89, "Y": 5.66, "V": 6.00
    }
    pI = sum(amino_acid_pI.get(aa, 0) for aa in protein_sequence) / len(protein_sequence)
    return pI

def calculate_protein_hydrophobicity(protein_sequence):
    amino_acid_hydrophobicity = {
        "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5,
        "C": 2.5, "E": -3.5, "Q": -3.5, "G": -0.4,
        "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9,
        "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8,
        "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2
    }
    hydrophobicity = sum(amino_acid_hydrophobicity.get(aa, 0) for aa in protein_sequence) / len(protein_sequence)
    return hydrophobicity

def calculate_protein_charge(protein_sequence, pH):
    amino_acid_charge = {
        "A": 0, "R": 1, "N": 0, "D": -1,
        "C": 0, "E": -1, "Q": 0, "G": 0,
        "H": 1, "I": 0, "L": 0, "K": 1,
        "M": 0, "F": 0, "P": 0, "S": 0,
        "T": 0, "W": 0, "Y": -1, "V": 0
    }
    charge = sum(amino_acid_charge.get(aa, 0) for aa in protein_sequence)
    return charge

def calculate_protein_instability_index(protein_sequence):
    dipeptide_weights = {
        "AA": 1.0, "AR": 0.5, "AN": 0.8, "AD": 0.9,
        "AC": 1.2, "AE": 0.7, "AQ": 0.6, "AG": 0.4,
        "AH": 0.3, "AI": 1.5, "AL": 1.4, "AK": 0.2,
        "AM": 1.1, "AF": 1.3, "AP": 0.9, "AS": 0.8,
        "AT": 0.7, "AW": 1.6, "AY": 1.2, "AV": 1.4,
        # ... (complete the dipeptide weights)
    }
    instability_index = sum(dipeptide_weights.get(protein_sequence[i:i+2], 0) for i in range(len(protein_sequence) - 1)) / len(protein_sequence)
    return instability_index

def calculate_protein_aliphatic_index(protein_sequence):
    aliphatic_weights = {
        "A": 1.0, "R": 0.0, "N": 0.0, "D": 0.0,
        "C": 0.5, "E": 0.0, "Q": 0.0, "G": 0.0,
        "H": 0.0, "I": 1.5, "L": 1.5, "K": 0.0,
        "M": 1.2, "F": 1.3, "P": 1.0, "S": 0.5,
        "T": 0.5, "W": 1.4, "Y": 1.3, "V": 1.4
    }
    aliphatic_index = sum(aliphatic_weights.get(aa, 0) for aa in protein_sequence) / len(protein_sequence)
    return aliphatic_index

def calculate_protein_gravy(protein_sequence):
    amino_acid_hydrophobicity = {
        "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5,
        "C": 2.5, "E": -3.5, "Q": -3.5, "G": -0.4,
        "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9,
        "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8,
        "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2
    }
    gravy = sum(amino_acid_hydrophobicity.get(aa, 0) for aa in protein_sequence) / len(protein_sequence)
    return gravy

def calculate_protein_aromaticity(protein_sequence):
    aromatic_amino_acids = {"F", "W", "Y"}
    aromaticity = sum(1 for aa in protein_sequence if aa in aromatic_amino_acids) / len(protein_sequence)
    return aromaticity

def calculate_protein_secondary_structure(protein_sequence):
    alpha_helix = sum(1 for aa in protein_sequence if aa in "ALMFWK") / len(protein_sequence)
    beta_sheet = sum(1 for aa in protein_sequence if aa in "VILY") / len(protein_sequence)
    coil = sum(1 for aa in protein_sequence if aa not in "ALMFWKVILY") / len(protein_sequence)
    return {"alpha_helix": alpha_helix, "beta_sheet": beta_sheet, "coil": coil}

def calculate_protein_solubility(protein_sequence):
    hydrophobic_amino_acids = {"A", "I", "L", "M", "F", "W", "V"}
    solubility = sum(1 for aa in protein_sequence if aa in hydrophobic_amino_acids) / len(protein_sequence)
    return solubility

def calculate_protein_aggregation_propensity(protein_sequence):
    aggregation_prone_amino_acids = {"I", "L", "V", "F", "W"}
    aggregation_propensity = sum(1 for aa in protein_sequence if aa in aggregation_prone_amino_acids) / len(protein_sequence)
    return aggregation_propensity

def calculate_protein_disorder(protein_sequence):
    disorder_prone_amino_acids = {"P", "E", "S", "K", "Q"}
    disorder = sum(1 for aa in protein_sequence if aa in disorder_prone_amino_acids) / len(protein_sequence)
    return disorder

def calculate_protein_binding_sites(protein_sequence):
    binding_site_amino_acids = {"R", "K", "D", "E"}
    binding_sites = sum(1 for aa in protein_sequence if aa in binding_site_amino_acids) / len(protein_sequence)
    return binding_sites

def calculate_protein_post_translational_modifications(protein_sequence):
    ptm_sites = sum(1 for aa in protein_sequence if aa in "STY") / len(protein_sequence)
    return ptm_sites

def calculate_protein_half_life(protein_sequence):
    half_life = sum(1 for aa in protein_sequence if aa in "DE") / len(protein_sequence)
    return half_life

def calculate_protein_stability(protein_sequence):
    stability = sum(1 for aa in protein_sequence if aa in "ACDEFGHIKLMNPQRSTVWY") / len(protein_sequence)
    return stability

def calculate_protein_flexibility(protein_sequence):
    flexibility = sum(1 for aa in protein_sequence if aa in "GASPV") / len(protein_sequence)
    return flexibility

def calculate_protein_hydrophilicity(protein_sequence):
    hydrophilic_amino_acids = {"R", "K", "D", "E", "N", "Q"}
    hydrophilicity = sum(1 for aa in protein_sequence if aa in hydrophilic_amino_acids) / len(protein_sequence)
    return hydrophilicity

def calculate_protein_charge(protein_sequence, pH):
    amino_acid_charge = {
        "A": 0, "R": 1, "N": 0, "D": -1,
        "C": 0, "E": -1, "Q": 0, "G": 0,
        "H": 1, "I": 0, "L": 0, "K": 1,
        "M": 0, "F": 0, "P": 0, "S": 0,
        "T": 0, "W": 0, "Y": -1, "V": 0
    }
    charge = sum(amino_acid_charge.get(aa, 0) for aa in protein_sequence)
    return charge

def nucleotide_count(sequence):
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G")
    }

sequence = "ATGCGCTA"
print("Nucleotide Count:", nucleotide_count(sequence))
print("Sequence Length:", length_sequence(sequence))
print("GC Content:", round(gc_content(sequence), 2))
print("Reverse Complement:", reverse_complement(sequence))
protein_sequence = translate_dna_to_protein(sequence)
print("Translated Protein Sequence:", protein_sequence)
print("Motif Count (CG):", count_motif(sequence, "CG"))
print("Motif Positions (CG):", find_motif_positions(sequence, "CG"))
print("Melting Temperature:", calculate_melting_temperature(sequence))
orfs = find_orfs(sequence)
print("Open Reading Frames:", orfs)
print("Nucleotide Frequencies:", calculate_nucleotide_frequencies(sequence))
print("Codon Usage:", calculate_codon_usage(sequence))
print("Protein Molecular Weight:", calculate_protein_molecular_weight(protein_sequence))
print("Protein Isoelectric Point:", calculate_protein_isoelectric_point(protein_sequence))
print("Protein Hydrophobicity:", calculate_protein_hydrophobicity(protein_sequence))
print("Protein Charge at pH 7:", calculate_protein_charge(protein_sequence, 7))
print("Protein Instability Index:", calculate_protein_instability_index(protein_sequence))
print("Protein Aliphatic Index:", calculate_protein_aliphatic_index(protein_sequence))
print("Protein GRAVY:", calculate_protein_gravy(protein_sequence))
print("Protein Aromaticity:", calculate_protein_aromaticity(protein_sequence))
print("Protein Secondary Structure:", calculate_protein_secondary_structure(protein_sequence))
print("Protein Solubility:", calculate_protein_solubility(protein_sequence))
print("Protein Aggregation Propensity:", calculate_protein_aggregation_propensity(protein_sequence))
print("Protein Disorder:", calculate_protein_disorder(protein_sequence))
print("Protein Binding Sites:", calculate_protein_binding_sites(protein_sequence))
print("Protein Post-Translational Modifications:", calculate_protein_post_translational_modifications(protein_sequence))
print("Protein Half-Life:", calculate_protein_half_life(protein_sequence))