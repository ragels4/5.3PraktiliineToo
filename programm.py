from funktsioonid import vahetus, generaator, jagamine, keskmine, lisamine

#создал списки которые не были defined
s = []
pos = []
neg = []
null = []
nol = []

# Põhifunktsioon
def arvud_loendis():
    """
Funktsioon loob kasutaja määratud arvu täisarvudega listi.
See sorteerib listi, jagab arvud positiivseteks, negatiivseteks ja nullideks,
arvutab iga grupi keskmise ja lisab need algsesse listi.
    """
    try:
        print("Andmed:")
        n = abs(int(input("Mitu täisarvu genereerime loendisse? => ")))
        mini = int(input("Sisesta vahemiku minimaalne arv => "))
        maxi = int(input("Sisesta vahemiku maksimaalne arv => "))
        
        if mini >= maxi:
            mini, maxi = maxi, mini

        # Genereeri loend
        generaator(n, s, mini, maxi)

        print("\nTulemused:")
        print("Saadud loend alates", mini, "kuni", maxi)
        s.sort()
        print("Sorteeritud loend", s)

        # Jagamine positiivseteks, negatiivseteks ja nullideks
        jagamine(s, pos, neg, nol)
        print("Positiivsete elementide loend", pos)
        print("Negatiivsete elementide loend", neg)
        print("Null-elementide loend", nol)

        # Positiivsete keskmine ja lisamine
        kesk = keskmine(pos)
        lisamine(s, kesk)
        print("Positiivsete keskmine:", kesk)

        # Negatiivsete keskmine ja lisamine
        kesk = keskmine(neg)
        lisamine(s, kesk)
        print("Negatiivsete keskmine:", kesk)

        # Lõplik sorteeritud loend
        print("Lisame keskmised algsesse massiivi:")
        s.sort()
        print(s)

    except ValueError:
        print("Palun sisesta ainult täisarvud.")

# Põhifunktsiooni käivitus
arvud_loendis()
