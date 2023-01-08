class DNA_base_error(Exception):
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
        ele = str(input("Enter the 4 bases from the list - [A,T,G,C] : "))
        if (ele == 'A' or ele == 'T' or ele == 'G' or ele == 'C'):
            lst.append(ele) # adding the DNA strand
        else:
            raise DNA_base_error(ele)
    print("Template Strand: ", lst)
    res_comp_DNA = comp_DNA_creator(lst)
    print("Complementary DNA for template Strand : ", res_comp_DNA)
    res_mRNA = mRNA_creator(lst)
    print("Corresponding mRNA for template Strand: ", res_mRNA)
def comp_DNA_creator(lst):
    comp_DNA = []
    lstlen = len(lst)
    for i in range(0,lstlen):
        if(lst[i] == 'A'):
            comp_DNA_ele = 'T'
            comp_DNA.append(comp_DNA_ele)
        elif(lst[i] == 'T'):
            comp_DNA_ele = 'A'
            comp_DNA.append(comp_DNA_ele)
        elif(lst[i] == 'G'):
            comp_DNA_ele = 'C'
            comp_DNA.append(comp_DNA_ele)
        elif(lst[i] == 'C'):
            comp_DNA_ele = 'G'
            comp_DNA.append(comp_DNA_ele)
    return comp_DNA
def mRNA_creator(lst):
    mRNA = []
    lstlen = len(lst)
    for i in range(0,lstlen):
        if(lst[i] == 'A'):
            mRNA_ele = 'U'
            mRNA.append(mRNA_ele)
        elif(lst[i] == 'T'):
            mRNA_ele = 'A'
            mRNA.append(mRNA_ele)
        elif(lst[i] == 'G'):
            mRNA_ele = 'C'
            mRNA.append(mRNA_ele)
        elif(lst[i] == 'C'):
            mRNA_ele = 'G'
            mRNA.append(mRNA_ele)
    return mRNA    
if __name__ == "__main__":
    main()