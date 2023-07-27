weight = int(input('Weight: '))
Type = input('Is weight in (K)g or (L)bs: ')

if Type.upper() == 'K':
    converted = weight * 2.205
    print(f'Your weight in pounds is: {converted}')

elif Type.upper() == 'L':
    converted_kg = weight // 2.205
    print(f'Your weight in kg is: {converted_kg}')

else:
    raise ValueError('Value should be either K/L')
