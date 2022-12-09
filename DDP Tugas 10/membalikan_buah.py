# Febry Billiyagi Karsidi - TI 02
# Membalikan list tanpa menggunakan fungsi/method sort()

buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']


def balikan(myArray):
    results = []
    myArrayLength = len(myArray)
    for buah in range(0, myArrayLength):
        results.append(myArray[myArrayLength-1])
        myArrayLength -= 1

    return results


print(balikan(buah))
