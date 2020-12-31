#Install biopython which is able to read in FASTA files using SeqRecord


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#Import file containing protein FASTA sequence

file_in = 'Mfn2_seq.fasta'

#The following code, used to record the FASTA sequence without spaces in between lines, was taken from a webpage: http://python.omics.wiki/biopython/examples/read-fasta

# seq_record opens the FASTA sequence and reads it as a fasta sequence. 

#The FASTA sequence is saved as fasta_sequence to be further manipulated

    for seq_record in SeqIO.parse(open('Mfn2_seq.txt', mode='r'),'fasta'):
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
    

#Turn categorised list into new sequence by removing punctuation: 

new_sequence= " ".join(categorised_sequence)

#Identify each SUMOylation site using capital letters

 new_sequence_1=new_sequence.replace("h k x a", "H K X A")
 new_sequence_2=new_sequence_1.replace("h k a a", "H K A A")
 new_sequence_3=new_sequence_2.replace("h k k a", "H K K A")
 new_sequence_4=new_sequence_3.replace("h k h a", "H K H A")
    
    print(new_sequence_4)

#Create seperate objects for each of the sequences to search for, taking into account the fact that h, k and a should also be considered x

hkxa = new_sequence.count("h k x a")
hkaa = new_sequence.count("h k a a")
hkka = new_sequence.count("h k k a")
hkha = new_sequence.count("h k h a")

#Search the categorised_sequence for each sequence and print the total of counts

print("There is", hkxa + hkaa + hkka + hkha, "SUMOylation sites in", fasta_file)
