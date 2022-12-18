def doMath():
    mathType = int(input('''
Tipe aritmatika:
1. Penjumlahan
2. Perkalian
3. Pembagian
                    
Pilih menu dari 3 angka diatas: '''))

    # Data Pengulangan dari operasi penjumlahan
    loopNumbers = [True, 0, []]
    number = 0
    if loopNumbers[0]:
        while loopNumbers[0]:
            if loopNumbers[1] > 1:
                if input('Do you want to stop?(y/n) ') == 'y':
                    loopNumbers[0] = False
                else:
                    loopNumbers[0] = True
                    number = int(
                        input('Bilangan: '))
            else:
                number = int(
                    input('Bilangan: '))
            loopNumbers[1] += 1
            loopNumbers[2].append(number)
    loopNumbers[2].pop()

    if mathType == 1:
        return f'Operation success, result: {penjumlahan(loopNumbers[2])}'
    elif mathType == 2:
        return f'Operation success, result: {perkalian(loopNumbers[2])}'
    elif mathType == 3:
        return f'Operation success, result: {perkalian(loopNumbers[2])}'
    else:
        if input('Failed, not found operation, try again please. (y/n): ') == 'y':
            doMath()
        else:
            return False


def penjumlahan(numbers):
    results = 0
    for number in numbers:
        results += number
    return results


def perkalian(numbers):
    results = 1
    for number in numbers:
        results *= number
    return results


def pembagian(numbers):
    results = 0
    for number in range(len(numbers)):
        if (number == 0):
            results = numbers[number]
        else:
            results /= numbers[number]

    return results
