import numpy.random as r
from modbus import compute_crc

crcs = []
count_non_unique = 0
message_bytes = 6
byte_size = 8

r = r.randint(0, 0xff, size=message_bytes)
print(f'randomly generated {message_bytes} byte message:')
print(r)

for mb in range(message_bytes):
    for by in range(byte_size):
        rr = r.copy()
        m = 1 << by
        bs = rr[mb] & (~ m)

        if rr[mb] & m:
            rr[mb] = bs
        else:
            rr[mb] = bs + m
        crc = compute_crc(rr)

        if crc in crcs:
            count_non_unique += 1
        else:
            crcs.append(crc)

print(f'out of {byte_size*message_bytes} possible 1-bit errors in a {message_bytes} byte message',
      f'{count_non_unique} duplicate CRCs were calculated',
      f'{message_bytes*byte_size - count_non_unique} unique CRCs were calculated',sep='\n')
print('unique CRCs:')
print(crcs)

count_non_unique = 0
crcs = []

tot = 0
# iterate through pairs
for mb in range(message_bytes):
    for by in range(byte_size):
        for mbmb in range(mb + 1): # include current byte mb in iteration
            for byby in range(byte_size):
                if mbmb == mb: # only go up to current bit in current byte
                    if byby >= by: 
                        continue
                rr = r.copy()
                m = 1 << by
                bs = rr[mb] & (~ m)

                if rr[mb] & m:
                    rr[mb] = bs
                else:
                    rr[mb] = bs + m

                mm = 1 << byby
                bsbs = rr[mbmb] & (~ mm)

                if rr[mbmb] & mm:
                    rr[mbmb] = bsbs
                else:
                    rr[mbmb] = bsbs + mm

                crc = compute_crc(rr)

                if crc in crcs:
                    count_non_unique += 1
                else:
                    crcs.append(crc)
                tot += 1

assert tot == message_bytes*byte_size*(message_bytes*byte_size - 1) / 2

print(f'out of {tot} possible 2-bit errors in a {message_bytes} byte message',
      f'{count_non_unique} duplicate CRCs were calculated',
      f'{tot - count_non_unique} unique CRCs were calculated',sep='\n')
print('unique CRCs:')
print(crcs[:100], '...')
