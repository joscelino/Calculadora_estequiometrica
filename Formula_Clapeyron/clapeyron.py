"""" script que calcula a formula de Clapeyron """

# Inputs
V = float(input('Volume (L): '))
T = float(input('Temperature (K): '))
n = float(input('Number of mols: '))

# Constants
R = 0.082

# Formula
P = (n*R*T) / V

# Printing
print(f'The pressure is: {P} atm')
