#created by LP_R9SAAO

#Ez egy próba modul

def osszeg():
    egyik = int(input("Kérek egy számot: "))
    masik = int(input("Kérek másik számot: "))

    eredmeny = egyik + masik

    print("Az eredmény értéke".center(50))
    print(str(egyik).rjust(50, '-'))
    print(str(masik).rjust(50, '-'))
    print("+".rjust(50))
    print(str(eredmeny).rjust(50, '-'))
    return


def szorzas():
    egyik = int(input("Kérek egy számot: "))
    masik = int(input("Kérek másik számot: "))

    eredmeny = egyik * masik

    print("Az eredmény értéke".center(50))
    print(str(egyik).rjust(50, '-'))
    print(str(masik).rjust(50, '-'))
    print("*".rjust(50))
    print(str(eredmeny).rjust(50, '-'))
    return
