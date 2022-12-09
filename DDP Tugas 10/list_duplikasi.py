# Febry Billiyagi Karsidi - TI 02
# List Duplikat


buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']


def duplikasi(myList):
    results = []
    for fruit in buah:
        spliting = (fruit + ' ') * 2
        for split in range(len(spliting.split())):
            results.append(spliting.split()[split])
    return results


print(duplikasi(buah))
