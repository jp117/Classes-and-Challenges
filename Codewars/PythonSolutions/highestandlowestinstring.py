def high_and_low(numbers):
    x = numbers.split()
    ints = []
    for y in range (0,len(x)):
        ints.append(int(x[y]))
    print(ints)
    high = max(ints)
    low = min(ints)
    return ''.join(str(high) + ' ' + str(low))