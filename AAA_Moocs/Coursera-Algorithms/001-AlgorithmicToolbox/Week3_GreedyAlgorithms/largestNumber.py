def largestNumber(n):
    numbers =[int(x) for x in n.split(',')]
    # Calculate the combination of biggest
    print( ''.join([str(n) for n in sorted(numbers, reverse=True)]))


largestNumber('3,9,5,9,7,1')