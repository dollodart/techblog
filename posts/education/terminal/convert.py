with open('terminal.rst','r') as _:
    chars = _.read()

l = len(chars)
pat = ':kbd:'
lpat = len(pat)
c = 0
out = ''
while c < l - lpat:
    if pat == chars[c:c + lpat]:
        in_kbd = True
        out += pat
        c += lpat
        assert chars[c] == '`'
        out += chars[c]
        c += 1
        while chars[c] != '`':
            if chars[c] == '+':
                out += '` + ' + pat + '`'
            elif chars[c] == ',':
                out += '`, ' + pat + '`'
            else:
                out += chars[c]
            c += 1
    else:
        out += chars[c]
        c +=1

with open('2term.rst', 'w') as _:
    _.write(out)
