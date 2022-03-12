from random import randint, seed
import argparse


def generator(s, p):
    seed(s)
    for i in range(p):
        print(randint(0, 10000))

        
def main():
    parse = argparse.ArgumentParser(
        description='Generator liczb od 0 do 10\'000')
    parse.add_argument('-s', '--seed', type=int, required=True,
                       metavar='', help='Wartość seeda')
    parse.add_argument('-p', '--powtorzenia', metavar='',
                       type=int, required=True, help='Ilość powtórzeń pętli')
    wyniki = parse.parse_args()
    generator(wyniki.seed, wyniki.powtorzenia)


if __name__ == '__main__':
    main()

# Wniosek:
# Dla takich samych wartości seeda są generowane takie same liczby | Do każdego seeda są przypisane konkretne liczby
