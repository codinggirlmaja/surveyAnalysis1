import pandas as pd


class AnalizaAnkete:
    def __init__(self, filename):
        self.dataset = pd.read_excel(filename)

    def prvihnkolona(self, n):
        """ Funkcija prvihnkolona pokrece metodu head koja prikazuje prvih pet redova baze podataka.

        Parametri
        ----------
        self: objekat
        n: broj redova

        Returns
        -------
        Prvih n redova baze podataka.
      """
        return self.dataset.head(n)

    def ukupanbrojredovaikolona(self):
        """ Funkcija ukupanbrojredovaikolona pokrece metodu shape koja prikazuje ukupan broj redova i kolona.

        Parametri
        ----------
        self: objekat

        Returns
        -------
        Broj redova i kolona baze podataka.
        """

        return self.dataset.shape

    def kolone(self):
        """ Funkcija kolone pokrece metodu columns koja išćitava imena svih kolona u bazi podataka...

        Parametri
        --------
        self: objekat

        Returns
        --------
        Imena svih kolona.
        """
        return self.dataset.columns

    def vrednostikategorija(self, column_name):
        """ Funkcija vrednostikategorija pokrece metodu value_counts koja računa vrednosti za svaku kategoriju određene kolone (pitanja).

        Parametri
        --------
        self: objekat
        column_name: ime kolone

        Returns
        --------
        Ukupne apsolutne vrednosti za sve kategorije određene kolone (određenog pitanja).
        """

        return self.dataset[column_name].value_counts()

    def raspodelakategorija(self, column_name):
        """ Funkcija raspodelakategorija pokrece metodu value_counts koja računa vrednosti za određenu kolonu u procentima.

        Parametri
        --------
        self: objekat
        column_name: ime kolone

        Returns
        --------
        Procentne vrednosti za sve kategorije određene kolone (određenog pitanja).

        """
        return self.dataset[column_name].value_counts(normalize=True)

    def dijagram(self, column_name):
        """ Funkcija dijagram pokrece metodu koja vraća trakastri dijagram za određenu kolonu.

        Parametri
        --------
        self: objekat
        column_name: ime kolone

        Returns
        --------
        Trakasti dijagram za određenu kolonu (određeno pitanje).

        """
        return self.dataset[column_name].value_counts().plot(kind='bar')

    def pita(self, column_name):
        """ Funkcija dijagram pokrece metodu koja vraća pita grafikon za određenu kolonu.

        Parametri
        --------
        self: objekat
        column_name: ime kolone

        Returns
        --------
        Pita grafikon za određenu kolonu (određeno pitanje).

        """
        return self.dataset[column_name].value_counts().plot(kind='pie')


# na osnovu definisane klase, kreiramo objekat koji će kao ulaz primiti rezultate ankete
ra = AnalizaAnkete('Ime ankete.xlsx')
dataset = pd.read_excel('Ime ankete.xlsx')

osnovnaanaliza = input("Da li želite da dobijete osnovni pregled rezultata ankete? ")

if osnovnaanaliza == "da":
    pregled = ra.prvihnkolona(5), ra.kolone(), ra.ukupanbrojredovaikolona()
    print(pregled)

    imekolone = input('Molim vas unesite ime kolone koju želite da analizite:')

    if imekolone in dataset.columns:
        specificnaanaliza = input(
            'Molim vas unesite željenu analizu nad izabranom kolonom [apsolutne vrednosti, vrednosti u procentima, trakasti dijagram, pita dijagram]')

        if specificnaanaliza == 'apsolutne vrednosti':
            vrednosti1 = ra.vrednostikategorija(imekolone)
            print(vrednosti1)
        elif specificnaanaliza == 'vrednosti u procentima':
            vrednosti2 = ra.raspodelakategorija(imekolone)
            print(vrednosti2)
        elif specificnaanaliza == 'trakasti dijagram':
            dijagram1 = ra.dijagram(imekolone)
            print(dijagram1)
        elif specificnaanaliza == 'pita dijagram':
            dijagram2 = ra.pita(imekolone)
            print(dijagram2)
        else:
            print('Niste uneli analizu koja spada u ponuđenu listu analiza, molim vas unesite tačno kako je napisano.')
            specificnaanaliza = input(
                'Molim vas unesite željenu analizu nad izabranom kolonom [apsolutne vrednosti, vrednosti u procentima, dijagram]:')
    else:
        print('Uneli ste nepostujuće ime kolone')
        imekolone = input('Molim vas unesite ime kolone koju želite da analizirate:')

else:
    imekolone = input('Molim vas unesite ime kolone koju želite da analizite:')
    if imekolone in dataset.columns:
        specificnaanaliza = input(
            'Molim vas unesite željenu analizu nad izabranom kolonom [apsolutne vrednosti, vrednosti u procentima, trakasti dijagram, pita dijagram]')

        if specificnaanaliza == 'apsolutne vrednosti':
            vrednosti1 = ra.vrednostikategorija(imekolone)
            print(vrednosti1)
        elif specificnaanaliza == 'vrednosti u procentima':
            vrednosti2 = ra.raspodelakategorija(imekolone)
            print(vrednosti2)
        elif specificnaanaliza == 'trakasti dijagram':
            dijagram1 = ra.dijagram(imekolone)
            print(dijagram1)
        elif specificnaanaliza == 'pita dijagram':
            dijagram2 = ra.pita(imekolone)
            print(dijagram2)
        else:
            print('Niste uneli analizu koja spada u ponuđenu listu analiza, molim vas unesite tačno kako je napisano.')
            specificnaanaliza = input(
                'Molim vas unesite željenu analizu nad izabranom kolonom [apsolutne vrednosti, vrednosti u procentima, dijagram]:')
    else:
        print('Uneli ste nepostujuće ime kolone')
        imekolone = input('Molim vas unesite ime kolone koju želite da analizirate:')