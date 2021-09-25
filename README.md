# BINF-6200-Project-1

First project for Bioinformatics Programming (BINF 6200) at Northeastern University. 

## Description

This project consists of three programs. The first program has the protein sequence for Rattus norvegicus PKC Beta-1 hardcoded into it, and calculates the number of amino acids as well as the molecular weight of the protein in daltons. The second program converts user input of a number of nucleotides to the corresponding number of amino acids.

### Dependencies

* Program written on PyCharm with Python 3.9 and linted with Pylint Version 2.4.4

### Executing program

Program 1: Call the program by entering python3 calc_daltons.py. System will print number of amino acids and estimated peptide chain weight in kilodaltons. 

Program 2: Call program by entering python3 calc_number_amino_acids.py. System will prompt user to enter a name for the DNA sequence, user should type name and press enter. System will prompt user to enter a number of nucleotides for the DNA sequence, user should again type the number and press enter. If nucleotide number is a multiple of three system will print the number of corresponding amino acids and approximate weight of peptide chain in kilodaltons. 

Program 3: Call program by entering python3 dynamic_protocol.py. System will prompt user to enter final volume of solution, user should input this number in ml and press enter. System will then prompt user to enter the concentration of the NaCl stock solution, user should input this number in mM and press enter. System will prompt user to enter the final desired concentration of NaCl in solution, user should input this number in mM and press enter. System will prompt user to enter the concentration of the MgCl2 stock solution, user should input this number in mM and press enter. System will then prompt user to enter the final desired concentration of MgCl2 in solution, user should input this number in mM and press enter. System will print instructions to create solution.

## Help

If nucleotide sequence entered into Program 2 is not a multiple of three the program will print "Error: the DNA sequence is not a multiple of 3".

## Authors

Laura Whitley, whitley.l@northeastern.edu

## Acknowledgments

Assignment instructions/goals written by Chelsey Leslin, PhD for BINF 6200 at Northeastern University
