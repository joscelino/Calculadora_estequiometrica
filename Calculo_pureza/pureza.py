"""  Purity calculator """
# Inputs (Reagent)
stoichiometric_coefficient_reagent = float(input("Type the stoichiometric coefficient of the reagent: "))
molar_mass_reagent = float(input("Type the molar mass of the reagent (g/mol): "))
mass_reagent = float(input("Type the mass of the reagent: "))

# Inputs (Product)
stoichiometric_coefficient_product = float(input("Type the stoichiometric coefficient of the product: "))
molar_mass_product = float(input("Type the molar mass of the product (g/mol): "))
mass_product = float(input("Type the mass of the product: "))


total_molar_mass_r = stoichiometric_coefficient_reagent * molar_mass_reagent
total_molar_mass_p = stoichiometric_coefficient_product * molar_mass_product

# Conditions
component = int(input(''' Choose the component to calculate the purity: 
[1] - reagent
[2] - product
'''))

# Calculations
if component == 1:
    x = (total_molar_mass_r*mass_product)/total_molar_mass_p
    x_yield = (x/mass_reagent) * 100
    comp = 'reagent'
if component == 2:
    x = (total_molar_mass_p * mass_reagent) / total_molar_mass_r
    x_yield = (x/mass_product) * 100
    comp = 'product'

# Printing
print(f'The {comp} yield was: {round(x_yield,4)}%')
