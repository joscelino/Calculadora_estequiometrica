
variable = int(input("""Choose a variable:
[1] Pressure
[2] Volume
[3] Number of moles
[4] Temperature

"""))

R = 0.082

if variable == 1:
    # Inputs
    V = float(input('Volume (L): '))
    T = float(input('Temperature (K): '))
    n = float(input('Number of moles: '))

    # Formula
    P = (n * R * T) / V

    # Printing
    print(f'The pressure is: {P} atm')

elif variable == 2:
    # Inputs
    P = float(input('Pressure (atm): '))
    T = float(input('Temperature (K): '))
    n = float(input('Number of moles: '))

    # Formula
    V = (n * R * T) / P

    # Printing
    print(f'The volume is: {V} L')

elif variable == 3:
    # Inputs
    P = float(input('Pressure (atm): '))
    T = float(input('Temperature (K): '))
    V = float(input('Volume (L): '))

    # Formula
    n = (P * V) / (R * T)

    # Printing
    print(f'The number of moles are: {n} .')

elif variable == 4:
    # Inputs
    P = float(input('Pressure (atm): '))
    V = float(input('Volume (L): '))
    n = float(input('Number of moles: '))

    # Formula
    T = (P * V) / (n * R)

    # Printing
    print(f'Temperature is: {T} K.')