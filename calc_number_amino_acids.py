# generating input prompts
name = input('Please enter a name for the DNA sequence: ')
print('Your sequence name is:', name)

length = input('Please enter the length of the sequence: ')
print('The length of the sequence is:', length)

# calculations from input
protein_length = eval(length)/3
weight = protein_length * 0.11

if 3 == 0:
    print('The length of the decoded protein is: ' + str(protein_length))
    print('The average weight of the protein sequence is: ' + str(weight))
# program output
else:
    print('Error: the DNA sequence is not a multiple of 3')
