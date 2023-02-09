from module import Bolygo
bolygok:list[Bolygo] = []
file = open(file='solsys.txt', mode='r', encoding='utf-8')
for sor in file: bolygok.append(Bolygo(sor))

# elemek száma a listában:
print(f'a naprendszerben {len(bolygok)} db bolygó van')


# adott tulajdonság értékösszege a listában
holdak_szama_osszesen:int = 0
for b in bolygok:
    holdak_szama_osszesen += b.holdak_szama
print(f'a holdak száma a naprandszerben: {holdak_szama_osszesen}')
print(f'naprendszerünkben az egy bolygóra eső átlagos holdak száma: {round(holdak_szama_osszesen / len(bolygok), 2)}')

# adott tulajdonságú elemek száma
nagy_bolygok_szama:int = 0
for b in bolygok:
    if b.terfogat_arany > 1:
        nagy_bolygok_szama += 1
print(f'a Földnél nagyobb bolygók száma: {nagy_bolygok_szama}')


# a lista eleget tesz-e bizonyos állításnak, vagy sem
for b in bolygok:
    if b.holdak_szama > 30:
        print('van olyan bolygó, melynek több, mint 30 holdja van!')
        break
else: print('nincs olyan bolygó, aminek több, mint 30 holdja van')


# a listában megtalálható-e az adott tulajdonságú (azaz 1db) elem,
# és ha igen, akkor hol
keresett_bolygo_neve = input('írd be a keresett bolygó nevét: ')
for i in range(len(bolygok)):
    if bolygok[i].nev.lower() == keresett_bolygo_neve.lower():
        print(f'A(z) {bolygok[i].nev} holdjainak száma: {bolygok[i].holdak_szama}')
        print(f'A(z) {bolygok[i].nev} Földhöz mért térfogataránya: {bolygok[i].terfogat_arany}')
        break
else: print(f'{keresett_bolygo_neve} nevű bolygó nincs a naprendszerünkben')


# a listában bizonyos tulajdonság szerint adott szélsőértéket képviselő elem helye
maximum_v_index:int = 0
for i in range(1, len(bolygok)):
    if bolygok[i].terfogat_arany > bolygok[maximum_v_index].terfogat_arany:
        maximum_v_index = i
print(f'a legnagyobb bolygó a naprendszerben a(z) {bolygok[maximum_v_index].nev}')


# a eredeti listában adott tulajdonságnak megfelelő összes elem (szűrt) listája
nuszosok:list[str] = []
for b in bolygok:
    if 'nusz' in b.nev.lower():
        nuszosok.append(b.nev)
if len(nuszosok) > 0:
    print(f'azon bolygók a naprendszerben, melyek neve tartalmazza, hogy "nusz"')
    for n in nuszosok:
        print(f'{n}', end=' ')
    print(end='\n')
else: print('nincsenek a szűrési feltételnek megfelelő nevű bolygók a naprendszerünkben') 