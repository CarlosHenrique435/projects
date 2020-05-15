from collections import deque
import argparse


def main():
    parse = argparse.ArgumentParser(description='Programa criptografar strings ou arquivos de textos')

    grupo = parse.add_mutually_exclusive_group()

    grupo.add_argument('-s', '--string', help="Get text", action='store')
    grupo.add_argument('-f', '--file', help='get text from file', action='store')

    args = parse.parse_args()

    if args.string:
        crip = cripString(args.string)
        print(crip)
    else:
        pass
        #getfile = cripFile(args.file)


def cripString(text):
    from alphabet import strings
    import random

    resultsCrip = []

    alphanot = deque(strings())
    alphaNorm = strings()
    rangeAvalue = random.randint(100,9999999999)
    valueRotate = random.randint(6,9999999)
    alphanot.rotate(valueRotate)

    for c in text:
        if c in alphaNorm:
            resultsCrip.append(alphanot[alphaNorm.index(c)])
        else:
            resultsCrip.append('§')

    CripText = ''.join(resultsCrip)

    FinalResult = [ord(c) for c in CripText]

    FinalResult.reverse()

    Final = [str(c) for c in FinalResult]
    FinalResult.clear()
    resultsCrip.clear()

    FinalMaster = []

    FinalMaster.append(str(hex(valueRotate)))
    for c in Final:
        FinalMaster.append(hex(int(c) ^ rangeAvalue))
    FinalMaster.append(hex(rangeAvalue))
    return ''.join(FinalMaster)


if __name__ == '__main__':
    main()
