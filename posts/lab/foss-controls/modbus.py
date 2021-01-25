def __generate_crc16_table():
    """
    from pymodbus3 
    (see static table of MODBUS over serial line specification and implementation guide V1.02)

    generates an ANSI crc16 lookup table for all possible byte values

    """
    crc16_table = []
    for byte in range(256):
        crc = 0x0000
        reciprocal_polynomial = 0xa001
        remaining_bits = 8
        while remaining_bits > 0:
            different_least_sig_bit = (byte ^ crc) & 0x0001
            if different_least_sig_bit: # addition modulo 2 evaluates to 1, change ls bit to 0
                crc = (crc >> 1) ^ reciprocal_polynomial 
                # reciprocal polynomial is A001
                # which is 1 + x^13 + x^15 + x^16
                # this is equivalent to operation on bit reversed input with the usual polynomial
                # 1 + x^2 + x^15 + x^16
                # here the byte is right-shifted, and so division operation is done least-to-most significant bit
            else: # addition modulo 2 evalutes to 0, move 0 out of register
                crc >>= 1
            byte >>= 1 # last bit (made 0) is moved out of the register
            remaining_bits -= 1
        crc16_table.append(crc)
    return crc16_table

__crc16_table = __generate_crc16_table()


def compute_crc(data):
    """ 
    from pymodbus3 
    (see algorithm description and C implementation in MODBUS over serial line specification and implementation guide V1.02)

    calculate the MODBUS RTU CRC

    data: tuple or other sequence-like of bytes
    """
    crc = 0xffff # initialize 2-byte register with 1s
    for byte in data:
        bit16xor = crc ^ byte # XOR 2-byte register with byte value
        bit8xor = bit16xor & 0xff # clear first byte in register
        idx = __crc16_table[bit8xor] # look up the "byte-CRC"
        # the "byte-CRC" can be non-zero up to the 2 bytes since a 16-bit polynomial is used
        crc = crc >> 8 # move out last byte (these are set to 0x00 implicitly by __crc16_table substitution)
        # crc = crc & 0xff # clear first byte (unnecessary since default fill value of 0 when right shifting)
        crc ^= idx # update CRC with XOR on byte-CRC
    # return lsb first
    # swapped = ((crc << 8) & 0xff00) | ((crc >> 8) & 0x00ff) # see below
    return (crc << 8 | crc >> 8) & 0xffff

if __name__ == '__main__':
    # wikipedia example (answer is b880)
    # why are there 1 byte spec for address, if you need to specify 2 byte?
    # if you zero pad the memory address to 2 bytes like (0x00, 0x02) the CRC is not the same

    print(hex(compute_crc((0x01, 0x04, 0x00, 0x02, 0xff, 0xff))))
    print(hex(compute_crc((0x01, 0x04, 0x02, 0xff, 0xff))))

    # weblog example
    station_address = 0x01,
    function_code = 0x00, 0x01
    memory_address = 0x00, 0x01
    data = station_address + function_code + memory_address
    print(hex(compute_crc(data)))
    print(bin(compute_crc(data)))
