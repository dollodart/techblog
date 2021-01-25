# more efficiently:
# bytes(string,encoding='ascii').hex()
# hex is python's preferred non-decimal base representation

def ascii2bits(string):
    """Ascii string to string of bits."""
    bit_string = ''
    for char in string:
        asci = ord(char)
        asci_8 = bin(asci)[2:]
        asci_8 = (8 - len(asci_8))*'0' + asci_8
        bit_string += asci_8
    return bit_string

if __name__ == '__main__':
    string = 'hello world'
    print(ascii2bits(string))
