import hashlib
import argparse


def hashe(path):
    with open(path, 'rb') as plik:   # r - reading | b - binary
        zawartosc = plik.read()

        md4 = hashlib.new('md4')
        md5 = hashlib.md5()
        sha224 = hashlib.sha224()
        sha256 = hashlib.sha256()
        sha384 = hashlib.sha384()
        sha512 = hashlib.sha512()
        sha3_224 = hashlib.sha3_224()
        sha3_256 = hashlib.sha3_256()
        sha3_384 = hashlib.sha3_384()
        sha3_512 = hashlib.sha3_512()

        md4.update(zawartosc)
        md5.update(zawartosc)
        sha224.update(zawartosc)
        sha256.update(zawartosc)
        sha384.update(zawartosc)
        sha512.update(zawartosc)
        sha3_224.update(zawartosc)
        sha3_256.update(zawartosc)
        sha3_384.update(zawartosc)
        sha3_512.update(zawartosc)

        print(f'{md4.name}: {md4.hexdigest()}')
        print(f'{md5.name}: {md5.hexdigest()}')
        print(f'{sha224.name}: {sha224.hexdigest()}')
        print(f'{sha256.name}: {sha256.hexdigest()}')
        print(f'{sha384.name}: {sha384.hexdigest()}')
        print(f'{sha512.name}: {sha512.hexdigest()}')
        print(f'{sha3_224.name}: {sha3_224.hexdigest()}')
        print(f'{sha3_256.name}: {sha3_256.hexdigest()}')
        print(f'{sha3_384.name}: {sha3_384.hexdigest()}')
        print(f'{sha3_512.name}: {sha3_512.hexdigest()}')


def main():
    parse = argparse.ArgumentParser(
        description='Generator hashy dla danego pliku')
    parse.add_argument('-p', '--path', metavar='',
                       required=True, type=str, help='Ścieżka do pliku')
    wyniki = parse.parse_args()
    hashe(wyniki.path)


if __name__ == '__main__':
    main()

# Wniosek eksperymentu:
# Po zmianie zawartości pliku tekstowego hashe zostały zmienione
