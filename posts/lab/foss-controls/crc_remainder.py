def right_arrow_func(shift):
    if shift == 0:
        return ''
    elif shift == 1:
        return '>'
    return (shift - 1)*'-' + '>'


def left_arrow_func(shift):
    if shift == 0:
        return ''
    elif shift == 1:
        return '<'
    return '<' + (shift-1)*'-'


def crc_remainder(input_bitstring, polynomial_bitstring,
                  initial_filler='0', shifting='left'):
    """
    Algorithm from Wikipedia.
    Calculates the CRC remainder of a string of bits
    using a chosen polynomial.
    Initial_filler should be '1' or '0'.
    Shifting is either 'left' or 'right'.
    """
    pb = polynomial_bitstring.lstrip('0')

    len_input = len(input_bitstring)
    len_pb = len(pb)
    len_ipad = len(pb) - 1
    rs = len_input - 1

    ipad = initial_filler * len_ipad
    ipadarr = list(input_bitstring + ipad) # mutable sequence needed

    st = ''

    while '1' in ipadarr[:len_input]:
        cur_shift = ipadarr.index('1') # first occurance

        if shifting == 'left':
            # since the input array is shifting
            # the operations will not drop down
            # like in the right shifting case
            st += (' '*(rs - cur_shift) + ''.join(ipadarr) +
                   left_arrow_func(cur_shift) + '\n')
            st += ' '*rs + '^'*len_pb + '\n'
            st += ' '*(rs) + pb + '\n'
        elif shifting == 'right':
            st += ''.join(ipadarr) + '\n'
            st += right_arrow_func(cur_shift) + pb + '\n'
            st += ' '*cur_shift+'^'*len_pb + '\n'
        else:
            raise Exception("allowed shift directions "
                            "are 'left' and 'right'")

        for i in range(len_pb):
            if pb[i] == ipadarr[cur_shift + i]:
                ipadarr[cur_shift + i] = '0'
            else:
                ipadarr[cur_shift + i] = '1'

    st += ''.join(ipadarr)
    return st, ''.join(ipadarr)[len_input:]


def polynomialbitstring2polynomialexpression(polynomial_bitstring):
    pb = polynomial_bitstring
    st = ''
    for pos, coeff in enumerate(reversed(pb)):
        if coeff == '1':
            st += f'x^{pos} + '
    return st.strip(' + ')


if __name__ == '__main__':
    # wikipedia test case
    pb = '1011'
    print(polynomialbitstring2polynomialexpression(pb))
    work, rem = crc_remainder('11010011101100', pb)
    print()
    print(work)
    print()
    assert rem == '100'
    print(f'remainder = {rem}')
