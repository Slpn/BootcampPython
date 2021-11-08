import sys

if len(sys.argv) != 2 or sys.argv[1].isdigit() == False:
    print("ERROR")
    sys.exit()
nb = int(sys.argv[1])
if nb == 0:
    print("I'm Zero.")
elif nb % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
