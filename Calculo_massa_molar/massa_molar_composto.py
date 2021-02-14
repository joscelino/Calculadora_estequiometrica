""" Calculo de massa molar de acordo com os atomos """

# Constants
C = 12.06
H = 1
O = 16

# Inputs
carbon = int(input('Type the number of carbon in the molecule: '))
hydrogen = int(input('Type the number of hydrogen in the molecule: '))
oxygen = int(input('Type the number of oxygen in the molecule: '))

# Formula
molecular_weight = C * carbon + H * hydrogen + O * oxygen

# Printing

print(f'The molecular mass of the chemical compound is: {molecular_weight} g/mol')
