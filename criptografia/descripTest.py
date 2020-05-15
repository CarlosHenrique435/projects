from collections import deque


def descrip(text):
    from alphabet import strings

    descripition = []
    almost = []

    rota = deque(strings())

    var = text.split('0x')
    for c in var[2:-1]:
        if c == '':
            pass
        else:
            descripition.append(int(f'0x{c}', 16) ^ int(f'0x{var[-1]}', 16))

    descripition.reverse()
    reversive = [chr(c) for c in descripition]

    rota.rotate(int(f'{var[1]}', 16))

    for final in ''.join(reversive):
        if final == "§":
            print(final)
        else:
            almost.append(rota.index(final))

    for c in almost:
        if c != '§':
            print(strings()[c], end='')
        else:
            pass


if __name__ == '__main__':
    descrip('0x572eb10x15dc248280x15dc2482c0x15dc2482f0x15dc248290x15dc248520x15dc2485e0x15dc248110x15dc248540x15dc248'
            '110x15dc248260x15dc2482e0x15dc2482c0x15dc2482d0x15dc248110x15dc248360x15dc248260x15dc2482e0x15dc248110x15dc'
            '248520x15dc2482f0x15dc2482c0x15dc24867')