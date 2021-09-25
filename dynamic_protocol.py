"""dynamic_protocol"""
# generating inputs
FINAL_VOL = float(input('Please enter the final volume of the solution (ml): '))
NACL_STOCK = float(input('Please enter the NaCl stock (mM): '))
NACL_FINAL = float(input('Please enter the NaCl final (mM): '))
MG_STOCK = float(input('Please enter the MgCl2 stock (mM): '))
MG_FINAL = float(input('Please enter the MgCl2 final (mM): '))

# calculating amount of NaCl needed
STEP1 = f"Add {str(FINAL_VOL * (NACL_FINAL / NACL_STOCK))} ml NaCl\n"

# calculating amount of MgCl2 needed
STEP2 = f"Add {str(FINAL_VOL * (MG_FINAL / MG_STOCK))} ml MgCl2\n"

# adding water to final volume
STEP3 = f"Add water to a final volume of {str(FINAL_VOL)} ml and mix"

print(STEP1 + STEP2 + STEP3)
