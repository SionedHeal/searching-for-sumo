def find_sumo(fasta_file):
    from Bio import SeqIO
    from Bio.SeqRecord import SeqRecord

    for seq_record in SeqIO.parse(open(fasta_file),'fasta'):
        fasta_sequence = seq_record.seq
        
        aminoacid_category = {"A": "h", "V": "h", "I": "h", "L": "h", "M": "h", "F": "h", "Y": "h", "W": "h", 
                  "G": "x", "P": "x", "R": "x", "H": "x", "S": "x", "T": "x", "C": "x", "N": "x", "Q": "x",
                  "D": "a", "E": "a",
                  "K": "k"}
        
        categorised_sequence=[]
        
    for letter in fasta_sequence:
        aminoacid_type=aminoacid_category[letter]
        categorised_sequence.append(aminoacid_type)
    
    new_sequence= "".join(categorised_sequence)
    
    new_sequence_1=new_sequence.replace("hkxa", "HKXA")
    new_sequence_2=new_sequence_1.replace("hkaa", "HKAA")
    new_sequence_3=new_sequence_2.replace("hkka", "HKKA")
    new_sequence_4=new_sequence_3.replace("hkha", "HKHA")
    
    print("Protein sequence:",fasta_sequence)
    print("Categorised sequence, motif positions as capitals:", new_sequence_4)
    
    hkxa = new_sequence.count("hkxa")
    hkaa = new_sequence.count("hkaa")
    hkka = new_sequence.count("hkka")
    hkha = new_sequence.count("hkha")
    
    print("There is", hkxa + hkaa + hkka + hkha, "SUMOylation sites in", fasta_file)
 
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
    
    print("at positions", sumo_positions)
