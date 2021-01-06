#Create a function within a module:
def find_sumo(fasta_file):
#Install biopython which is able to read in FASTA files using SeqRecord
 

    from Bio import SeqIO
    from Bio.SeqRecord import SeqRecord

#The following code, used to record the FASTA sequence without spaces in between lines, was taken from a webpage: http://python.omics.wiki/biopython/examples/read-fasta

# seq_record opens the FASTA sequence and reads it as a fasta sequence. 

#The FASTA sequence is saved as fasta_sequence to be further manipulated

    for seq_record in SeqIO.parse(open(fasta_file),'fasta'):
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

new_sequence= "".join(categorised_sequence)

#Identify each SUMOylation site using capital letters

 new_sequence_1=new_sequence.replace("hkxa", "HKXA")
 new_sequence_2=new_sequence_1.replace("hkaa", "HKAA")
 new_sequence_3=new_sequence_2.replace("hkka", "HKKA")
 new_sequence_4=new_sequence_3.replace("hkha", "HKHA")
#Dictate function to print the original fasta sequence, followed by the categorised sequence showing where the
#sumo sites are using capital letters
    print(fasta_sequence)
    print(new_sequence_4)

#Create seperate objects for each of the sequences to search for, taking into account the fact that h, k and a should also be considered x

hkxa = new_sequence.count("hkxa")
hkaa = new_sequence.count("hkaa")
hkka = new_sequence.count("hkka")
hkha = new_sequence.count("hkha")

#Search the categorised_sequence for each sequence and print the total of counts

print("There is", hkxa + hkaa + hkka + hkha, "SUMOylation sites in", fasta_file)

#Determine the positions of each sequence and add them to a list if the position number is >0
    sumo_positions = [] 

    hkxa_pos = new_sequence.find("hkxa")
    if hkxa_pos > 0:
        sumo_positions.append(hkxa_pos)
        
    hkaa_pos = new_sequence.find("hkaa")
    if hkaa_pos > 0:
        sumo_positions.append(hkaa_pos)
        
    hkka_pos = new_sequence.find("hkka")
    if hkka_pos > 0:
        sumo_positions.append(hkka_pos)
        
    hkha_pos = new_sequence.find("hkha")
    if hkha_pos > 0:
        sumo_positions.append(hkha_pos)
#Print the positions of each sequence
    print("at positions", sumo_positions)
