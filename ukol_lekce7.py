#vstupní text
TEXTS = ['''
    Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley. ''',

    '''At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.'''
    ]  

#úloha
"""
Text analyzér
-------------

Modul si vyžádá nejprve přihlašovací údaje. Pokud je uživatel uložený, může vybrat číslo textu (1-3) a modul mu zobrazí tyto informace:
- počet slov,
- počet slov začínajících velkým písmenem,
- počet slov pouze s malými písmeny,
- počet číslic,
- součet všech číselných hodnot,
- nejdelší slovo,
- nejčastější slovo,
- histogram.
"""

#databáze uživatelů
uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

#speciální znaky
oddelovac = "-" * 35
mezera = " " * 6

#input username
username = input('Uživatelské jméno: ')

#prihlaseni a vyzvani k heslu
if username in uzivatele.keys():
    password = input('Heslo: ')
else:
    print("Neregistrovaný uživatel")
    quit()
print(oddelovac)

# kontrola spravnosti hesla, vyzva k zadani cisla
if uzivatele.get(username) == password:
    print(f'Vítej v aplikaci, {username}. K analýze máš na výber ze 3 textů.')
    text_no = input('Zadej číslo mezi 1-3: ')
else:
    print('Heslo je špatné')
    quit()

print(oddelovac)

#kontrola zadaneho cisla
if text_no.isnumeric() and 1 <= int(text_no) <= 3:
    print('Statistiky')
else:
    print('Zadané číslo není v rozmezí 1-3.')
    text_no = input('Zadej číslo mezi 1-3: ')

#index 
txt_index = int(text_no)-1

#replace .,-
TEXTS[txt_index] = TEXTS[txt_index].replace('.', '').replace(',', '').replace('-', ' ')

#Statistiky vypocet
##pocet slov
pocet_slov = len(TEXTS[txt_index].split())

##počet slov začínajících velkým písmenem
title = len([slovo for slovo in TEXTS[txt_index].split() if slovo.istitle()])

##počet slov pouze s malými písmeny
lowercase = len([slovo for slovo in TEXTS[txt_index].split() if slovo.islower()])

##počet číslic
digit = len([int(cislo) for cislo in TEXTS[txt_index].split() if cislo.isnumeric()])

##součet všech číselných hodnot
suma = sum([int(cislo) for cislo in TEXTS[txt_index].split() if cislo.isnumeric()])

##nejdelší  slovo
words = TEXTS[txt_index].split()
lengths = [len(word) for word in words]
max_length = max(lengths)
max_word = [word for word in words if len(word) == max_length]

#nejčastější slovo
most_word = max(set(TEXTS[txt_index].split()), key = TEXTS[txt_index].split().count)
most_freq = TEXTS[txt_index].split().count(most_word)

#zobrazeni vysledku
print(f'Ve vybraném textu je {pocet_slov} slov.',
    f'Ve vybraném textu je {title} slov začínajících velkým písmenem.',
    f'Ve vybraném textu je {lowercase} slov složených pouze z malých písmen.',
    f'Ve vybraném textu jsou {digit} číslice.',
    f'Součet všech číselných hodnot je {suma}.',
    f'Nejdelší slovo je slovo "{max_word[0]}" dlouhé {max_length} symbolů.',
    f'Nejčastějším slovem je slovo "{most_word}" vyskytující se v textu celkem {most_freq}.',
    oddelovac,
    f'Delka slova {mezera} frekvence slova',
    oddelovac,
     sep= "\n")

##histogram 
tallies = [0 for x in range(max_length + 1)]
for length in lengths:
    tallies[length] += 1
total_words = len(words)
for length in range(len(tallies)):
    if tallies[length] != 0:
        freq = tallies[length]
        hodnoty = "*" * freq
        print(f'{length:3} {hodnoty:17} {freq:10d}')