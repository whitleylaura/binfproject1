"""calc_number_amino_acids"""
# generating input prompts
NAME = input('Please enter a name for the DNA sequence: ')
print('Your sequence name is:', NAME)

LENGTH = input('Please enter the length of the sequence: ')
print('The length of the sequence is:', LENGTH)

# calculations from input
PROTEIN_LENGTH = eval(LENGTH)/3
WEIGHT = PROTEIN_LENGTH * 0.11

# program output
if LENGTH % 3 == 0:
    print('The length of the decoded protein is: {0}'.format(str(PROTEIN_LENGTH)))
    print('The average weight of the protein sequence is: {0}'.format(str(WEIGHT)))
else:
    print('Error: the DNA sequence is not a multiple of 3')
