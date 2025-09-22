from math import sqrt

def isprime(p):
    if p < 2:
        return False
    else :
        for k in range(2, int(sqrt(p) + 1 )):
            if p%k == 0:
                return False
        return True


def main():
    n = int(input("Entrez un entier: "))
    if isprime(n):
        print(f"{n} est un nombre premier.")
    else:
        print(f"{n} n'est pas un nombre premier.")


    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
