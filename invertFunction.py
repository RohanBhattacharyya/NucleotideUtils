def invert(nucleotide_mapping):
    x = input("First Sequence:  ").upper()
    print("Second Sequence: ", end="")
    for char in x:
        try:
            print(nucleotide_mapping[char], end="")
        except KeyError:
            print(char, end="")

# def specialInvert(codon_mapping):
#     x = input("First Sequence:  ").upper()
#     print("Second Sequence: ", end="")
#     x+=" "

#     nucleotides = "AUCG"

#     currentcodon=""
#     for z in x:
#         if len(currentcodon) < 3:
#             if z in nucleotides:
#                     currentcodon += z
#         else:
#             print(codon_mapping[currentcodon],end=" ")
#             currentcodon=""
#             x+=" "

def specialInvert(codon_mapping):
    x = input("First Sequence:  ").upper()
    print("Second Sequence: ", end="")

    nucleotides = "AUCG"
    currentcodon = ""

    for z in x:
        if z in nucleotides:
            currentcodon += z
            if len(currentcodon) == 3:
                print(codon_mapping.get(currentcodon, "?"), end=" ")  # Using get to avoid KeyErrors
                currentcodon = ""  # Reset for the next codon