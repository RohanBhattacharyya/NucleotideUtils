from invertFunction import *

codon_mapping = {
    # Phenylalanine (Phe)
    'UUU': 'Phe', 'UUC': 'Phe',
    
    # Leucine (Leu)
    'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    
    # Isoleucine (Ile)
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    
    # Methionine (Met) - Start Codon
    'AUG': 'Met',
    
    # Valine (Val)
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    
    # Serine (Ser)
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'AGU': 'Ser', 'AGC': 'Ser',
    
    # Proline (Pro)
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    
    # Threonine (Thr)
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    
    # Alanine (Ala)
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    
    # Tyrosine (Tyr)
    'UAU': 'Tyr', 'UAC': 'Tyr',
    
    # Stop Codons
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',
    
    # Histidine (His)
    'CAU': 'His', 'CAC': 'His',
    
    # Glutamine (Gln)
    'CAA': 'Gln', 'CAG': 'Gln',
    
    # Asparagine (Asn)
    'AAU': 'Asn', 'AAC': 'Asn',
    
    # Lysine (Lys)
    'AAA': 'Lys', 'AAG': 'Lys',
    
    # Aspartic Acid (Asp)
    'GAU': 'Asp', 'GAC': 'Asp',
    
    # Glutamic Acid (Glu)
    'GAA': 'Glu', 'GAG': 'Glu',
    
    # Cysteine (Cys)
    'UGU': 'Cys', 'UGC': 'Cys',
    
    # Tryptophan (Trp)
    'UGG': 'Trp',
    
    # Arginine (Arg)
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
    
    # Glycine (Gly)
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}

def CtoP():
    specialInvert(codon_mapping)