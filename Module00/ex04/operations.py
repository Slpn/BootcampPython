import sys

if (len(sys.argv)) > 3:
    print('InputError: too many arguments')
    quit()
if len(sys.argv) == 1:
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('     python operations.py 10 3')
    quit()
if sys.argv[1].isdigit() == False or  sys.argv[1].isdigit() == False:
    if sys.argv[1].isdigit() == False or  sys.argv[1].isdigit() == False:
        print('InputError: only numbers');
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('     python operations.py 10 3')
    quit()
nb = int(sys.argv[1])
nb2 = int(sys.argv[2])
tmp ='Quotient:   '
tmp2 = 'Reminder:   '
print('Sum:        ',nb + nb2)
print('Difference: ',nb - nb2)
print('Product:    ',nb * nb2)
if nb!=0 and nb2!=0:
    print(tmp , nb / nb2)
else:
    print(tmp, 'ERROR (div by zero)')
if nb!=0 and nb2!=0:
    print(tmp2, nb % nb2)
else:
    print(tmp2, 'ERROR (div by zero)')
