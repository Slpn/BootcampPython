import sys

len = len(sys.argv) - 1
# tmp = sys.argv[len][::-1].swapcase()
tmp = ''
if len == 1:
    while len > 0:
        tmp += sys.argv[len][::-1].swapcase()
        len -= 1
        if len != 0:
            tmp += ' '
    print(tmp)
