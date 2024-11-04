uang = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2
def cari_indeks(uang, y1, y2):
    if y1 in uang:
        return uang.index(y1)
    elif y2 in uang:
        return uang.index(y2)
    else:
        return 0
indeks = cari_indeks(uang, y1, y2)
print (indeks)