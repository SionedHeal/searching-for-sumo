#Install biopython which is able to read in FASTA files using SeqRecord


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#Import file containing protein FASTA sequence

file_in = 'Mfn2_seq.fasta'

#The following code, used to record the FASTA sequence without spaces in between lines, was taken from a webpage: http://python.omics.wiki/biopython/examples/read-fasta

# seq_record opens the FASTA sequence and reads it as a fasta sequence. 
# The fasta id line is removed from seq_record.description, and is separated into seq_record.id, which can be printed seperately 

#The FASTA sequence is saved as fasta_sequence to be further manipulated

with open (file_in, 'w') as f_in:
    for seq_record in SeqIO.parse(open('Mfn2_seq.txt', mode='r'),'fasta'):
        seq_record.description=''.join(seq_record.description[1:])
        print(seq_record.seq)
        print(seq_record.id)
        fasta_sequence = seq_record.seq
        

#Consensus SUMOylation site: h K x a (h = hydrophobic, x = any amino acid, a = acidic residue)
#Dictionary created categorsing each amino acid in the FASTA sequence into either h, K, x, or a


aminoacid_category = {"A": "h", "V": "h", "I": "h", "L": "h", "M": "h", "F": "h", "Y": "h", "W": "h", 
                  "G": "x", "P": "x", "R": "x", "H": "x", "S": "x", "T": "x", "C": "x", "N": "x", "Q": "x",
                  "D": "a", "E": "a",
                  "K": "k"}

#List created for each amino acid as it's category to be documented

categorised_sequence=[]

#Loop over each letter in fasta sequence and categorise into either h, K, x or a using the dictionary

for letter in fasta_sequence:
    aminoacid_type=aminoacid_category[letter]
    categorised_sequence.append(aminoacid_type)
    
print(categorised_sequence)

#Turn categorised list into new sequence by removing punctuation: 

new_sequence= " ".join(categorised_sequence)
print(new_sequence)

#Search new sequence string for specific SUMOylation consensus sequence: h K x a

print("There is", new_sequence.count("h k x a"), "SUMOylation site")
print("at position", new_sequence.find("h k x a"))
