def penjumlahan(*numbers):
    results = 0
    for number in numbers:
        results += number
    return results


def perkalian(*numbers):
    results = 1
    for number in numbers:
        results *= number
    return results


def pembagian(*numbers):
    results = 0
    for number in range(len(numbers)):
        if (number == 0):
            results = numbers[number]
        else:
            results /= numbers[number]

    return results
