This is code writted in Python produced to scan any protein FASTA sequence for a specific motif of 
amino acids which suggest that the protien may be able to be modified by SUMO at the lysine residue 
within this motif. The code has been tested with the fasta sequence of two protiens which are known 
to contian the SUMOylation motif: Mitofusin2 (Mfn2) and Dynamin-related protein 1 (Drp1). 

To run:

1) Download the SUMO.py code which is the module that contains the function required to search a 
text file containing the fasta sequence of the protein of interest. 

2) Download the search_protein.py code which is the python script that will be run in the terminal
once the name of the text file containing the protein fasta sequence replaces "fasta_file". 

3) Download the example data, either Mfn2_seq.txt or Drp1_seq.txt, which contain the fasta sequences 
of the corresponding proteins. 

4) In the search_protein.py file in python, replace "fasta_file" with the name of the example data
file downloaded (either "Mfn2_seq.txt" or "Drp1_seq.txt"). Save and run the file in a new terminal. 
The output should give the fasta sequence, a categorised sequence with motifs identified using 
capital letters, and the number of SUMOylation sites there is, with their positions stated in a list.

When Mfn2_seq.txt is run, the output is expected to state their are 2 SUMOylatio sites at positions 
461 and 190. 
When Drp1_seq.txt is run, the output is expected to state their are 3 SUMOylation sites at positions 
510, 260, and the 3rd one is not states (an issue with the current code). 

5) Create a new text file and copy & paste the whole fasta sequence of a protein of interest 
(include all lines of the fastas sequence, including the title line). Try inserting this file into 
the search_protein.py code and run to see if your protein contains any SUMOylation motifs.  

Note: There is a risk that not all of the positions of each SUMO motif will be stated in the output.
However, the categorised code will show each motif position using capital letters, that can be
translated on the protein fasta sequence. 
