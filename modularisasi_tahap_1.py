"""
Program menghitung luas segitiga
"""
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'segitiga dgn alas = {alas} dan tinggi = {tinggi} mempunyai luas = {luas_segitiga}')

print('\nmenghitung luas segitiga dgn copas')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'segitiga dgn alas = {alas} dan tinggi = {tinggi} mempunyai luas = {luas_segitiga}')

print('\nmenghitung luas segitiga dgn fungsi')


def luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'menghitung segitiga dgn fungsi, hasilnya = {luas_segitiga(10,6)}')
print(f'menghitung segitiga dgn fungsi, hasilnya = {luas_segitiga(20,2)}')
