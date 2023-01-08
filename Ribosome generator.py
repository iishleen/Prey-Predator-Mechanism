class mRNA_base_error(Exception):
    def __init__(self, DNA_base_input, message="Sorry, wrong base selected!"):
        self.DNA_base_input = DNA_base_input
        self.message = message
        super().__init__(self.message)
def main():
    lst = []
    comp_DNA = [] 
    # number of elements as input
    n = int(input("Enter the number of elements in the DNA strand : "))

    # iterating for range
    for i in range(0, n):
        ele = str(input("Enter the 4 bases from the list - [A,U,G,C] : "))
        if (ele == 'A' or ele == 'U' or ele == 'G' or ele == 'C'):
            lst.append(ele) # adding the DNA strand
        else:
            raise DNA_base_error(ele)
    print("mRNA Strand for amino acid processing: ", lst)
    amino_acid_chain = ribosome(lst)
    print("Amino Acid chain is: ", amino_acid_chain)
    
def ribosome(lst):
    amino_acid_lst = []
    codon_string = ''
    working_mRNA_ref_dic={}
    
    mRNA_ref_dic = {('GCU','GCG','GCC','GCA'): 'Alanine', ('GGU','GGC','GGA','GGG'): 'Glycine', 
                    ('AUU','AUC','AUA'): 'Isoleucine',('CUU','CUA','CUG','CUC','UUA','UUG'): 'Leucine', 
                    ('CCU','CCG','CCA','CCC'): 'Proline',('GUU','GUA','GUC','GUG'):'Valine', 
                    ('UUU','UUC'):'Phenylalanine', ('UGG',''):'Tryptophan', ('UAU','UAC'): 'Tyrosine',
                    ('GAU','GAC'):'Aspartic Acid',('GAA','GAG'):'Glutamic Acid',
                    ('CGU','CGA','CGC','CGG','AGA','AGG'): 'Arginine', ('CAU','CAC'): 'Histidine',
                    ('AAA','AAG'): 'Lysine', ('UCU','UCA','UCG','UCC','AGU','AGC'): 'Serine',
                    ('ACU','ACC','ACG','ACA'):'Threonine', ('UGU','UGC'):'Cysteine', ('AUG','') :'Methionine',
                    ('AAU','AAC'):'Asparagine', ('CAA','CAG'):'Glutamine', ('UGA','') : 'Stop Codon'}
    for k, v in mRNA_ref_dic.items():
        for key in k:
            working_mRNA_ref_dic[key] = v
    while(len(lst)>2):
        for i in range(0,3):
            codon_string += lst[i]
        amino_acid_lst.append(working_mRNA_ref_dic[codon_string])
        codon_string = ''
        del lst[:3]
    return amino_acid_lst

                
        
    
    