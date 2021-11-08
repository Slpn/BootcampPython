import sys

len = len(sys.argv)
i = 2
tmp = sys.argv[1][::-1].swapcase()
while i < len:
    tmp += ' '
    tmp += sys.argv[i][::-1].swapcase()
    i += 1
print(tmp)
