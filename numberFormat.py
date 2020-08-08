def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        width = len(bin(number)) - 2
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width))

    # Conversion methods
    # decimal = str(i)
    # octal = str(oct(i))[2:]
    # h = str(hex(i))[2:]
    # hexa = h.upper()
    # binary = str(bin(i))[2:]

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
