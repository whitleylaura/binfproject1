# generating inputs
final_vol = float(input('Please enter the final volume of the solution (ml): '))
nacl_stock = float(input('Please enter the NaCl stock (mM): '))
nacl_final = float(input('Please enter the NaCl final (mM): '))
mg_stock = float(input('Please enter the MgCl2 stock (mM): '))
mg_final = float(input('Please enter the MgCl2 stock (mM): '))

# calculating amount of NaCl needed
step1 = f"Add {str(final_vol * (nacl_final / nacl_stock))} ml NaCl\n"

# calculating amount of MgCl2 needed
step2 = f"Add {str(final_vol * (mg_final / mg_stock))} ml MgCl2\n"

# adding water to final volume
step3 = f"Add water to a final volume of {str(final_vol)} ml and mix"

print(step1 + step2 + step3)