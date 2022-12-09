# Febry Billiyagi Karsidi - TI 02
# Tugas DDP Mencari huruf konsonan, dengan algoritma yang dinamis

def konsonan(param):
    konsonans = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                 "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    # Pecah parameter kata menjadi sebuah list
    i = 0
    paramArray = []
    paramUpper = []
    while i < len(param):
        if param[i].isupper():
            paramUpper.append(param[i])
        paramArray.append(param[i])
        i += 1

    # Filter list kata pada parameter dengan huruf konsonan
    paramFilter = []
    for karakterParam in paramArray:
        karakterParam = karakterParam.lower()
        if karakterParam in konsonans:
            paramFilter.append(karakterParam)

    # Gantikan Huruf asli, jika sebelumnya kapital akan menjadi kapital kembali
    for karakterNum in range(len(paramFilter)):
        if paramFilter[karakterNum].upper() in paramUpper:
            paramFilter[karakterNum] = paramFilter[karakterNum].upper()

    # Jadikan string, array dari hasil filter akan disatukan menjadi sebuah kata/teks
    results = ''.join(paramFilter)

    return results


print(konsonan('Nurul Fikri'))  # NrlFkr
print(konsonan('Febry Billiyagi'))  # FBryBllyg
