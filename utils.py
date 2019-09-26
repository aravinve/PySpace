def find_max(numbers):
    maximum =  numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum