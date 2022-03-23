# modem table
modem_table = """110 baud Bell 101 modem|FSK|0.1|1958
300 baud (Bell 103 or V.21)|FSK|0.3|1962
1200 modem (1200 baud) (Bell 202)|FSK|1.2|1976
1200 modem (600 baud) (Bell 212A or V.22)|QPSK|1.2|1980[15][16]
2400 modem (600 baud) (V.22bis)|QAM|2.4|1984[15]
9600 modem (2400 baud) (V.32)|QAM|9.6|1984[15]
14.4k modem (2400 baud) (V.32bis)|trellis|14.4|1991[15]
19.2k modem (2400 baud) (V.32terbo)|trellis|19.2|1993[15]
28.8k modem (3200 baud) (V.34)|trellis|28.8|1994[15]
33.6k modem (3429 baud) (V.34)|trellis|33.6|1996[18]
56k modem (8000/3429 baud) (V.90)|digital|56.0/33.6|1998[15]
56k modem (8000/8000 baud) (V.92)|digital|56.0/48.0|2000[15]"""

# peripheral table
peripheral_table = """Apple Desktop Bus|10.0 kbit/s|1.25 kB/s|1986
PS/2 port|12.0 kbit/s|1.5 kB/s|1987
Serial MIDI|31.25 kbit/s|3.9 kB/s|1983
CBM Bus max[61][62]|41.6 kbit/s|5.1 kB/s|1981
Serial RS-232 max|230.4 kbit/s|28.8 kB/s|1962
Serial DMX512A|250.0 kbit/s|31.25 kB/s|1998
Parallel (Centronics/IEEE 1284)|1 Mbit/s|125 kB/s|1970 (standardized 1994)
Serial 16550 UART max|1.5 Mbit/s|187.5 kB/s|
USB 1.0 low speed|1.536 Mbit/s|192 kB/s|1996
Serial UART max|2.7648 Mbit/s|345.6 kB/s|
GPIB/HPIB (IEEE-488.1) IEEE-488 max.|8 Mbit/s|1 MB/s|Late 1960s (standardized 1976)
Serial EIA-422 max.|10 Mbit/s|1.25 MB/s|
USB 1.0 full speed|12 Mbit/s|1.5 MB/s|1996
Parallel (Centronics/IEEE 1284) EPP (Enhanced Parallel Port)|16 Mbit/s|2 MB/s|1992
Parallel (Centronics/IEEE 1284) ECP (Extended Capability Port)|20 Mbit/s|2.5 MB/s|1994
Serial EIA-485 max.|35 Mbit/s|4.375 MB/s|
GPIB/HPIB (IEEE-488.1-2003) IEEE-488 max.|64 Mbit/s|8 MB/s|
FireWire (IEEE 1394) 100|98.304 Mbit/s|12.288 MB/s|1995
FireWire (IEEE 1394) 200|196.608 Mbit/s|24.576 MB/s|1995
FireWire (IEEE 1394) 400|393.216 Mbit/s|49.152 MB/s|1995
USB 2.0 high speed|480 Mbit/s|60 MB/s|2000
FireWire (IEEE 1394b) 800[63]|786.432 Mbit/s|98.304 MB/s|2002
Fibre Channel 1 Gb SCSI|1.0625 Gbit/s|100 MB/s|
FireWire (IEEE 1394b) 1600[63]|1.573 Gbit/s|196.6 MB/s|2007
Fibre Channel 2 Gb SCSI|2.125 Gbit/s|200 MB/s|
eSATA (SATA 300)|3 Gbit/s|300 MB/s|2004
CoaXPress Base (up and down bidirectional link)|3.125 Gbit/s + 20.833 Mbit/s|390 MB/s|2009
FireWire (IEEE 1394b) 3200[63]|3.1457 Gbit/s|393.216 MB/s|2007
External PCI Express 2.0 ×1|4 Gbit/s|500 MB/s|
Fibre Channel 4 Gb SCSI|4.25 Gbit/s|531.25 MB/s|
USB 3.0 SuperSpeed (aka USB 3.1 Gen 1)|5 Gbit/s|500 MB/s|2010
eSATA (SATA 600)|6 Gbit/s|600 MB/s|2011
CoaXPress full (up and down bidirectional link)|6.25 Gbit/s + 20.833 Mbit/s|781 MB/s|2009
External PCI Express 2.0 ×2|8 Gbit/s|1 GB/s|
USB 3.1 SuperSpeed+ (aka USB 3.1 Gen 2)|10 Gbit/s|1.212 GB/s|2013
External PCI Express 2.0 ×4|16 Gbit/s|2 GB/s|
Thunderbolt|2 × 10 Gbit/s|2 × 1.25 GB/s|2011
USB 3.2 SuperSpeed+[64] (aka USB 3.2 Gen 2×2)|20 Gbit/s|2.424 GB/s|2017
Thunderbolt 2|20 Gbit/s|2.5 GB/s|2013
External PCI Express 2.0 ×8|32 Gbit/s|4 GB/s|
Thunderbolt 3 two links|40 Gbit/s|5 GB/s|2015
USB4[65]|40 Gbit/s|5 GB/s|2019
External PCI Express 2.0 ×16|64 Gbit/s|8 GB/s"""

import matplotlib.pyplot as plt

def read_table(table):
    xyz = []
    for row in table.split('\n'):
        z, x, y = row.split('|')[-3:]
        x = float(x.split('[')[0].split('/')[0])
        #print(y.split('[')[0])
        y = float(y.split('[')[0])
        xyz.append((x,y,z))

    x, y, z = zip(*xyz)

    return x, y, z

def read_table_2(table):
    xyz = []
    for row in table.split('\n'):
        try:
            name, rate_bit, rate_byte, year = row.split('|')
            if year:
                rate_bit = rate_bit.lower()
                num, unit = rate_bit.split(' ')
                dunit, tunit = unit.split('/')
                #
                if dunit == 'kbit':
                    mult = 1
                elif dunit == 'mbit':
                    mult = 1e3
                elif dunit == 'gbit':
                    mult = 1e6
                #
                num = float(num)
                num *= mult
                #
                year = int(year)
                xyz.append((num, year, name))
        except ValueError:
            print('bad row', row)

    x, y, z = zip(*xyz)

    return x, y, z

if __name__ == '__main__':
    x, y, z = read_table(modem_table)
    plt.semilogy(y, x, 'o', label='modems (analog)')
    x, y, z = read_table_2(peripheral_table)
    plt.semilogy(y, x, 'o', label='peripherals (digital)')
    #
    plt.xlabel('Year')
    plt.ylabel('Transmission rate in kbit/s')
    #
    plt.legend()
    #
    plt.savefig('exponential-growth.png')
    plt.show()
